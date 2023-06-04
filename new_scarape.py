import os
import uuid
import cloudscraper
from bs4 import BeautifulSoup

ACCESS_ID = 'DO008G7NQJWP9X94A9DU'
SECRET_KEY = 'qv67dcZlrGQKeGLT0/jAxMXMUn5lC5qc26gvb+bmm50'
i=0

def save_content(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    try:
        try:
            title = soup.find('div', class_='doc_title').get_text(strip=True)
        except:
            title= f"{uuid.uuid4()}.txt"

        content = soup.find('div', class_='judgments').get_text(strip=True)
        file_name = f"{title}.txt"
        
        if not os.path.exists('cases'):
            os.makedirs('cases')
        
        with open(f'cases/{file_name}', 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print("something went wrong", e)

all_urls = []
scraper = cloudscraper.create_scraper()

for i in range(0,20):
    url = f"https://indiankanoon.org/search/?formInput=doctypes%3A%20supremecourt%20fromdate%3A%2011-1-1972%20todate%3A%2031-3-2023%20sortby%3A%20leastrecent&pagenum={i}"
    response = scraper.get(url, timeout=15) 

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all(class_ = "result_title")

    base_url = "https://indiankanoon.org"

    for div in links:
        a_tag = div.find('a')
        href = a_tag['href']
        full_url = f"{base_url}{href}"
        all_urls.append(full_url)

        response = scraper.get(full_url, timeout=15)
        save_content(response.text)

# for i in all_urls:
#     print("all urls")
#     print(i)

# with open('urls.txt', 'w') as f:
#     for url in all_urls:
#         f.write("'"+url + "',")
