from collections import deque

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


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
        
    if not queue:
        return
    
    vertex = queue.popleft()
    
    if vertex not in visited:
        print(vertex,end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
        
    bfs_recursive(graph, queue, visited)


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    
    print(vertex, end=' ')  
    for neighbor in graph[vertex].keys():
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

bfs_recursive(test_graph, deque(["Market Square"]))
print("\n")
dfs_recursive(test_graph, "Market Square")