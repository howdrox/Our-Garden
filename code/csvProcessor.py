import csv, json


def genFavorise():
    favorise = {}
    with open("./csv/data_arcs_poids.csv") as arcs:
        reader = csv.reader(arcs, delimiter=";")
        for source, interaction, cible, poids in reader:
            if interaction == "favorise":
                if source in favorise:
                    favorise[source][cible] = int(poids)
                else:
                    favorise[source] = {cible: int(poids)}

    with open("./json/favorise.json", "w+") as f:
        json.dump(favorise, f)


def genIndicator():
    indicator = {}
    with open("./csv/data_sommets_bioindicateurs.csv") as f:
        reader = csv.reader(f, delimiter=";")
        for (
            espece,
            lumiere,
            temperature,
            humidite,
            pH,
            nutriment,
            texture,
            organique,
        ) in reader:
            indicator[espece] = {
                "lumiere": float(lumiere),
                "temperature": float(temperature),
                "humidite": float(humidite),
                "pH": float(pH),
                "nutriment": float(nutriment),
                "texture": float(texture),
                "organique": float(organique),
            }

    with open("./json/indicator.json", "w+") as f:
        json.dump(indicator, f)


def genCategory():
    category = {}
    with open("./csv/data_sommets_categories.csv") as f:
        reader = csv.reader(f, delimiter=";")
        for source, catégorie in reader:
            if catégorie in category:
                category[catégorie].append(source)
            else:
                category[catégorie] = [
                    source,
                ]

    with open("./json/category.json", "w+") as f:
        json.dump(category, f)


def genIngredient():
    ingredient = [
        "genet",
        "topinambour",
        "pissenlit",
        "cassis",
        "lin",
        "carotte sauvage",
        "cumin",
        "cerfeuil commun",
        "melisse citronnelle",
        "groseillier",
        "sauge",
        "moutarde",
        "morelle de balbis",
        "ciboulette chinoise",
        "anis",
        "panais",
        "courgette",
        "cornichon",
        "bourrache officinale",
        "sarriette",
        "feve",
        "melon",
        "tournesol",
        "echalote",
        "thym",
        "romarin",
        "achillee millefeuille",
        "prunier",
        "framboisier",
        "cerisier",
        "rue fetide",
        "navet",
        "roquette",
        "chicoree",
        "epinard",
        "artichaut",
        "persil",
        "agrume",
        "lavande",
        "rosier",
        "tanaisie commune",
        "courge",
        "origan",
        "vigne",
        "poirier commun",
        "trefle blanc",
        "mache",
        "potiron",
        "mais",
        "haricot",
        "pasteque",
        "cosmos",
        "tomate",
        "basilic",
        "fenouil",
        "celeri",
        "betterave",
        "coriandre",
        "pois",
        "camomille allemande",
        "kiwi",
        "pomme de terre",
        "asperge",
        "concombre",
        "aneth",
        "chou",
        "laitue",
        "oignon",
        "fraisier des bois",
        "souci",
        "phacelie",
        "pommier",
        "ciboulette",
        "pecher",
        "ail",
        "carotte",
        "poireau",
        "cresson",
        "radis",
    ]
    with open("./json/ingredient.json", "w+") as f:
        json.dump(ingredient, f)


def change_float(bio):
    new_dict = {}
    for plant in bio.keys():
        new_dict[plant] = {}
        for cond in bio[plant].keys():
            new_dict[plant][cond] = float(bio[plant][cond])

    with open("./json/indicator.json", "w") as test:
        json.dump(new_dict, test)


genIndicator()
