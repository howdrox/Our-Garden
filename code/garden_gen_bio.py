import json


def filters(adj_weight, bio):
    new_dict = {}

    for plant in adj_weight.keys():
        if plant in bio:
            new_dict[plant] = adj_weight[plant]

    return new_dict


def update_weight(adj_weight, bio, user_cond, user_weight):
    # Update cost based on the difference in conditions of the two plants and on the user's conditions and weight
    for plant_from in adj_weight.keys():
        for plant_to in adj_weight[plant_from].keys():
            if plant_to in bio:
                total_distance = 0
                for cond in bio[plant_from].keys():
                    # Cost from difference in conditions of the two plants
                    total_distance += (
                        abs(bio[plant_from][cond] - bio[plant_to][cond]) / 2
                    )
                    # Cost from the difference to the users conditions
                    total_distance += (
                        abs(bio[plant_from][cond] - user_cond[cond])
                        * user_weight[cond]
                        / 4
                    )
                adj_weight[plant_from][plant_to] += total_distance

    # Writes new costs in new file
    with open("./json/favoriseBioindicator.json", "w") as new:
        json.dump(adj_weight, new)


with open("./json/favorisePoids.json", "r") as f:
    adj_weight = json.load(f)

with open("./json/bioindicator.json", "r") as b:
    bio = json.load(b)


user_cond = {
    "lumiere": 6.0,
    "temperature": 5.0,
    "humidite": 6.0,
    "pH": 6.0,
    "nutriment": 5.0,
    "texture": 2.0,
    "organique": 6.0,
}

user_weight = {
    "lumiere": 8.0,
    "temperature": 6.0,
    "humidite": 6.0,
    "pH": 4.0,
    "nutriment": 1.0,
    "texture": 1.0,
    "organique": 1.0,
}

ingredients = [
    "mache",
    "framboisier",
    "cerisier",
    "cassis",
]


filtered_adj_weight = filters(adj_weight, bio)
update_weight(filtered_adj_weight, bio, user_cond, user_weight)


# Has been removed: "echalote", "pasteque", "agrume", "sauge", "ciboulette chinoise"
