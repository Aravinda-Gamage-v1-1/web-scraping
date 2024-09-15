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
        next_paragraph = heading.find_next('p')

        # store heading and content
        headings.append(heading_text)
        if next_paragraph:
            content.append(next_paragraph.text.strip())
        else:
            content.append("") # In case there's no paragraph after the heading

    # create a DataFrame from the lists
    df = pd.DataFrame({'heading': headings, 'Content': content})

    # write the DataFrame to an Execel file
    df.to_excel("csvToExcel.xlsx", sheet_name="Headings and Content", index= False)

    print("Data successfully written to 'web_data.xlsx'")

else:
    print("Error")
