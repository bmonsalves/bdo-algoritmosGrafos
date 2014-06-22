import sys
def dijkstra(grafo,inicio,fin,visitado=[],distancias={},anteriores={}):

    # ENCUENTRA LA RUTA MAS CORTA ENTRE ELNODO INICIAL Y FINAL
    # luego de hacer el recorrido si llega al nodo final retorna la ruta
    if inicio==fin:
        ruta=[]

        while fin != None:
            ruta.append(fin)
            fin=anteriores.get(fin,None)
        return distancias[inicio], ruta[::-1]

    # Detectar si es la primera vez que pasa, establece la distancia actual como 0
    if not visitado: 
        distancias[inicio]=0

    #procesa los vecinos del nodo, seguimiento de los predecesores
    for vecino in grafo[inicio]:

        if vecino not in visitado:
            vecinodist = distancias.get(vecino,sys.maxint)
            tentativedist = distancias[inicio] + grafo[inicio][vecino]

            if tentativedist < vecinodist:
                distancias[vecino] = tentativedist
                anteriores[vecino]=inicio

    # vecinos procesados, ahora marcan el nodo actual como visitado
    visitado.append(inicio)

    # encuentra el nodo no visitado mas cercano al inicio
    noVisitados = dict((k, distancias.get(k,sys.maxint)) for k in grafo if k not in visitado)
    nodoCercano = min(noVisitados, key=noVisitados.get)

    # envia el nodo siguiente para continuar con el recorrido
    return dijkstra(grafo,nodoCercano,fin,visitado,distancias,anteriores)


grafo = {
        'A': {'B': 7, 'D': 5},
        'B': {'A': 7, 'C': 8},
        'C': {'B': 8, 'E': 5},
        'D': {'A': 5, 'B': 9, 'E': 15, 'F' : 6},
        'E': {'C': 5, 'B': 7, 'D': 15, 'F': 8, 'G' : 9},
        'F': {'D': 6, 'E': 8, 'G': 11},
        'G': {'F': 11, 'E': 9}
        }
print "recorrido minimo: ",dijkstra(grafo,'C','F')