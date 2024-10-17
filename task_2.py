import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Station A", "Station B", "Station C", 
    "Station D", "Station E", "Station F", 
    "Station G", "Station H", "Station I"
]
G.add_nodes_from(stations)

routes = [
    ("Station A", "Station B"), 
    ("Station A", "Station C"), 
    ("Station B", "Station D"), 
    ("Station C", "Station D"), 
    ("Station D", "Station E"),
    ("Station E", "Station F"), 
    ("Station F", "Station G"),
    ("Station F", "Station H"),
    ("Station G", "Station I"),
    ("Station H", "Station I")
]
G.add_edges_from(routes)

def find_paths(graph, start, end):
    try:
        dfs_path = list(nx.dfs_edges(graph, source=start))
        dfs_path_nodes = [start] + [edge[1] for edge in dfs_path]

        bfs_path = list(nx.bfs_edges(graph, source=start))
        bfs_path_nodes = [start] + [edge[1] for edge in bfs_path]

        shortest_path = nx.shortest_path(graph, source=start, target=end)

        return dfs_path_nodes, bfs_path_nodes, shortest_path
    except nx.NetworkXNoPath:
        return None, None, None

dfs_result, bfs_result, shortest_path = find_paths(G, "Station A", "Station I")

print("Шлях за допомогою DFS:", " -> ".join(dfs_result))
print("Шлях за допомогою BFS:", " -> ".join(bfs_result))
print("Найкоротший шлях:", " -> ".join(shortest_path))

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

dfs_edges = list(zip(dfs_result[:-1], dfs_result[1:]))
bfs_edges = list(zip(bfs_result[:-1], bfs_result[1:]))
shortest_edges = list(zip(shortest_path[:-1], shortest_path[1:]))

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold', edge_color='gray')
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='blue', width=2, label="DFS Path")
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='green', width=2, style="dashed", label="BFS Path")
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='red', width=2, label="Shortest Path")

plt.title("Comparison of DFS and BFS Paths")
plt.legend(loc="upper left")
plt.show()
