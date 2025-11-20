import heapq  # Librería para manejar colas de prioridad (min-heap)

def dijkstra_step_by_step(graph, source):
    """
    Implementación del algoritmo de Dijkstra con impresión paso a paso.
    graph: diccionario {nodo: [(vecino, peso), ...]}
    source: nodo inicial
    """
    # Inicializamos distancias a infinito y predecesores a None
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0.0  # La distancia al nodo origen es 0

    # Cola de prioridad con tuplas (distancia, nodo)
    pq = [(0.0, source)]
    visited = set()  # Conjunto de nodos ya procesados
    step = 0

    print("=== Simulador Dijkstra (Consola) ===")
    print(f"Origen: {source}\n")

    # Mientras haya nodos en la cola
    while pq:
        step += 1
        d_u, u = heapq.heappop(pq)  # Extraemos el nodo con menor distancia
        if u in visited:
            continue  # Si ya fue visitado, lo saltamos
        visited.add(u)

        print(f"[Paso {step}] Nodo {u} con distancia {d_u}")

        # Recorremos vecinos del nodo actual
        for v, w in graph.get(u, []):
            alt = dist[u] + w  # Calculamos distancia alternativa
            # Si encontramos un camino más corto, actualizamos
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))  # Insertamos en la cola
                print(f"    Relajación: {u} -> {v}, nueva distancia {alt}")

    # Al terminar, devolvemos distancias y predecesores
    return dist, prev

def reconstruct_path(prev, target):
    """
    Reconstruye el camino más corto desde el origen hasta el nodo target.
    prev: diccionario de predecesores
    target: nodo destino
    """
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = prev[curr]
    return list(reversed(path))  # Invertimos para obtener el orden correcto

# Grafo de ejemplo (puede representar una mazmorra o mapa)
graph = {
    "A": [("B", 2), ("C", 5)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 5), ("B", 1), ("D", 2), ("E", 8)],
    "D": [("B", 4), ("C", 2), ("E", 4)],
    "E": [("C", 8), ("D", 4)]
}

# Ejecutamos el simulador desde el nodo A
dist, prev = dijkstra_step_by_step(graph, "A")
print("\nResultado final:")
print("Distancias:", dist)
print("Ruta A -> E:", reconstruct_path(prev, "E"))
