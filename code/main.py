import os,json
import garden_gen_bio

ingredients=[]
conditions={}
print('welcome to our garden')

def savoir_demande():
    print('please input les espèces que vous voulez, end with a blank line')
    while(True):
        espece=input()
        if espece=='':
            break
        else:
            ingredients.append(espece)

    print('please input the condition you want')
    print("vous préférez une condition où : ")
    for i in ('lumiere','temperature','humidite','pH','nutriment','texture','organique'):
        conditions[i]=input(i+' : ')
    
    with open("./json/input.json",'w+') as f:
            json.dump({'ingredients':ingredients,'conditions':conditions},f)

if os.path.exists('./json/input.json'):
    print('on a trouvé votre ancien demande, vous voulez le gardez? y/n')
    if input()=='y':
        with open("./json/input.json") as f:
            j=json.load(f)
            ingredients = j['ingredients']
            conditions=j['conditions']
        print('your ancient require is:')
        print(ingredients)
        print(conditions)
    else:
        savoir_demande()
else:
    savoir_demande()


with open("./json/favorisePoids.json") as f:
    favorise = json.load(f)

garden = garden_gen_bio.cheapest_cycle(favorise, ingredients)
print(garden)