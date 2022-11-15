import json


def dijkstra(adj, root, final):
    # Error checking
    if root not in adj or final not in adj:
        print("Invalid nodes")
        return []

    toExplore = [root]
    costs = {}

    # sets all cost to infinity
    for key in adj.keys():
        costs[key] = float("inf")
    costs[root] = 0

    print(costs)

    while len(toExplore) != 0:
        current = toExplore.pop(0)
        for node in adj[current]:
            toExplore.append(node)
            oldCost = costs[node]
            newCost = costs[current] + adj[current][node]
            print(oldCost)
            print(newCost)
            if newCost < oldCost:
                costs[node] = newCost

    return costs[final]


with open("./json/favorisePoids.json") as f:
    favorise = json.load(f)

ingredients = ["pommier", "poirier commun"]
minCost = dijkstra(favorise, ingredients[0], ingredients[1])
print(minCost)
