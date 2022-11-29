import json


def filters(adj_weight, bio):
    new_dict = {}

    for plant in adj_weight.keys():
        if plant in bio:
            new_dict[plant] = adj_weight[plant]

    return new_dict


def update_weight(user_cond, user_weight):
    # Filters the `adj_weight` to only allow plants that are in `bioindicator.json`
    with open("./json/bioindicator.json", "r") as f:
        bio = json.load(f)
    filtered = filters(adj_weight, bio)

    # Update cost based on their difference to the user's conditions and weight
    for plant_from in filtered.keys():
        for plant_to in filtered[plant_from].keys():
            if plant_to in bio:
                total_distance = 0
                for cond in bio[plant_from].keys():
                    total_distance += (
                        abs(bio[plant_from][cond] - user_cond[cond]) * user_weight[cond]
                    )
                filtered[plant_from][plant_to] += total_distance

    # Writes new costs in new file
    with open("./json/favoriseBioindicator.json", "w") as f:
        json.dump(filtered, f)


with open("./json/favorisePoids.json", "r") as f:
    adj_weight = json.load(f)


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

update_weight(user_cond, user_weight)


# Has been removed: "echalote", "pasteque", "agrume", "sauge", "ciboulette chinoise"
