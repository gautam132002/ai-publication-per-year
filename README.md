# Publication Scraper: Arxiv and Google Scholar

This repository contains a web scraper for extracting the number of publications from Google Scholar and Arxiv separately. It focuses on the following topics: 'Deep Learning', 'Reinforcement Learning', 'Transfer Learning', and 'Causality'. The scraper retrieves the publication count for each topic per year and provides functionality to plot the data in graphs.

## Usage

To use this scraper, follow the steps below:

1. Activate the virtual environment by running the following command:

   ```
   source/bin/activate
   ```

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. For more detailed information and instructions, please refer to the provided documentation in the `doc.pdf` file.

## Program Files

This repository includes the following program files:

- `arxiv.py`: This script scrapes Arxiv for publications, collects the data, and plots graphs based on the scraped data.
- `scholar.py`: This script scrapes Google Scholar for publications, collects the data, and plots graphs based on the scraped data.
- `plot.py`: This script is a PyQt5 application that allows users to select a CSV file and plots the data contained in the file.

## Scraped Data

The repository already includes pre-scraped data in the `./extracted_by_gautam` directory for both Arxiv and Google Scholar:

- Arxiv: The file `./extracted_by_gautam/publication_counts_arxiv.csv` contains the publication counts for the specified topics from Arxiv.
- Google Scholar: The file `./extracted_by_gautam/publication_counts.csv` contains the publication counts for the specified topics from Google Scholar.

You can directly use the `plot.py` script on these CSV files to visualize the data in the form of line graphs.

## Additional Details

This scraper is designed to retrieve the number of publications for specific topics from Arxiv and Google Scholar. It utilizes web scraping techniques to extract the required data. However, please note that web scraping may be subject to the terms and conditions of the websites being scraped. Ensure that you comply with the policies and guidelines of Arxiv and Google Scholar or any other platforms you scrape.

The scraper collects the publication counts for the topics 'Deep Learning', 'Reinforcement Learning', 'Transfer Learning', and 'Causality' on a yearly basis. It then provides a convenient way to plot the data using the `plot.py` script. The script uses the PyQt5 library to create a graphical user interface (GUI) where you can select the CSV file containing the data and visualize it as a line graph.

Please refer to the provided documentation or contact the repository owner for further information or assistance.

## Contribution

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or additional features. Your contributions are greatly appreciated!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to the terms of this license.