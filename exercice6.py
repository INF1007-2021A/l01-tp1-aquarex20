"""
Dans cet exercice, vous manipulerez les nombres complexes.
Vous devez compléter deux fonctions, la fonction trouverModule() qui retourne le module d'un nombre complexe
et la fonction effectuerRotation() qui effectue une rotation du nombre selon un angle saisi par l'utilisateur.
Pour rappel, pour effectuer une rotation d'un angle , il suffit de multiplier le nombre complexe par  + .
Voici les deux fonctions à compléter :

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np



def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):
    # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
    module =sqrt(nombreComplexe.real**2+nombreComplexe.imag**2)

    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)
    print("Le module du nombre complexe est", int(module*1000)/1000, ". \nTandis que son angle est ",int(angle*1000)/1000)

    # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'

    resultat = nombreComplexe*(cos(radians(angle_rotation))+sin(radians(angle_rotation))*1j)

    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)
    print("Le nouveau module du nombre complexe est", int(nouveauModule*1000)/1000, "." 
        "\nTandis que son nouvel angle est ",int(nouvelAngle*1000)/1000)

    return resultat


def dessiner(number, label):
    if number != None:
        plt.polar([0, radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
