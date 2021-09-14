import math
"""
Dans cet exercice, vous devez calculer la position d'une voiture à un temps t. Votre fonction prend en entrée:

positionInitiale (en m)
vistesseInitiale (en km/h)
duree* (en secondes)
vitesseFinale (km/h) qui est la vitesse du vehicule apres t secondes.
Finalement vous devez calculer la position finale en mètre. Les équations du MRUA, 
tirées d'alloprof, pourrons certainement vous aider:

"""

def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    a=(vitesseFinale-vitesseInitiale)/duree


    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = positionInitiale+((vitesseInitiale+vitesseFinale)*duree/3.600)/2

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesseFinale en km/h: "))
    print(calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale))
