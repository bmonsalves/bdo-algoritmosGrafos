from collections import defaultdict
from heapq import *

#BUSCAR ARBOL MINIMO 



def prim( grafo ):
    conn = defaultdict( list )
    for c,n1,n2 in grafo['aristas']:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )
 
    mst = []
    usado = set( grafo['nodos'][0] )
    usable_arista = conn[ grafo['nodos'][0] ][:]
    heapify( usable_arista )
 
    while usable_arista:
        cost, n1, n2 = heappop( usable_arista )
        if n2 not in usado:
            usado.add( n2 )
            mst.append( ( cost, n1, n2  ) )
 
            for e in conn[ n2 ]:
                if e[ 2 ] not in usado:
                    heappush( usable_arista, e )
    return mst
 

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
