import requests
from bs4 import BeautifulSoup

# making a GET request
response = requests.get('https://example.com/')

# parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')

s = soup.find('div', class_ = 'entry-content')
content = s.find_all('p')

print(content)