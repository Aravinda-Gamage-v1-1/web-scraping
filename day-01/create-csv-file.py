# improt requered libs
import requests
from bs4 import BeautifulSoup
import pandas as pd

# define the url
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

# get the response from the url
response = requests.get(url)

# check if the request was success
if response.status_code == 200:

    # parse the content
    soup = BeautifulSoup(response.content, 'html.parser')

    # list to store headings and their related content
    headings = []
    content = []

    # find all heading (h2) and paragraphs (p) and store them
    for heading in soup.find_all('h2'):
        heading_text = heading.text.strip()

        # get the next paragraph after each heading
        next_
