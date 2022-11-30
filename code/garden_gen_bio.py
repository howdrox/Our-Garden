import json


def filters(adj_weight, bio):
    new_dict = {}

    for plant in adj_weight.keys():
        if plant in bio:
            new_dict[plant] = adj_weight[plant]

    return new_dict


def update_weight(user_cond, user_weight):
    # Filters the `adj_weight` to only allow plants that are in `bioindicator.json`
    with open("./json/favorisePoids.json", "r") as f:
        adj_weight = json.load(f)
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
                        abs(bio[plant_to][cond] - user_cond[cond]) * user_weight[cond]
                    )
                filtered[plant_from][plant_to] += total_distance

    # Writes new costs in new file
    with open("./json/favoriseBioindicator.json", "w") as f:
        json.dump(filtered, f)


# Has been removed: "echalote", "pasteque", "agrume", "sauge", "ciboulette chinoise"
