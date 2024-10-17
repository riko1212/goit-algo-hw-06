import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Station A", "Station B", "Station C", 
    "Station D", "Station E", "Station F", 
    "Station G", "Station H", "Station I"
]
G.add_nodes_from(stations)

routes_with_weights = [
    ("Station A", "Station B", 4), 
    ("Station A", "Station C", 2), 
    ("Station B", "Station D", 5), 
    ("Station C", "Station D", 8), 
    ("Station D", "Station E", 6),
    ("Station E", "Station F", 3), 
    ("Station F", "Station G", 7),
    ("Station F", "Station H", 4),
    ("Station G", "Station I", 2),
    ("Station H", "Station I", 1)
]
G.add_weighted_edges_from(routes_with_weights)

def find_all_shortest_paths(graph):
    shortest_paths = {}
    for source in graph.nodes:
        paths = nx.single_source_dijkstra_path(graph, source)
        shortest_paths[source] = paths
    return shortest_paths

shortest_paths = find_all_shortest_paths(G)

print("Найкоротші шляхи між всіма вершинами графа:")
for start, paths in shortest_paths.items():
    for end, path in paths.items():
        print(f"Шлях від {start} до {end}: {' -> '.join(path)}")

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graph with Weights")
plt.show()
