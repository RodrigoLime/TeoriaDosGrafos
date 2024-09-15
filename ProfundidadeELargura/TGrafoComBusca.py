# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""

## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

from collections import deque

import pilhaPython.pilha as pilha
import filaCircularPython.filaCircular as fila

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

    def dfs(self, start):
        visited = [False] * self.n
        stack = pilha.Pilha()
        stack.push(start)
        visited[start] = True

        while not stack.isEmpty():
            n = stack.pop()
            print(f"Visitou vértice {n}")

            for m in range(self.n):
                if self.adj[n][m] == 1 and not visited[m]:
                    print(f"Vértice {n} entrou na pilha")
                    stack.push(n)
                    stack.push(m)
                    visited[m] = True
                    break
        
    def bfs(self, start):
        visited = [False] * self.n
        queue = fila.FilaCircular(self.n)
        queue.enqueue(start)
        visited[start] = True

        while not queue.isEmpty():
            n = queue.dequeue()
            print(f"Visitou vértice {n}")

            for m in range(self.n):
                if self.adj[n][m] == 1 and not visited[m]:
                    print(f"Vértice {m} entrou na fila")
                    queue.enqueue(m)
                    visited[m] = True


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
    