import os, json
import garden_gen
import garden_gen_weight
import garden_gen_bio

ingredients = []
conditions = {}
weight = {}
print("Welcome to our garden")


def savoir_demande():
    print(
        "Please input the species wanted with an `enter` after each of them, then confirm with enter"
    )
    while True:
        espece = input()
        if espece == "":
            break
        else:
            ingredients.append(espece)

    print("Please input your garden conditions")
    for i in (
        "lumiere",
        "temperature",
        "humidite",
        "pH",
        "nutriment",
        "texture",
        "organique",
    ):
        conditions[i] = float(input(i + " : "))

    print("Please input the weight accorded to each condition")
    for i in (
        "lumiere",
        "temperature",
        "humidite",
        "pH",
        "nutriment",
        "texture",
        "organique",
    ):
        weight[i] = float(input(i + " : "))

    with open("./json/input.json", "w+") as f:
        json.dump(
            {"ingredients": ingredients, "conditions": conditions, "weight": weight}, f
        )


if os.path.exists("./json/input.json"):
    print("On a trouvé votre ancien demande, vous voulez la garder? y/n")
    if input() == "y":
        with open("./json/input.json") as f:
            j = json.load(f)
            ingredients = j["ingredients"]
            conditions = j["conditions"]
            weight = j["weight"]
        print("Your ancient query is:")
        print(ingredients)
        print(conditions)
        print(weight)
    else:
        savoir_demande()
else:
    savoir_demande()


with open("./json/favorisePoids.json") as f:
    adj_weight = json.load(f)

with open("./json/favoriseBioindicator.json") as f:
    adj_weight_bio = json.load(f)


garden_v1 = garden_gen.shortest_cycle(adj_weight, ingredients)
print("\nBased on BFS the shortest cycle is: ")
print(garden_v1)
print("The graph of this garden is in `garden_v1.png`\n")


garden_v2 = garden_gen_weight.cheapest_cycle(adj_weight, ingredients)
print(
    "Using the dijkstra algorithm and the standart cost of compost the cheapest cycle is :"
)
print(garden_v2["path"])
print(f"With a total cost of : {garden_v2['cost']}")
garden_gen_weight.mk_diagram(adj_weight, garden_v2, "garden_v2")
print("The graph of this garden is in `garden_v2.png`\n")


garden_gen_bio.update_weight(conditions, weight)
garden_v3 = garden_gen_weight.cheapest_cycle(adj_weight_bio, ingredients)
print(
    "Using the dijkstra algorithm and taking into account the users garden conditions the best cycle is :"
)
print(garden_v3["path"])
print(f"With a total cost of : {garden_v3['cost']}")
garden_gen_weight.mk_diagram(adj_weight_bio, garden_v3, "garden_v3")
print("The graph of this garden is in `garden_v3.png`\n")
