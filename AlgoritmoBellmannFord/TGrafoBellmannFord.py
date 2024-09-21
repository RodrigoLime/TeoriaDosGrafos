# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, isWeighted=False):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        self.isWeighted = isWeighted
        # matriz de adjacência
        if isWeighted:
            self.adj = [[float('inf') for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w, weight=1):
        if self.isWeighted:
            if self.adj[v][w] == float('inf'):
                self.adj[v][w] = weight
                self.m+=1 # atualiza qtd arestas
        else:
            if self.adj[v][w] == 0:
                self.adj[v][w] = 1
                self.m+=1
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if self.isWeighted:
            if self.adj[v][w] != float('inf'):
                self.adj[v][w] = float('inf')
                self.m-=1
        else:
            if self.adj[v][w] == 1:
                self.adj[v][w] = 0
                self.m-=1 # atualiza qtd arestas


    # Algoritmo de Bellmann-Ford	
    def bellmannFord(self, origin):
        # apenas para grafos ponderados
        if not self.isWeighted:
            print("Grafo não é ponderado")
            return

        # inicializa as variaveis
        d = [float('inf')] * self.n 
        d[origin] = 0
        rot = [-1] * self.n


        for j in range(self.n):
            for i in range(self.n):
                #se tiver um caminho de j para i
                if self.adj[j][i] != float('inf'):
                    #se a distancia da origem ate i for maior que a distancia de j + peso da aresta
                    if d[i] > d[j] + self.adj[j][i]:
                        # atualiza a distancia de i
                        d[i] = d[j] + self.adj[j][i]
                        rot[i] = j
                    
        return d, rot

    

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
    