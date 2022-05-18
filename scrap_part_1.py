import requests
from bs4 import BeautifulSoup
import csv
import os


# Création de fonction pour chaque données requises:

#UPC
def upc_page(soup):
    tds = soup.findAll("td")
    upc = tds[0].text
    return upc

#Titre
def title_page(soup):
    title = soup.h1.text
    return title

#Prix Inclus Taxe
def price_inc_tax_page(soup):
    tds = soup.findAll("td")
    price = tds[3].text
    return price

#Prix Exclus Taxe
def price_excl_tax_page(soup):
    tds = soup.findAll("td")
    price = tds[2].text
    return price

#Disponibilité
def available_page(soup):
    tds = soup.findAll("td")
    available = tds[5].text
    num_list = []
    for num in available:   
        if num.isdigit():
            num_list.append(num)
            continue
    num_available = "".join(num_list)
    return num_available

#Description
def description_page(soup):
    p_soup = soup.findAll("p")
    description = p_soup[3].text
    return description
    
#Categorie
def category_page(soup):
    ul = soup.find("ul", class_="breadcrumb")
    ul_list = list(ul)[5]
    category = ul_list.text.strip()
    return category 

#Avis 
def review_page(soup):
    star_soup = soup.find("p", class_="star-rating")
    star_str = str(star_soup)
        
    if "One" in star_str:
        star = "1 star"
    elif "Two" in star_str:
        star = "2 stars"
    elif "Three" in star_str:
        star = "3 stars"
    elif "Four" in star_str:
        star = "4 stars"   
    elif "Five" in star_str:
        star = "5 stars"
    else:
        star = "No star"
    return star

#Image Url
def image_url(soup):
    image_soup = soup.find("div", class_="item active")
    image = image_soup.find("img", src=True)
    url_soup  = image.get("src")
    url = "http://books.toscrape.com" + url_soup[5:]
    return url



# Scraping d'une page spécifique au choix
page_url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page_scrap_list = [page_url]



result = requests.get(page_url)

if result.ok:
    soup = BeautifulSoup(result.content, "html.parser")
 
    page_scrap_list.append(upc_page(soup))
    page_scrap_list.append(title_page(soup))
    page_scrap_list.append(price_inc_tax_page(soup))
    page_scrap_list.append(price_excl_tax_page(soup))
    page_scrap_list.append(available_page(soup))
    page_scrap_list.append(description_page(soup))
    page_scrap_list.append(category_page(soup))
    page_scrap_list.append(review_page(soup))
    page_scrap_list.append(image_url(soup))


# Création du dossier /data 
try:
    os.mkdir("data")
except os.error:
    pass


# Ecriture des données de la liste page_scrap_list dans un dossier csv / avec en tête
with open("data/csv_" + str(title_page(soup)) + ".csv", "w", encoding='utf-8') as f:
    en_tete = ["URL", "UPC", "Title", "Price Tax Inc", "Price Tax Exc", "Available", "Description", "Category", "Review", "Image"]
    dw = csv.DictWriter(f, delimiter=",", fieldnames=en_tete)
    dw.writeheader()
    writer = csv.writer(f, delimiter=",")
    writer.writerow(page_scrap_list)
