from requests import get
from bs4 import BeautifulSoup

# Lien de la page à scraper
url = "http://books.toscrape.com/"

# url de la page
response = get(url)

#variables listes
side_categories = []
article = []
product_page_url = []
upc = []
titre = []
price_including_tax = []
price_excluding_tax = []
number_available = []
product_description = []
category = []
review_rating = []
image_url = []
liste_produits = []

# Si la requete est ok
if response.ok :
    # recuperation page html
    soup=BeautifulSoup(response.text, "lxml")
    # recuperation de tout le code classe "article"
    article=soup.findAll("article")
    # recuperation de tout le code classe "side_categories"
    side_categories=soup.find("div", {"class" : "side_categories"}).findAll("a")

    # toutes premieres pages produits/categories
    #for i in side_categories :
        #print (url+i["href"])
        #print (i.text)

    #print("side_categories : "+side_categories)
    #print.append("article : "+article[1])

    #print (len(side_categories))
    
    """for i in side_categories :
        liste_produits.append(i.find("a")["href"])
        response = get(liste_produits[0])
        soup=BeautifulSoup(response.text, "lxml")
        print(liste_produits.append(i.find("a")["href"]))
        print("liste_produits : "+side_categories[0])"""

    #for i in soup.findAll("strong") :
        #print ("strong : "+i)
    print ("nombre total articles : "+soup.findAll("strong")[0].text)
    print ("nombre articles par page : "+soup.findAll("strong")[2].text)
    total = soup.findAll("strong")[0].text
    pages = soup.findAll("strong")[2].text
    division = int(total)//int(pages)
    print (division)
    divisiontext = str(division)
    print ("nombre pages : "+divisiontext)

    for i in article :

        #product_page_url
        product_page_url.append(url+i.find("a")["href"])
        response = get(product_page_url[-1])
        soup=BeautifulSoup(response.text, "lxml")
        titre.append(soup.find("h1").text)
        print ("titre 1 : "+titre[-1])    

        # recuperation td
        td = soup.find_all ("td")
        upc = soup.find_all ("td")[0].text
        price_excluding_tax = soup.find ("th", text="Price (excl. tax)").find_next_sibling("td").text
        #product_description = soup.find ("article")("p").text
        #product_description.append(i.find("p").text)
        #product_description = soup.find ("p").text
        #print ("product_page_url : "+product_page_url[-1])
        #print ("universal_ product_code (upc) : "+td[0].text)
        #print ("title : "+titre[-1])
        #print ("price_including_tax : "+td[2].text[2:])
        #print ("price_excluding_tax : "+price_excluding_tax[2:])
        #print ("product_description : "+product_description[-1])

        #methode 3
        taxe = soup.find ("th", text="Tax").parent.find("td").text
        #print ("taxe : "+taxe[2:])
        #product_description
        #for i in article :
        #    product_description = i.find ["p"].text
        #print ("product_description : "+product_description[-1])

        image = soup.find ("img")["src"]
        #print ("image : "+"http://books.toscrape.com/"+image[6:])

"""
# recuperation titre
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
# recuperation th
    for lignes_th in soup.find_all ("th") :
	    print("ligne th : "+lignes_th.text)
# recuperation td
    for lignes_td in soup.find_all ("td") :
	    print("ligne td : "+lignes_td.text)
"""
