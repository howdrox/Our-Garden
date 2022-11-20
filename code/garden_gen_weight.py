import json
import itertools
import os


def dijkstra(adj, root, final):
    # Error checking
    if root not in adj or final not in adj:
        print("Invalid nodes")
        return {}

    haveExplored = []
    paths = {}
    unexplored = list(adj.keys())

    # sets all cost to infinity
    for key in adj.keys():
        paths[key] = {"cost": float("inf"), "path": [key]}
    paths[root]["cost"] = 0

    while len(haveExplored) < len(adj):
        # finds minimum
        found = False
        i = 0
        while not found:
            if unexplored[i] not in haveExplored and i < len(unexplored):
                min_node = unexplored[i]
                min_cost = paths[unexplored[i]]["cost"]
                found = True
            i += 1

        for node in unexplored:
            if paths[node]["cost"] < min_cost:
                min_cost = paths[node]["cost"]
                min_node = node

        # updates cost of nodes connected to minimum
        for node in adj[min_node]:
            if node in adj and node not in haveExplored:
                oldCost = paths[node]["cost"]
                newCost = paths[min_node]["cost"] + adj[min_node][node]
                if newCost < oldCost:
                    paths[node]["cost"] = newCost
                    paths[node]["path"] = paths[min_node]["path"] + [node]

        haveExplored.append(min_node)
        unexplored.remove(min_node)

    return paths[final]


def cycle(adj, ingredients):
    "Returns the cycle that goes through each `ingredients` in order"

    if len(ingredients) < 2:
        print("Not enough ingredients")
        return []

    result = {"path": [], "cost": 0}

    i = 0
    while i < len(ingredients):
        if i == len(ingredients) - 1:
            path = dijkstra(adj, ingredients[-1], ingredients[0])
        else:
            path = dijkstra(adj, ingredients[i], ingredients[i + 1])

        if i == 0:
            result["path"] += path["path"]
            result["cost"] += path["cost"]
        else:
            result["path"] += path["path"][
                1:
            ]  # [1:] to prevent the same ingredient from being mentioned twice
            result["cost"] += path["cost"]

        i += 1

    return result


def cheapest_cycle(adj, ingredients):
    "Returns the shortest cycle that goes through each `ingredients` by checking for all possible permutations"
    all_perm = list(itertools.permutations(ingredients, len(ingredients)))

    cheapest_cycle = cycle(adj, all_perm[0])
    min_cost = cycle(adj, all_perm[0])["cost"]
    for i in range(1, len(all_perm)):
        cost = cycle(adj, all_perm[i])["cost"]
        if cost < min_cost:
            min_cost = cost
            cheapest_cycle = cycle(adj, all_perm[i])

    return cheapest_cycle


def mk_diagram(adj, path):
    cycle = path["path"]
    cost = path["cost"]
    result = "digraph {\n"

    i = 0
    while i < len(cycle) - 1:
        result += (
            f'"{cycle[i]}" -> "{cycle[i + 1]}" [label={adj[cycle[i]][cycle[i + 1]]}]\n'
        )
        i += 1
    result += f'label="total cost: {cost}"\n'
    result += "}"

    with open("output_weighted.dot", "w") as f:
        f.write(result)

    os.system("dot -Tpng -o output_weighted.png output_weighted.dot")


# Main function
with open("./json/favorisePoids.json") as f:
    favorise = json.load(f)

ingredients = ["fraisier des bois", "framboisier", "cerisier", "cassis"]
garden = cheapest_cycle(favorise, ingredients)
print(garden)
mk_diagram(favorise, garden)
