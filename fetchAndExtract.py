import re
import time
from googlesearch import search

urlsListFile = open("URLs_List.txt", "r")
prefix = 'https://www.lepanierbleu.ca/fr/marchands/'

def getWebsiteName(urlsListFile):
    sitesNamesList = []
    for link in urlsListFile:
        if link.startswith(prefix):
            linkSliced = re.sub(f"^{prefix}", "", link)
            sitesNamesList.append(linkSliced)       
    return sitesNamesList

def lookForWebsites(websitesNames):
    # en_tete = ["titre", "description"]
    with open('data.csv', 'w') as sitesUrlsFile:
        for siteName in websitesNames:
            try:
                time.sleep(1)
                result = next(search(siteName + " website", num_results=1))
                # sitesUrlsFile.write(f"Top website found for {siteName} : {result}")
                print(f"Top website found for {siteName} : {result}")
            except StopIteration:
                print(f"No website found for {siteName}")
            except Exception as e:
                print(f"Error occurred for {siteName}: {str(e)}")
                break  # Optionally break after an error or handle it differently
    
websitesNames = getWebsiteName(urlsListFile)
lookForWebsites(websitesNames)

# if response.status_code == 200 :
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a')
    
#     prefix = 'https://www.lepanierbleu.ca/fr/marchands'
#     prefix = '/web/'
#     matching_links = []
#     for link in links:
#         # if link.text.startswith(prefix):
#         if link.get('href') and link['href'].startswith(prefix):
#             print(link.text)
#             matching_links.append(link['href'])
#         else:
#             print(f"Failed to fetch the webpage: status code {response.status_code}")
