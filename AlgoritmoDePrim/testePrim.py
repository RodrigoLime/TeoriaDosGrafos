## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873
## Gabriel Gonzaga Chung - 10403025

from TGrafoNDPrim import Grafo

g = Grafo(5)
g2 = Grafo(4)
g3 = Grafo(9)

# Teste Aleatório
print("\nTestando para um grafo aleatório\n")
g.insereA(0,1,20) # insere aresta 0 - 1 com peso 20
g.insereA(0,2,30)
g.insereA(2,1,25)
g.insereA(1,3,22)
g.insereA(3,4,50)

print(g.prim(0))
g.showMin()

# Teste da atividade anterior
print("\nTestando para um grafo da atividade anterior\n")
g2.insereA(0,1,20) # insere aresta 0 - 1 com peso 20
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

print(g2.prim(0))
g2.showMin()

# Teste do material de aula do professor (começando a contagem com 0 ao invés de 1)
print("\nTestando para um grafo do material de aula professor\n")
g3.insereA(0,1,4) # insere aresta 0 - 1 com peso 4
g3.insereA(0,5,5)
g3.insereA(1,0,4)
g3.insereA(1,2,7)
g3.insereA(1,5,3)
g3.insereA(2,1,7)
g3.insereA(2,3,5)
g3.insereA(2,6,6)
g3.insereA(3,2,5)
g3.insereA(3,4,3)
g3.insereA(4,3,3)
g3.insereA(4,6,2)
g3.insereA(4,7,4)
g3.insereA(5,0,5)
g3.insereA(5,1,3)
g3.insereA(5,6,7)
g3.insereA(5,8,5)
g3.insereA(6,2,6)
g3.insereA(6,4,2)
g3.insereA(6,5,7)
g3.insereA(6,7,6)
g3.insereA(7,4,4)
g3.insereA(7,6,6)
g3.insereA(7,8,8)
g3.insereA(8,5,5)
g3.insereA(8,7,8)

print(g3.prim(0))
g3.showMin()