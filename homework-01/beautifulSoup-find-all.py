import requests
from bs4 import BeautifulSoup

# making a GET request
response = requests.get('https://www.geeksforgeeks.org/fundamentals-of-algorithms/')

# parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')

s = soup.find('div', class_ = 'text')
content = s.find_all('p')

print(content)