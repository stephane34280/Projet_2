import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrap_book(url):
    response1=requests.get(url)
    if response1.ok:
        soup1=BeautifulSoup(response1.text)
        upc=soup1.find("th",text="UPC").parent.find("td").text
        title=soup1.find("h1").text
        price_excl=soup1.find("th",text="Price (excl. tax)").parent.find("td").text[1:]
        price_incl=soup1.find("th",text="Price (incl. tax)").parent.find("td").text[1:]
        availability=soup1.find("th",text="Availability").parent.find("td").text[10:-11]
        #description=soup1.find("div",{"id":"product_description"}).find_next_sibling("p").text
        description=""
        review=soup1.find("i",{"class":"icon-star"}).parent["class"][1]
        image_url="http://books.toscrape.com/"+soup1.find("img")["src"][6:]
    return url,upc,title,price_excl,price_incl,availability,review,image_url,description
print (scrap_book("http://books.toscrape.com/")[])

"""
def get_list_books(url):
        response=requests.get(url)
        if response.ok:
            soup=BeautifulSoup(response.text)
            article=soup.findAll("article")
            return list(map(lambda x:"http://books.toscrape.com/catalogue/"+x.find("a")["href"][9:],article))
"""
"""
def category_find(url):
    response=requests.get(url)
    if response.ok:
        soup=BeautifulSoup(response.text)
        num_pages=int(soup.findAll("strong")[1].text)
        num_pages=1+num_pages//20
    category=url.replace("http://books.toscrape.com/catalogue/category/books/","").replace("/index.html","")
    return category,num_pages
"""
"""
def list_categories():
    url="http://books.toscrape.com/catalogue/page-1.html"
    response=requests.get(url)
    if response.ok:
        soup=BeautifulSoup(response.text)
        return list(map(lambda i:"http://books.toscrape.com/catalogue/"+i["href"],soup.find("ul",{"class":"nav nav-list"}).findAll("a")[1:]))
"""
"""
listy=[]
for i in list_categories():
    categ=category_find(i)[0]
    for k in get_list_books(i):
        listy.append(list(scrap_book(k)).append(categ))
    for j in range(1,category_find(i)[1]):
        url="http://books.toscrape.com/catalogue/category/books/"+category_find(i)[0]+"/page-"+str(j+1)+".html"
        for k in get_list_books(url):
            listy.append(list(scrap_book(k)).append(categ))

p=pd.DataFrame(listy,columns=["category","url","upc","title","price excl tax","price incl tax","availability","review","image_url","description"])
p.to_csv(r"C:/Users/Imen/Desktop/scrap.csv",index=False)
"""