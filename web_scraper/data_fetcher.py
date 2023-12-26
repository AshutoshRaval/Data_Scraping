# data_fetcher.py
import requests

def fetch_page(url):
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        response.raise_for_status()
