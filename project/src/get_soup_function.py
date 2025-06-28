# import different modules and libraries
import requests
from bs4 import BeautifulSoup


# Function to retrieve the content of the page from this URL.
# And then the Content to the BeautifulSoup Library to give for parsing and structuring.
def get_soup(url: str):
    # The header is used to specify information about the web browser or client.
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                             'Chrome/91.0.4472.124 Safari/537.36'}
    src = requests.get(url, headers=headers).content
    beautiful_soup = BeautifulSoup(src, 'lxml')

    return beautiful_soup

