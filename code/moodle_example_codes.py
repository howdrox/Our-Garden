# These are functions copied from https://moodle.insa-lyon.fr/pluginfile.php/345540/mod_resource/content/1/SUJET%20-%20Etude%20InSavour%20-%20Interactions%20Savoureuses%20-%20v02.8.html

import csv

with open("./csv/data_arcs.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")

    adjacents = {}  

    for ligne in reader:
        source, interaction, cible = ligne
        if interaction == "favorise":
            if source not in adjacents: 
                adjacents[source] = [cible]  
                adjacents[source].append(cible)

    print(adjacents)


def existe_chemin_BFS(adjacents, depart, arrivee):
    a_explorer = [depart]
    deja_collectes = [depart]

    while len(a_explorer) != 0:
        courant = a_explorer.pop(0)

        if courant == arrivee:
            return True

        if courant in adjacents:
            for sommet in adjacents[courant]:
                if sommet not in deja_collectes:
                    a_explorer.append(sommet)
                    deja_collectes.append(sommet)

    return False


def calcul_chemin_BFS(adjacents, depart, arrivee):
    a_explorer = [depart]
    deja_collectes = [depart]
    chemins = {depart: [depart]}

    while len(a_explorer) != 0:
        courant = a_explorer.pop(0)

        if courant == arrivee:
            return chemins[arrivee]

        if courant in adjacents:
            for sommet in adjacents[courant]:
                if sommet not in deja_collectes:
                    a_explorer.append(sommet)
                    deja_collectes.append(sommet)
                    chemins[sommet] = chemins[courant] + [sommet]

    return None
