# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:05 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from grafoMatriz import Grafo
from TGrafoND import GrafoND

# Testes estão no relatório, não estão todos aqui porque fomos testando e
# apagando para o terminal não ficar poluído 

g = Grafo(5)
#insere as arestas do grafo
g.insereA(0,1)
g.insereA(1,2)
g.insereA(2,0)
g.insereA(2,3)
g.insereA(3,4)
g.insereA(4,3)
g.showMin()

gr = g.reduce()
print("Grafo reduzido:")
gr.showMin()

gw = Grafo(5, isWeighted=True)

gw.insereA(0,1,20) # insere aresta 0->1 com peso 20
gw.insereA(0,2,30)
gw.insereA(2,1,21)
gw.insereA(1,3,22)
gw.insereA(3,4,50)

gw.showMin()

gw.removeA(0,1)

gw.show()




# remove vertice 0
g.removeV(0)
g.showMin()
# print(f"Grafo é simétrico? {g.isSymmetric()}")

print("Grafo do arquivo inputMatriz.txt:")
gArq = Grafo()

gArq.initFile("inputMatriz.txt")

gArq.showMin()


# remove vertice 0

#Grafo nao direcionado sem peso

nd = GrafoND(3)
nd.insereA(0,1)
nd.insereA(0,2)
nd.insereA(1,2)

nd.showMin()
print(f"Grafo é conexo? {nd.isConnected()}")


# Grafo nao direcionado com peso
nd = GrafoND(4, isWeighted=True)

nd.insereA(0,1,20) # insere aresta 0->1 com peso 20
nd.insereA(0,2,30)
nd.insereA(2,1,21)
nd.insereA(1,3,22)
nd.removeA(0,1)

nd.showMin()