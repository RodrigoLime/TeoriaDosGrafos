## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from TGrafoDijkstra import Grafo

g = Grafo(4, isWeighted=True)

g.insereA(0,1,20) # insere aresta 0->1 com peso 20
g.insereA(0,2,30)
g.insereA(0,3,50)
g.insereA(1,0,20)
g.insereA(1,2,40)
g.insereA(1,3,15)
g.insereA(2,0,30)
g.insereA(2,1,40)
g.insereA(2,3,15)
g.insereA(3,0,50)
g.insereA(3,1,15)
g.insereA(3,2,15)

d, rot = g.dijsktra(2)
print("Distâncias: ", d)
print("Rotas: ", rot)

