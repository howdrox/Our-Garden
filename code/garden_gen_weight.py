import json


def dijkstra(adj, root, final):
    toExplore = [root]
    alreadyExplored = [root]
    costs = {}

    # sets all cost to infinity
    for key in adj.keys():
        costs[key] = float("inf")
    costs[root] = 0

    print(costs)

    while len(toExplore) != 0:
        current = toExplore.pop(0)

        if current in adj:
            for node in adj[current]:
                # if node not in alreadyExplored:
                toExplore.append(node)
                alreadyExplored.append(node)
                oldCost = costs[node]
                newCost = costs[current] + adj[current][node]
                print(oldCost)
                print(newCost)
                if newCost < oldCost:
                    costs[node] = newCost

    return costs[final]


with open("./json/favorise_poids.json") as f:
    favorise = json.load(f)

ingredients = ["pomme", "poirier commun"]
minCost = dijkstra(favorise, ingredients[0], ingredients[1])
print(minCost)
