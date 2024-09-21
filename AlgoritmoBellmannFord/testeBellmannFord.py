## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from TGrafoBellmannFord import Grafo

# 1) Grafo do material de aula (slides)
g1 = Grafo(5, isWeighted=True)

g1.insereA(0,1,1) # insere aresta 0->1 com peso 6
g1.insereA(0,4,1)
g1.insereA(1,2,1)
g1.insereA(1,3,2)
g1.insereA(2,3,4)
g1.insereA(2,4,2)
g1.insereA(3,0,3)
g1.insereA(4,0,2)
g1.insereA(4,3,1)

d, rot = g1.bellmannFord(0)
print("Grafo 1: ")
print("Distâncias: ", d)
print("Rotas: ", rot)



# 2) Grafo da atividade anterior
g2 = Grafo(4, isWeighted=True)

g2.insereA(0,1,20) # insere aresta 0->1 com peso 20
g2.insereA(0,2,30)
g2.insereA(0,3,50)
g2.insereA(1,0,20)
g2.insereA(1,2,40)
g2.insereA(1,3,15)
g2.insereA(2,0,30)
g2.insereA(2,1,40)
g2.insereA(2,3,15)
g2.insereA(3,0,50)
g2.insereA(3,1,15)
g2.insereA(3,2,15)

d, rot = g2.bellmannFord(2)
print("\nGrafo 2: ")
print("Distâncias: ", d)
print("Rotas: ", rot)

