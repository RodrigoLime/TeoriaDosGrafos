## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873
## Gabriel Gonzaga Chung - 10403025

from TGrafoNDPrim import Grafo

g = Grafo(5)

g.insereA(0,1,20) # insere aresta 0->1 com peso 20
g.insereA(0,2,30)
g.insereA(2,1,25)
g.insereA(1,3,22)
g.insereA(3,4,50)

print(g.prim(0))