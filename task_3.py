test_graph = {
    "Market Square": {
        "Castle Street": 3,
        "Bus Station": 5,
        "Kisvarda Castle": 7
    },
    "Castle Street": {
        "City Hospital": 2,
        "Market Square": 3,
        "Rakoczi Street": 4  
    },
    "City Hospital": {
        "Bus Station": 4,
        "Vasarosnameny Road": 6  
    },
    "Bus Station": {
        "Rakoczi Street": 3,
        "Market Square": 5,
        "City Hospital": 4
    },
    "Rakoczi Street": {
        "Vasarosnameny Road": 5,
        "Castle Street": 4,
        "Bus Station": 3  
    },
    "Vasarosnameny Road": {
        "Kisvarda Castle": 6,
        "City Hospital": 6  
    },
    "Kisvarda Castle": {
        "Market Square": 7,
        "Vasarosnameny Road": 6  
    }
}

def dijkstra (graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float('inf'):
            break

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_node)
        unvisited.remove(current_node)

    return distances

print(dijkstra(test_graph, "Bus Station"))