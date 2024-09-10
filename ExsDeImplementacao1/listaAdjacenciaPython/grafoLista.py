# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""

# Grafo como uma lista de adjacência
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m-=1

    #Ex17
    def isEqual(self, g):
        if self.n != g.n or self.m != g.m:
            return False
        for i in range(self.n):
            if self.listaAdj[i] != g.listaAdj[i]:
                return False
        return True

    #Ex18
    def convertToMatrix(self):
        g = Grafo(self.n)
        g.m = self.m 
        g.listaAdj = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in self.listaAdj[i]:
                g.listaAdj[i][j] = 1
        return g

    #Ex19
    def invert(self):
        g = Grafo(self.n)
        g.m = self.m
        for i in range(self.n):
            for j in self.listaAdj[i][::-1]:
                g.listaAdj[i].append(j)
        return g
    
    #Ex20
    def isVSource(self, v):
        if len(self.listaAdj[v]) == 0:
            return 0
        
        for i in range(self.n):
            if v in self.listaAdj[i]:
                return 0
    
        return 1

    #Ex21
    def isVSink(self, v):
        if len(self.listaAdj[v]) > 0:
            return 0
        
        for i in range(self.n):
            if v in self.listaAdj[i]:
                return 1
    
        return 0
    
    #Ex22
    def isSymmetric(self):
        for i in range(self.n):
            for j in self.listaAdj[i]:
                if i not in self.listaAdj[j]:
                    return 0
        return 1
    
    #Ex23
    def initFile(self, nomeArq):
        arq = open(nomeArq, "r")
        self.n = int(arq.readline())
        self.m = int(arq.readline())
        for _ in range(self.m):
            v, w = map(int, arq.readline().split())
            self.insereA(v, w)
        arq.close()

    #Ex24
    def NDremoveV(self, v):
        for i in range(self.n):
            if v in self.listaAdj[i]:
                self.listaAdj[i].remove(v)
                self.m -= 1
        self.listaAdj[v] = []
        self.n -= 1
    
    #Ex25
    def removeV(self, v):
        self.m -= len(self.listaAdj[v])
        self.listaAdj[v] = []
        
        for i in range(self.n):
            if v in self.listaAdj[i]:
                self.listaAdj[i].remove(v)
                self.m -= 1

    #Ex26
    def isComplete(self):
        for i in range(self.n):
            if len(self.listaAdj[i]) != self.n - 1:
                return False
            
        return True
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )
        
        