from sqlite3 import Cursor
import psycopg2
import requests
from bs4 import BeautifulSoup
import uuid
import random
import os.path
import sys, os



from boto3 import session

from botocore.client import Config

ACCESS_ID = 'DO008G7NQJWP9X94A9DU'
SECRET_KEY = 'qv67dcZlrGQKeGLT0/jAxMXMUn5lC5qc26gvb+bmm50'
i=0


def save_content(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    try:
        # Extract the desired content here. For example, you may want to extract
        # the text inside a specific div or paragraph with a specific class or id.
        # Replace 'div_class' with the actual class or id name.
        try:
            title = soup.find('div', class_='doc_title').get_text(strip=True)
        except:
            title= f"{uuid.uuid4()}.txt"

        content = soup.find('div', class_='judgments').get_text(strip=True)
        
        # Generate a unique filename for the text file
        file_name = f"{title}.txt"
        
        # Save the content in a text file

        with open(f'cases/{file_name}', 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print("something went wrong",e)

all_urls = []
for i in range(0,20):

# for J in range(1,10):
    url = f"https://indiankanoon.org/search/?formInput=doctypes%3A%20supremecourt%20fromdate%3A%2011-4-1963%20todate%3A%2031-3-2023%20sortby%3A%20leastrecent&pagenum={i}"


    # Requests URL and get response object
    response = requests.get(url,timeout=15) 

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all(class_ = "result_title")
    print((links))
    base_url = "https://indiankanoon.org"

    for div in links:
        # Find the nested <a> tag
        a_tag = div.find('a')
        
        # Get the href attribute value
        href = a_tag['href']
        
        # Print the href value
        print(href)
        # href = link['href']
        full_url = f"{base_url}{href}"
        all_urls.append(full_url)

        response = requests.get(full_url, timeout=15)
        
        # # Call a function to save the content in a text file (defined in the next step)
        save_content(response.text)

for i in all_urls:
    print("all urls")
    print(i)

with open('urls.txt', 'w') as f:
    for url in all_urls:
        f.write("'"+url + "',")



