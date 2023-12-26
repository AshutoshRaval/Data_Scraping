# main.py
from web_scraper import fetch_page, parse_table, save_to_csv

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
html_content = fetch_page(url)
if html_content:
    df = parse_table(html_content)
    if not df.empty:
        save_to_csv(df, 'D:/DataScraping/Companies12.csv')
