import requests
from bs4 import BeautifulSoup
import os
import urllib.request


def dl_img(url, file_path, file_name):

    with open(f'{file_path}/{file_name}', 'wb+') as file:
        file.write(
            urllib.request.urlopen(url).read()
                   )
    


general_url = "http://books.toscrape.com/catalogue/page-1.html"
url_img_list = []
title_element = []


i = 1
result = requests.get(general_url)

while result.ok:
    soup = BeautifulSoup(result.content, "html.parser")
    img_soup = soup.findAll("img", src=True )
    for img in img_soup:
        img_url =  "http://books.toscrape.com/" + img["src"][2:]
        url_img_list.append(img_url)
    for element in img_soup:
        title = element["alt"]
        title_filtred = title.replace("/", "-")
        title_element.append(title_filtred)
        
    

    i += 1
    general_url = "http://books.toscrape.com/catalogue/page-" + str(i) + ".html"
    result = requests.get(general_url)




try:
    os.mkdir("Image")
except os.error:
    pass


for url, title in zip(url_img_list, title_element):
    dl_img(url, "Image", title)
    
