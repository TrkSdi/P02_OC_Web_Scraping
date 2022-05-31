import requests
from bs4 import BeautifulSoup
import os
import urllib.request


# fonction qui permet de télécharger et de nommer les images
def dl_img(url, file_path, file_name):

    with open(f'{file_path}/{file_name}', 'wb+') as file:
        file.write(
            urllib.request.urlopen(url).read()
                   )
    


general_url = "http://books.toscrape.com/catalogue/page-1.html"
elements = []


i = 1
result = requests.get(general_url)

while result.ok:
    soup = BeautifulSoup(result.content, "html.parser")
    # Isoler les urls des images ainsi que les titres puis les rajouter dans la liste elements
    img_soup = soup.findAll("img", src=True )
    for element in img_soup:
        img_url =  "http://books.toscrape.com/" + element["src"][2:]
        title = element["alt"]
        title_filtred = title.replace("/", "-")
        elements.append({"img": img_url, "title" : title_filtred })
        
        
    

    i += 1
    general_url = "http://books.toscrape.com/catalogue/page-" + str(i) + ".html"
    result = requests.get(general_url)


try:
    os.mkdir("Image")
except os.error:
    pass

# execution de la fonction
for element in elements:
    dl_img(element["img"], "Image", element["title"] + ".jpg")
    
