import json


def check_ingredients(all_cond, ingredients, user_cond, bio):
    compatible = dict.fromkeys(all_cond, True)

    for cond in all_cond:
        for ing in ingredients:
            if abs(float(bio[ing][cond]) - user_cond[cond]) > 2:
                compatible[cond] = False
                print(f"{ing} not compatible with {cond}")

    return compatible


with open("./json/favorisePoids.json", "r") as f:
    favorise = json.load(f)

with open("./json/bioindicator.json", "r") as b:
    bio = json.load(b)

all_cond = [
    "lumiere",
    "temperature",
    "humidite",
    "pH",
    "nutriment",
    "texture",
    "organique",
]

user_cond = {
    "lumiere": 5.0,
    "temperature": 5.0,
    "humidite": 7.0,
    "pH": 6.0,
    "nutriment": 5.0,
    "texture": 2.0,
    "organique": 6.0,
}

ingredients = [
    "fraisier des bois",
    "framboisier",
    "cerisier",
    "cassis",
]


yes = check_ingredients(all_cond, ingredients, user_cond, bio)
print(yes)
