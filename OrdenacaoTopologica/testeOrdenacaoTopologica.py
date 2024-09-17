## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from TGrafoOrdenacaoTopologica import Grafo

g = Grafo(8)

g.insereA(0,1) #a -> b
g.insereA(0,2) #a -> c
g.insereA(0,4) #a -> e
g.insereA(1,3) #b -> d
g.insereA(1,4) #b -> e
g.insereA(2,5) #c -> f
g.insereA(2,6) #c -> g
g.insereA(3,7) #d -> h
g.insereA(4,7) #e -> h
g.insereA(5,4) #f -> e
g.insereA(5,6) #f -> g
g.insereA(6,7) #g -> h

g.topologicOrdering()
