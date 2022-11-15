import csv,json

def genFavorise():
    favorise={}
    with open("./csv/data_arcs_poids.csv") as arcs:
        reader=csv.reader(arcs,delimiter=';')
        for source, interaction, cible, poids in reader:
            if interaction=='favorise':
                if source in favorise: 
                    favorise[source][cible] = int(poids)
                else:
                    favorise[source] = {cible:int(poids)}

    with open('./json/favorise.json','w+') as f:
        json.dump(favorise,f)

def genIndicator():
    indicator={}
    with open("./csv/data_sommets_bioindicateurs.csv") as f:
        reader=csv.reader(f,delimiter=';')
        for espece,lumiere,temperature,humidite,pH,nutriment,texture,organique in reader:
            indicator[espece]={
                'lumiere':lumiere,
                'temperature':temperature,
                'humidite':humidite,
                'pH':pH,
                'nutriment':nutriment,
                'texture':texture,
                'organique':organique
            }

    with open('./json/indicator.json','w+') as f:
        json.dump(indicator,f)

genIndicator()