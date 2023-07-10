import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt

def search_publications(query, year):

    search_query = f"{query}"
    url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&as_ylo={year}&as_yhi={year}&q='{search_query}'&btnG="

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element that contains the publication count
    count_elem = soup.find('div', {'id': 'gs_ab_md'})

    # Extract the publication count from the element
    count_text = count_elem.text.strip().split()[1]  
    count_text = count_text.strip().replace(",", "")
    try:
        count_text = int(count_text)
    except:
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
    futures = [executor.submit(process_topic, topic) for topic in topics]
    for future in futures:
        future.result()

filename = 'publication_counts_scholar.csv'
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