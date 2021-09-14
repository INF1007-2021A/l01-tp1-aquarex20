#instructions

"""
Le problème suivant est appelé FizzBuzz. Vous devez compléter la fonction fizzBuzz() qui prend en entrée un nombre n.

Imprimer fizz si n est un multiple de 3
Imprimer buzz s’il s’agit d’un multiple de 5
Imprimer fizzbuzz s’il s’agit à la fois d’un multiple de 3 et 5
Imprimer ledit chiffre autrement.
Il suffit de compléter la fonction fizzBuzz().
"""

def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    if n%3==0 and n%5!=0:
        print("fizz")

    elif n%5==0 and n%3!=0:
        print("buzz")

    elif n%3==0 and n%5==0:
        print("fizzbuzz")

    else:
        print(n)

    resultat = n
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
