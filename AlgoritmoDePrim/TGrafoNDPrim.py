# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873
## Gabriel Gonzaga Chung - 10403025

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[float('inf') for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w, peso = 1):
        if self.adj[v][w] == float('inf'):
            self.adj[v][w] = peso
            self.adj[w][v] = peso
            self.m+=1
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if self.adj[v][w] != float('inf'):
            self.adj[v][w] = float('inf')
            self.adj[w][v] = float('inf')
            self.m-=1 # atualiza qtd arestas


    # Algoritmo de Prim
    def prim(self, origin):
        # Inicializa as variaveis
        V = list(range(self.n))
        T = [origin]
        E = []
        custo = 0

        # Versao iterativa em vez de recursiva
        while set(T) != set(V):
            
            # Atualiza o conjunto de vertices que nao estao em T
            KminusT = [v for v in V if v not in T]
            valor = float('inf')
            
            # Encontra a aresta de menor peso
            for k in T:
                for i in KminusT:
                    if self.adj[k][i] < valor:
                        valor = self.adj[k][i]
                        vint = k
                        vext = i
            # Adiciona o vertice novo ao conjunto T
            T.append(vext)

            # Adiciona a aresta nova ao conjunto E
            E.append((vint, vext))

            # Atualiza o custo
            custo += valor

        return E, custo


    

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != float('inf'):
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:2d} ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = ∞ ", end="")
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
                if self.adj[i][w] != float('inf'):
                    print(f" {self.adj[i][w]:2d} ", end="") 
                else:
                    print(" ∞  ", end="")

            print("\n")
        print("\nfim da impressao do grafo." )
    