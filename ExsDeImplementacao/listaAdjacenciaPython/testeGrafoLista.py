# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:42:48 2023

@author: icalc
"""
from grafoLista import Grafo

g = Grafo(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
# mostra o grafo preenchido
g.show()
g.removeA(0,1)
g.show()

g2 = Grafo(4)
g2.insereA(0,2)
g2.insereA(2,1)
g2.insereA(2,3)
g2.insereA(1,3)

g2.show()
print(g.isEqual(g2))
print(g.convertToMatrix().listaAdj)
g2.invert().show()