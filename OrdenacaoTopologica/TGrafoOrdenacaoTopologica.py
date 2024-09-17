# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from filaCircularPython import filaCircular

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, isWeighted=False):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        if isWeighted:
            self.adj = [[float('inf') for i in range(n)] for j in range(n)]
        else:
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

    def inDegree(self, v):
        grau = 0
        for i in range(self.n):
            # para cada vértice i verifica se é adjacente a v
            if self.adj[i][v] == 1:
                grau+=1
        return grau

    def outDegree(self, v):
        grau = 0
        for i in range(self.n):
            # para cada vértice ivverifica se é adjacente a i
            if self.adj[v][i] == 1:
                grau+=1
        return grau
    
    def topologicOrdering(self):
        # grau de entrada de cada vértice
        GE = [0] * self.n
        for i in range(self.n):
            GE[i] = self.inDegree(i)
        
        # fila de vértices com grau de entrada zero
        F = filaCircular.FilaCircular()
        for i in range(self.n):
            if GE[i] == 0:
                print(f"Vértice {i} foi colocado na fila")
                F.enqueue(i)
                GE[i] = -1

        # processa os vértices
        while not F.isEmpty():
            print("Array GE:", GE)
            # remove um vértice da fila
            v = F.dequeue()
            print(f"Vértice {v} foi removido da fila")
            for w in range(self.n):
                # para cada vértice w adjacente a v, decrementa o grau de entrada e se for zero, coloca na fila
                if self.adj[v][w] == 1:
                    GE[w]-=1
                    if GE[w] == 0:
                        print(f"Vértice {w} foi colocado na fila")
                        F.enqueue(w)
                        GE[w] = -1

    

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
    