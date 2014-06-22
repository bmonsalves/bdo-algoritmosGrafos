parent = dict()
rango = dict()

#BUSCAR ARBOL MINIMO 

def make_set(nodo):
    parent[nodo] = nodo
    rango[nodo] = 0

def find(nodo):
    if parent[nodo] != nodo:
        parent[nodo] = find(parent[nodo])
    return parent[nodo]

def union(nodo1, nodo2):
    root1 = find(nodo1)
    root2 = find(nodo2)
    if root1 != root2:
        if rango[root1] > rango[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rango[root1] == rango[root2]: rango[root2] += 1

def kruskal(grafo):
    for nodo in grafo['nodos']:
        make_set(nodo)

    arbol_minimo = list()
    aristas = list(grafo['aristas'])
    aristas.sort()
    for arista in aristas:
        weight, nodo1, nodo2 = arista
        if find(nodo1) != find(nodo2):
            union(nodo1, nodo2)
            arbol_minimo.append(arista)
    return arbol_minimo

#diccionario
grafo = {
        'nodos': ['A', 'B', 'C', 'D', 'E', 'F','G'],
        'aristas': [
            (7,'A', 'B'), (5,'A', 'D'),
            (8,'B', 'C'), (9,'B', 'D'), (7,'B', 'E'),
            (5,'C', 'E'),
            (15,'D', 'E'), (6,'D', 'F'),
            (8,'E', 'F'), (9,'E', 'G'),
            (11,'F', 'G')
            ]
        }


print "kruskal: ", kruskal(grafo)


