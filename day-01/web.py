# import requered libs
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# url of the page to scrap
url = "https://example.com/"

# send a get request of the server
response = requests.get(url)

if response.status_code == 200:

    # parsing the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # get all code
    # print(response.text)

    # get tags inside content
    # print(soup.p.text)

    # print(soup.a.string)
    # print(soup.p.string)
    # print(soup.h1.string)

    tags = soup.find_all(['h1', 'p'])
    for tag in tags:
        print(tag.text.strip())
else:
    print("Error")