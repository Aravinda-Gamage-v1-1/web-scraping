import requests
from bs4 import BeautifulSoup

# making a GET request
response = requests.get('https://example.com/')

# check status code for response received
# success code = 200
print(response)

# parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())