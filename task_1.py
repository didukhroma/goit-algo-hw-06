import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
graph = {
    "Market Square": {"Castle Street": 3},
    "Castle Street": {"City Hospital": 2, },
    "City Hospital": {"Bus Station": 4, },
    "Bus Station": {'Rakoczi Street': 3, "Market Square": 5},
    "Rakoczi Street": {"Vasarosnameny Road": 5},
    "Vasarosnameny Road": { "Kisvarda Castle": 6},
    "Kisvarda Castle": { "Market Square": 7}
}
# Bus stops
bus_stops = graph.keys()
G.add_nodes_from(bus_stops)
# Edges
edges = []
for start_pos, end_pos in graph.items():
    for end, time in end_pos.items():
        edges.append((start_pos, end, time))


# # Add weighted edges to the graph
for start_pos, end_pos, time in edges:
    G.add_edge(start_pos, end_pos, weight=time)

# Draw the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightgreen')

# Draw edges
nx.draw_networkx_edges(G, pos, width=2)

# Draw node labels
nx.draw_networkx_labels(G, pos, font_size=10)

# Draw edge labels (driving time)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, label_pos=0.5)
plt.title("Kisvarda Bus Transport Network (with Driving Times)", fontsize=14)
plt.text(0.5, -0.5, f"Quantity of nodes: {nx.number_of_nodes(G)}", ha='center', va='bottom', fontsize=10, color='gray')
plt.text(0.5, -0.6, f"Quantity of edges: {nx.number_of_edges(G)}", ha='center', va='bottom', fontsize=10, color='gray')
plt.axis('off')
plt.show()
