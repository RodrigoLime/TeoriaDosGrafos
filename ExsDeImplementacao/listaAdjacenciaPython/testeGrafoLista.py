# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:42:48 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from grafoLista import Grafo

# Testes estão no relatório, não estão todos aqui porque fomos testando e
# apagando para o terminal não ficar poluído 

g = Grafo(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(0,3)
g.insereA(1,0)
g.insereA(1,2)
g.insereA(1,3)
g.insereA(2,0)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(3,0)
g.insereA(3,1)
g.insereA(3,2)

# mostra o grafo preenchido
g.show()

print(f"Grafo é completo? {g.isComplete()}")

# print("Grafo do arquivo inputLista.txt:")
# gArq = Grafo()
# gArq.initFile("inputLista.txt")
# gArq.show()

# g2 = Grafo(4)
# g2.insereA(0,2)
# g2.insereA(2,1)
# g2.insereA(2,3)
# g2.insereA(1,3)

# g2.show()
# print(F"Grafos são iguais? {g.isEqual(g2)}")
# print(g.convertToMatrix().listaAdj)
# g2.invert().show()