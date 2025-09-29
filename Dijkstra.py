import heapq

def dijkstra(grafo, inicio):
    # Inicializar distancias
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Cola de prioridad
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

# Grafo de ejemplo
grafo_dijkstra = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 6, 'D': 1},
    'C': {'A': 5, 'B': 6, 'D': 2, 'E': 5},
    'D': {'B': 1, 'C': 2, 'E': 1},
    'E': {'C': 5, 'D': 1}
}

resultado_dijkstra = dijkstra(grafo_dijkstra, 'A')
print("Distancias mínimas desde A (Dijkstra):")
for nodo, distancia in resultado_dijkstra.items():
    print(f"A → {nodo}: {distancia}")
