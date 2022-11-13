import csv,json


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

