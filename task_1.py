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

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_weight='bold', edge_color='gray')
plt.title("Transport Network Graph")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for station, deg in degree.items():
    print(f"{station}: {deg}")
