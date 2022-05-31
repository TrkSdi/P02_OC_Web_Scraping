import requests
from bs4 import BeautifulSoup
from scrap_part_2 import scrap_category
import os


 
general_url = "http://books.toscrape.com/index.html"
reponse = requests.get(general_url)
category_main_url = []

if reponse.ok:
    soup = BeautifulSoup(reponse.content, "html.parser")
    div_soup = soup.findAll("div", class_="side_categories")
    for ul_soup in div_soup:
        ul = ul_soup.find("ul", class_=False)
        a = ul.findAll("a")
        for url in a:
            urls = url["href"]
            categories_url = "http://books.toscrape.com/" + urls[:-10]
            category_main_url.append(categories_url)

try:
    os.mkdir("data")
except os.error:
    pass

for link in category_main_url: 
    scrap_category(link)

