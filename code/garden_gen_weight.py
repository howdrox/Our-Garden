import json


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
                print(min_cost)
                print(min_node)

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


def mk_diagram():
    """digraph {
      root -> a
      root -> b [weight=2]
      root -> c [weight=3]
    }"""


# Main function:
with open("./json/favorisePoids.json") as f:
    favorise = json.load(f)

ingredients = ["pommier", "haricot"]
minCost = dijkstra(favorise, ingredients[1], ingredients[0])
print(minCost)
