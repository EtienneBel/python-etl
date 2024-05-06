import requests

from bs4 import BeautifulSoup

url = "https://web.archive.org/web/*/https://www.lepanierbleu.ca/fr/marchands*"
response = requests.get(url)

if response.status_code == 200 :
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    # prefix = 'https://www.lepanierbleu.ca/fr/marchands'
    prefix = '/web/'
    matching_links = []
    for link in links:
        # if link.text.startswith(prefix):
        if link.get('href') and link['href'].startswith(prefix):
            print(link.text)
            matching_links.append(link['href'])
        else:
            print(f"Failed to fetch the webpage: status code {response.status_code}")
