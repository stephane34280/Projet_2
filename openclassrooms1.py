#openclassrooms1

# On importe la fonction 'get' (téléchargement) de 'requests' 
# Et la classe 'Selector' (Parsing) de 'scrapy'
from requests import get
from bs4 import BeautifulSoup
#from scrapy import Selector
# Lien de la page à scraper
url = "http://books.toscrape.com/"

#l'url de la page
response = get(url)
#print ("response : "+response.text)

#le code source de la page
source = BeautifulSoup (response.text, "lxml")
#print ("source : "+source)
#if response.status_code == 200 :
if response.ok :
    # Si la requete s'est bien passee
    #source = response.text
    #print (response.text)
    soup=BeautifulSoup(response.text, "lxml")
    article=soup.findAll("article")
    for i in article :
        #print (i)
        lien = i.find("a")["href"]
        print ("product_page_url : "+url+lien)
# recuperation title
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = get(url)
source = None
if response.ok :
    soup=BeautifulSoup(response.text, "lxml")
    titre = soup.find("h1")
    print ("titre : "+titre.text)

# recuperation upc
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = get(url)
source = None
if response.ok :
    soup=BeautifulSoup(response.text, "lxml")
    #upc = soup.find("td")
    #print (upc.text)

    for lignes_th in soup.find_all ("th") :
	    print("ligne th : "+lignes_th.text)

    for lignes_td in soup.find_all ("td") :
	    print("ligne td : "+lignes_td.text)

    #image = soup.find ("src", "img", id="product_gallery")
    #print ("image : "+image.text)

    #image_url = soup.find("src", attrs={"alt" : "A Light in the Attic"}, id="product_gallery")

    article1=soup.find(class_="item active")
    print ("essai 1 : "+article1.text)
    #image_url = soup.find("src", "img", class_="article")
    #print ("image_url : "+image_url.text.string)

    #product = soup.find_next("td").product_type.strip
    #print (product)