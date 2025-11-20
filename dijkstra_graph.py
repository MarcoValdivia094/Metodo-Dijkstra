import networkx as nx
import matplotlib.pyplot as plt

def plot_graph_with_path(graph_dict, path):
    """
    Dibuja el grafo y resalta el camino más corto.
    graph_dict: diccionario con nodos y aristas
    path: lista de nodos que forman el camino más corto
    """
    G = nx.Graph()
    # Añadimos aristas con pesos
    for u, edges in graph_dict.items():
        for v, w in edges:
            G.add_edge(u, v, weight=w)

    # Posiciones de los nodos (layout automático)
    pos = nx.spring_layout(G, seed=42)

    # Dibujamos nodos y etiquetas
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color="#87CEFA", node_size=900, font_weight="bold")

    # Dibujamos pesos de las aristas
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    # Resaltamos el camino más corto en rojo
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color="red")

    plt.title("Camino más corto resaltado (Dijkstra)")
    plt.show()

# Usamos el mismo grafo y reconstruimos el camino A -> E
path = reconstruct_path(prev, "E")
plot_graph_with_path(graph, path)
