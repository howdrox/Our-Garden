import json
import itertools


def check_ingredients(usefull_cond, ingredients, user_cond, bio):
    compatible = dict.fromkeys(usefull_cond, True)

    for cond in usefull_cond:
        for ing in ingredients:
            if abs(float(bio[ing][cond]) - user_cond[cond]) > 2:
                compatible[cond] = False
                # print(f"{ing} not compatible with {cond}")

    result = True
    for i in compatible.keys():
        if not compatible[i]:
            result = False

    return result


def possible_ingredients(all_list, user_cond, bio, usefull_cond):
    perm = list(itertools.combinations(all_list, 4))
    possible = []

    for i in perm:
        if check_ingredients(usefull_cond, i, user_cond, bio):
            possible.append(list(i))

    return possible


with open("./json/favorisePoids.json", "r") as f:
    favorise = json.load(f)

with open("./json/bioindicator.json", "r") as b:
    bio = json.load(b)

with open("./json/possibleIngredientsPerCategory.json", "r") as a:
    all_dict = json.load(a)
    all_list = []
    for i in all_dict.keys():
        if i != "fleur":
            all_list += all_dict[i]

all_cond = [
    "lumiere",
    "temperature",
    "humidite",
    "pH",
    "nutriment",
    "texture",
    "organique",
]

usefull_cond = [
    "lumiere",
    "temperature",
    "humidite",
    "pH",
    "texture",
]

user_cond = {
    "lumiere": 6.0,
    "temperature": 5.0,
    "humidite": 6.0,
    "pH": 6.0,
    "nutriment": 5.0,
    "texture": 2.0,
    "organique": 6.0,
}

weight = {
    "lumiere": 8.0,
    "temperature": 6.0,
    "humidite": 6.0,
    "pH": 4.0,
    "texture": 1.0,
}

ingredients = [
    "mache",
    "framboisier",
    "cerisier",
    "cassis",
]


possible_list = possible_ingredients(all_list, user_cond, bio, usefull_cond)
print(len(possible_list))

# Has been removed: "echalote", "pasteque", "agrume", "sauge", "ciboulette chinoise"
