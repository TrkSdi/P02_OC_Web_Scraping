import requests
from bs4 import BeautifulSoup
import csv
from scrap_part_1 import upc_page,  title_page, price_inc_tax_page, price_excl_tax_page, available_page, description_page, category_page, review_page, image_url
import os


def scrap_category(base_url):

    i = 1
    category_url = base_url + "index.html"
    all_article_category = []



    reponse = requests.get(category_url)

    while reponse.ok:

        # je parse et je liste tous les urls sur toutes les pages d'une catégorie
        url_list = []
        doc = BeautifulSoup(reponse.content, "html.parser")
        doc_article = doc.findAll("article")
        for a_doc in doc_article:
            a = a_doc.find("a")
            url = a["href"][8:]
            url_list.append("http://books.toscrape.com/catalogue" + url)
            
        
        # je cherche les infos requises dans chaque url de url_list
        for link in url_list:
            row_list = []
            result = requests.get(link)
            soup = BeautifulSoup(result.content, 'html.parser')
            
            row_list.append(link)
            row_list.append(upc_page(soup))
            row_list.append(title_page(soup))
            row_list.append(price_inc_tax_page(soup))
            row_list.append(price_excl_tax_page(soup))
            row_list.append(available_page(soup))
            row_list.append(description_page(soup))
            row_list.append(category_page(soup))
            row_list.append(review_page(soup))
            row_list.append(image_url(soup))
            
            
            all_article_category.append(row_list)
            
            
        # j'alimente la condition while afin que je puisse chercher les url de toutes les pages d'une catégorie
        i += 1
        category_url = base_url + "page-" + str(i) + ".html"
        reponse = requests.get(category_url)
        
        
    with open("data/csv_" + str.lower(category_page(soup)) + ".csv", "w", encoding='utf-8') as f:
        #en tete
        en_tete = ["URL", "UPC", "Title", "Price Tax Inc", "Price Tax Exc", "Available", "Description", "Category", "Review", "Image"]
        dw = csv.DictWriter(f, delimiter=",", fieldnames=en_tete)
        dw.writeheader()
        writer = csv.writer(f, delimiter=",")
        for row in all_article_category:
            writer.writerow(row)

# création ou vérification de fichier 
try:
    os.mkdir("data")
except os.error:
    pass


scrap_category("http://books.toscrape.com/catalogue/category/books/sequential-art_5/")

  