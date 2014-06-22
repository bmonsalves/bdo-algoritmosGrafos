from collections import defaultdict
from heapq import *

#BUSCAR ARBOL MINIMO 



def prim( grafo ):
    #crea listas en base a un indice comun, en este caso los indices seran los nodos 1 y 2
    #en cada indice se almacena la tupla (c, n1, n2)
    conn = defaultdict( list )
    for c,n1,n2 in grafo['aristas']:
        #direccionamiento
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )
 
    recorrido = []
    #toma el nodo inicial
    usado = set( grafo['nodos'][0] )
    #toma las aristas que contienen el nodo inicial
    nueva_arista = conn[ grafo['nodos'][0] ][:]
    
    #mantiene en la posicion 0 el menor valor de la lista
    heapify( nueva_arista )
 
    while nueva_arista:
        #saca el primer valor de la lista y lo almacena en costo, n1, n2
        costo, n1, n2 = heappop( nueva_arista )
        #pregunta si el nodo final de la arista no ha sido visitado
        if n2 not in usado:
            usado.add( n2 )
            #agrega la arista al recorrido
            recorrido.append( ( costo, n1, n2  ) )
            #print "recorrido",recorrido

            #recorre la lista de nodos invertidos y en caso de que no se aya pasado por el nodo lo agrega a la lista de aristas.
            for e in conn[ n2 ]:
                # e[2] corresponde al "nodo de llegada"
                if e[ 2 ] not in usado:
                    #agrega "e" a nueva_arista
                    heappush( nueva_arista, e )
    return recorrido
 
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
 
print "prim:", prim(grafo)
