# On importe la fonction 'get' (téléchargement) de 'requests' 
# Et la classe 'Selector' (Parsing) de 'scrapy'
from requests import get
from scrapy import Selector
# Lien de la page à scraper
url = "https://www.seloger.com/immobilier/locations/immo-paris-75/bien-appartement"
response = get(url)
source = None # Le code source de la page 
if response.status_code == 200 :
    # Si la requete s'est bien passee
    source = response.text
    print (response.text)

if source :
    # Si le code source existe
    selector = Selector(text=source)
    titles = selector.css("div.root li")
    fichier = open("texte.csv", mode="a")

    for title in titles:
        level = title.css("span.tocnumber::text").extract_first()
        name = title.css("span.toctext::text").extract_first()
        print(level + " " + name)
        fichier.write(level + ";" + name + "\n")


##fichier.write(level + " " + name)
##print (fichier)
##fichier.close()
