# Wikipedia Page Scraper

This project is a simple Python web scraper that extracts data from Wikipedia pages and saves it as a CSV file. The scraper focuses on the "List of largest companies in the United States by revenue" page as an example.

## Features

- Fetches HTML content from a specified Wikipedia page.
- Parses and extracts table data using BeautifulSoup.
- Saves the extracted data into a CSV file.


## Usage

Follow these steps to use the Wikipedia Page Scraper:

1. **Import the Package:**
   Start by importing the necessary functions from the `web_scraper` package.

   ```python
   from web_scraper import fetch_page, parse_table, save_to_csv

