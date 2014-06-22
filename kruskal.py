#lista de pares key/value
padre = dict()
costos = dict()

#BUSCAR ARBOL MINIMO 

#crea listas key/value con los nodos y asigna costos
def armar_serie(nodo):
    padre[nodo] = nodo
    costos[nodo] = 0

#busca el nodo padre del ingresado y lo retorna
def buscar(nodo):
    if padre[nodo] != nodo:
        padre[nodo] = buscar(padre[nodo])
    return padre[nodo]

#toma la desicion de tomar los nodos con la menor arista
def unir(nodo1, nodo2):
    
    #toma la raiz de cada nodo
    raiz1 = buscar(nodo1)
    raiz2 = buscar(nodo2)
    #corrobora que el padre de los nodos sea distinto para no crear ciclos
    if raiz1 != raiz2:
        #Comprueba que el costo que almacena la llave costos[raiz1] sea mayor
        #de serlo, se almacena raiz1 en la llave padre[raiz2]
        if costos[raiz1] > costos[raiz2]:

            #asigna un nodo el nodo de destino a la tupla 
            #si raiz1 == A y raiz2 == C se almacena en la lista padre el valor "C:A"
            padre[raiz2] = raiz1

        else:
            padre[raiz1] = raiz2

            if costos[raiz1] == costos[raiz2]: 
                costos[raiz2] += 1


def kruskal(grafo):
    for nodo in grafo['nodos']:
        armar_serie(nodo)

    arbol_minimo = list()
    #transforma las aristas en listas
    aristas = list(grafo['aristas'])
    #ordena las aristas de menos a mayor
    aristas.sort()

    #recorre las aristas ordenadas
    for arista in aristas:
        costo, nodo1, nodo2 = arista

        if buscar(nodo1) != buscar(nodo2):
            unir(nodo1, nodo2)
            #agrega la arista a la lista
            arbol_minimo.append(arista)
    return arbol_minimo

#diccionario
grafo = {
        'nodos': ['A','B','C','D','E','F','G'],
        'aristas': [
            (7,'A','B'),(5,'A','D'),
            (8,'B','C'),(9,'B','D'), (7,'B','E'),
            (5,'C','E'),
            (15,'D','E'),(6,'D','F'),
            (8,'E','F'),(9,'E','G'),
            (11,'F','G')
            ]
        }

print "kruskal: ", kruskal(grafo)
