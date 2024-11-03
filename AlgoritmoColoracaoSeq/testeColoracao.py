## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873
## Gabriel Gonzaga Chung - 10403025

from TGrafoColoracao import Grafo

g = Grafo(9)

g.insereA(0, 5)
g.insereA(0, 6)
g.insereA(0, 8)
g.insereA(1, 2)
g.insereA(1, 7)
g.insereA(2, 4)
g.insereA(2, 7)
g.insereA(3, 4)
g.insereA(3, 5)
g.insereA(3, 7)
g.insereA(4, 6)
g.insereA(5, 6)
g.insereA(5, 8)
g.insereA(6, 7)
g.insereA(6, 8)

coloracao = g.coloracao_sequencial()
print(coloracao)