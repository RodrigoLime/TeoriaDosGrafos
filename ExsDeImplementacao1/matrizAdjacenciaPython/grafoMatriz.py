# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m-=1 # atualiza qtd arestas

    #Ex1
    def inDegree(self, v):
        grau = 0
        for i in range(self.n):
            if self.adj[i][v] == 1:
                grau+=1
        return grau

    #Ex2
    def outDegree(self, v):
        grau = 0
        for i in range(self.n):
            if self.adj[v][i] == 1:
                grau+=1
        return grau
    
    #Ex3
    def isVSource(self, v):
        return (self.inDegree(v) == 0 and self.outDegree(v) > 0)
    
    #Ex4
    def isVSink(self, v):
        return (self.inDegree(v) > 0 and self.outDegree(v) == 0)
    
    #Ex5
    def isSymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return False
        return True

    #Ex6
    def initFile(self, nomeArq):
        arq = open(nomeArq, "r")
        self.n = int(arq.readline())
        self.m = int(arq.readline())
        for _ in range(self.m):
            v, w = map(int, arq.readline().split())
            self.insereA(v, w)
        arq.close()

    #Ex9
    def removeV(self, v):
        for i in range(self.n):
            self.removeA(v, i)
            self.removeA(i, v)

        tempAdj = [[0 for _ in range(self.n - 1)] for _ in range(self.n - 1)]
        i2 = 0
        j2 = 0
        for i in range(self.n):
            j2 = 0
            if i == v:
                continue
            for j in range(self.n):
                if j == v:
                    continue
                tempAdj[i2][j2] = self.adj[i][j]
                j2+=1
            i2+=1
        self.n-=1
        self.adj = tempAdj
    
    #Ex11
    def isComplete(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.adj[i][j] == 0:
                    return False
        return True

    #Ex12
    def Complementary(self):
        tempAdj = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i != j:  # Pula diagonal
                    if self.adj[i][j] == 0:
                        tempAdj[i][j] = 1
                    else:
                        tempAdj[i][j] = 0
        return tempAdj
    
    #Ex14S
    def directTransitiveClosure(self):
        reach = [[self.adj[i][j] for j in range(self.n)] for i in range(self.n)]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        return reach

    def inverseTransitiveClosure(self):
        reach = [[self.adj[j][i] for j in range(self.n)] for i in range(self.n)]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

        return reach
        
    #Ex15
    #def Reduce(self):

        

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    