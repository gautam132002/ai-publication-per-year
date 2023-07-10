import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

def search_publications(query, year):

    # Build the URL for the search
    url = f"https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=%27'{query}'%27&terms-0-field=all&classification-computer_science=y&classification-economics=y&classification-eess=y&classification-physics=y&classification-physics_archives=all&classification-q_biology=y&classification-q_finance=y&classification-statistics=y&classification-include_cross_list=include&date-filter_by=specific_year&date-year={year}&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=50&order=-announced_date_first"

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the publication count
    count_elem = soup.find('h1', {'class': 'title is-clearfix'})


    # Extract the publication count from the element
    try:
        count_text = count_elem.text.strip().split(" ")[3] 
        count_text = count_text.strip().replace(",", "")
        count_text = int(count_text)
    except:
        count_text = 0
        pass

    return count_text

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Deep Learning', 'Reinforcement Learning', 'Transfer Learning', 'Causality'])
        
        for year in data.keys():
            writer.writerow([year] + data[year])

# Topics to search for
topics = ['deep learning', 'reinforcement learning', 'transfer learning', 'causality']

# Dictionary to store publication counts for each topic and year
publication_counts = {year: [0, 0, 0, 0] for year in range(1990, 2024)}

def process_topic(topic):
    for year in tqdm(range(1990, 2024), desc=f"Processing {topic}"):
        count = search_publications(topic, year)
        publication_counts[year][topics.index(topic)] = count

# Create a ThreadPoolExecutor with the number of threads equal to the number of topics
with ThreadPoolExecutor(max_workers=len(topics)) as executor:
    # Submit the tasks for each topic
    futures = [executor.submit(process_topic, topic) for topic in topics]

    for future in futures:
        future.result()

filename = 'publication_counts_arxiv.csv'
save_to_csv(publication_counts, filename)

# =======  CODE TO PLOT DATA =================

df = pd.read_csv(filename)

# Extract the data for plotting
years = df['Year']
query_data = df.drop('Year', axis=1)

# Set up the plot
plt.figure(figsize=(10, 6))

# Iterate over the query data and plot each line with a different color
colors = ['blue', 'green', 'red', 'purple']
labels = query_data.columns

for i, query in enumerate(query_data.columns):
    plt.plot(years, query_data[query], color=colors[i], label=labels[i])

# Set the plot title and labels
plt.title('Publication Counts over Time')
plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.legend()
plt.show()