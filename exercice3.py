#Instructions
"""

Dans cet exercice vous devez convertir un nombre de secondes en nombres d'années, semaines, jours, heures, minute et secondes.
Par exemple, si l'utilisateur entre '633323104' secondes, votre programme devra renvoyé 20 années, 4 semaines, 2 jours,
3 heures, 5 minutes et 4 secondes. Vous pouvez créer d'autres variables pour vous aider.

PS: On considère qu'une année est composée exactement de 365 jours !
"""

def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    années =int(secondes/(3600*24*365))

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines =int(((secondes-années*(3600*24*365))/(7*24*3600)))

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours =int(((secondes-années*(3600*24*365)-semaines*(7*24*3600))/(24*3600)))

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures =int(((secondes-années*(3600*24*365)-semaines*(7*24*3600)-jours*(24*3600))/3600))

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes =int(((secondes-années*(3600*24*365)-semaines*(7*24*3600)-jours*(24*3600)-heures*3600)/60))

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes =(secondes-années*(3600*24*365)-semaines*(7*24*3600)-jours*(24*3600)-heures*3600-minutes*60)

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(années ,semaines ,jours ,heures ,minutes ,secondes)

    return (années ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
