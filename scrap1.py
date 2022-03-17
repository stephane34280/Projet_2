import requests
import bs4
import pandas as pd

##token = 'https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement/?LISTING-LISTpg='
token = 'https://www.google.fr'
def get_pages(token, nb):
    pages = []
    for i in range(1,nb+1):
        j = token + str(i)
        pages.append(j)
    return pages
pages = get_pages(token,295)


for i in pages:
   response = requests.get(i)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
em_box = soup.find_all("em", {"class":"agency-website"})

parameters = ['data-prix','data-codepostal','data-idagence','data-idannonce','data-nb_chambres','data-nb_pieces','data-surface','data-typebien']
df_f = pd.DataFrame()
for par in parameters:
    l = []
    for el in em_box:
        j = el[par]
        l.append(j)
    l = pd.DataFrame(l, columns = [par])
    df_f = pd.concat([df_f,l], axis = 1)

import itertools as it
proxies = pd.read_csv('proxy_list.txt', header = None)
proxies = proxies.values.tolist()
proxies = list(it.chain.from_iterable(proxies))
proxy_pool = it.cycle(proxies)
proxy = next(proxy_pool)

import random
import time
# !pip install fake-useragent
from fake_useragent import UserAgent
ua = UserAgent()
time.sleep(random.randrange(1,5))

response = requests.get(i,proxies={"http": proxy, "https": proxy}, headers={'User-Agent': ua.random},timeout=5)

while len(pages) > 0:
    try:
       ...
       pages.remove(i)
    except:
       print("Skipping. Connnection error")