import requests
from bs4 import BeautifulSoup
import uuid

def get_doc_and_save():
    url = 'https://indiankanoon.org/doc/1426993/'
    response = requests.get(url)

    if response.status_code == 200:
        # `print(response.text)` is printing the HTML content of the webpage that was fetched using
        # the `requests` library.
        # print(response.text)
        save_content(response.text)

    else:
        print(f"Failed to get the webpage: status code {response.status_code}")

def save_content(response_text):
    soup = BeautifulSoup(response_text, 'html.parser')
    try:
        try:
            title = soup.find('div', class_='doc_title').get_text(strip=True)
        except:
            title= f"{uuid.uuid4()}.txt"
        
        content = soup.find('div', class_='judgments').get_text(strip=True)

        # Generate a unique filename for the text file
        file_name = f"{title}.txt"
        
        # Save the content in a text file
        with open(f'cases/{file_name}', 'w', encoding='utf-8') as file:
            print(content)
            file.write(content)
    except Exception as e:
        print("something went wrong", e)

# Call the function
get_doc_and_save()
