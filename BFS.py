from collections import deque

def bfs(grafo, inicio, meta):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
            visitados.add(nodo)

    return None

# Grafo de ejemplo
grafo_bfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

camino_bfs = bfs(grafo_bfs, 'A', 'F')
print("\nCamino BFS de A a F:", camino_bfs)
