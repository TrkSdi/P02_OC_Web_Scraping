
# Projet 02 - Scrap de site Booktoscrap.com

## Création de l'environnement 

Dans Terminal, on exécuté la ligne de code suivante : 

‘python -m venv nomenvironnement‘

## Activation de l'environnement 

Dans Terminal : 

“souce nomenvironnement/bin/activate“

## Script 

### 1) Scrap 




Pour la création de l'environnement j'ai suivi le cours sur l'environnement virtuel, dans ce sens j'ai créer un environnement avec la ligne de code :

python -m venv <nomenvironnement>

Par la suite j'ai procédé à l'activation de cet environnement

source <nomenvironnement>/bin/activate

Par la suite, j'ai crée quatre scripts distincts concernant chacune des étapes demandées.

Dans le scrap_part_1, j'ai crée des fonctions qui vont chercher un à un les éléments demandés et sont, par la suite, rajouté à une liste. 
Après cela un fichier csv est crée reprenant les éléments. 

Dans scrap_part_2, j'ai cherché les urls de toutes les pages d'une catégorie. J'ai ensuite importé les fonctions de scrap_part_1 pour les appliquer à chacune des pages d'une catégorie.

Dans scrap_part_3, j'ai cherché les urls de toutes les pages de toutes les catégorie. J'ai ensuite importé la fonction de scrap_part_2 pour les appliquer à chacune des pages de toutes les catégories du site.

Enfin dans scrap_part_4, j'ai isolé et ajouté à une liste les urls des images ainsi que leur titre, de tous les articles présents sur le site. Par la suite, j'ai procédé à leur téléchargement

 
 
 
 