"""
Completer la fonction pointDeRencontre() qui calcule la position du point de rencontre entre deux véhicules se
déplaçant l’un vers l’autre à une vitesse respective de v1 et v2 et se trouvant à une distance d.
Considérez que le véhicule 1 se trouve initialement au point 0 et que les vitesses sont constantes.

Si par exemple le véhicule 1 se déplace à une vitesse de 2 unités de distance par unité de temps,
 que le véhicule 2 se déplace à une vitesse de 1 unité de distance par une unité de temps et que les deux véhicules se
  trouvent à 12 unités de distance, ils se rencontreront au point situé à 8 unités de distance de la position initiale
  du véhicule 1.

Il suffit de compléter la fonction pointDeRencontre().
"""

def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    # d-v1*t=v2*t
    #d=t(v1+v2)
    #t=d/(v1+v2) le temps de rencontre



    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = v1*distance/(v1+v2)

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
