# parser.py
from bs4 import BeautifulSoup
import pandas as pd

def parse_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable sortable')

    for table in tables:
        titles = table.find_all('th')
        world_table_titles = [title.text.strip() for title in titles]
        df = pd.DataFrame(columns=world_table_titles)
        column_data = table.find_all('tr')

        for row in column_data[1:]:
            row_data = row.find_all('td')
            individual_row_data = [data.text.strip() for data in row_data]
            length = len(df)
            df.loc[length] = individual_row_data
        
        return df  # Assuming we're interested in the first table only
