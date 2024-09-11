# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
from collections import deque

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

    #Ex1
    def inDegree(self, v):
        grau = 0
        for i in range(self.n):
            # para cada vértice i verifica se é adjacente a v
            if self.adj[i][v] == 1:
                grau+=1
        return grau

    #Ex2
    def outDegree(self, v):
        grau = 0
        for i in range(self.n):
            # para cada vértice ivverifica se é adjacente a i
            if self.adj[v][i] == 1:
                grau+=1
        return grau
    
    #Ex3
    def isVSource(self, v):
        # usa as funções inDegree e outDegree para verificar se é fonte
        return (self.inDegree(v) == 0 and self.outDegree(v) > 0)
    
    #Ex4
    def isVSink(self, v):
        # usa as funções inDegree e outDegree para verificar se é sorvedouro
        return (self.inDegree(v) > 0 and self.outDegree(v) == 0)
    
    #Ex5
    def isSymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                # se algum elemento da matriz for diferente do elemento simétrico, a matriz não é simétrica
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
        # remove todas as arestas que tem v como origem ou destino
        for i in range(self.n):
            self.removeA(v, i)
            self.removeA(i, v)

        # cria uma nova matriz de adjacência com um vértice a menos
        tempAdj = [[0 for _ in range(self.n - 1)] for _ in range(self.n - 1)]
        i2 = 0
        j2 = 0

        # copia os valores da matriz antiga para a nova matriz, excluindo a linha e coluna do vértice removido
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
                # se algum vertice nao for adjacente a todos os outros, o grafo nao é completo
                if i != j and self.adj[i][j] == 0:
                    return False
        return True

    #Ex12
    def complementary(self):
        tempAdj = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i != j:  # Pula diagonal
                    # inverte os valores da matriz de adjacência, tirando a diagonal principal
                    if self.adj[i][j] == 0:
                        tempAdj[i][j] = 1
                    else:
                        tempAdj[i][j] = 0
        return tempAdj
    
    #Ex14
    def directTransitiveClosure(self, v):
        # usa busca em largura para encontrar todos os vértices que são alcançáveis a partir de v
        reach = [0] * self.n
        queue = deque([v])
        reach[v] = 1

        # enquanto a fila não estiver vazia, verifica os vértices adjacentes
        while queue:
            current = queue.popleft()
            for j in range(self.n):
                if self.adj[current][j] == 1 and not reach[j]:
                    reach[j] = 1
                    queue.append(j)

        return reach

    def inverseTransitiveClosure(self, v):
        # usa busca em largura para encontrar todos os vértices que alcançam v
        reach = [0] * self.n
        queue = deque([v])
        reach[v] = 1

        # enquanto a fila não estiver vazia, verifica os vértices adjacentes
        while queue:
            current = queue.popleft()
            for j in range(self.n):
                if self.adj[j][current] == 1 and not reach[j]:
                    reach[j] = 1
                    queue.append(j)

        return reach
    
    def isStronglyConnected(self):
        # usa os metodos de fecho transitivo direto e inverso para verificar se o grafo é fortemente conexo
        for v in range(self.n):
            direct_reach = self.directTransitiveClosure(v)
            inverse_reach = self.inverseTransitiveClosure(v)
            
            # se nao for uma interseccao completa entre os fechos, o grafo nao é fortemente conexo
            if not all(direct_reach) or not all(inverse_reach):
                return False
        return True
    
    def isSemiStronglyConnected(self):
        # usa os metodos de fecho transitivo direto e inverso para verificar se o grafo é semi-fortemente conexo
        for v in range(self.n):
            direct_reach = self.directTransitiveClosure(v)
            inverse_reach = self.inverseTransitiveClosure(v)
            
            for i in range(self.n):
                # se um vértice não for alcançável por v ou não alcançar v, o grafo não é semi-fortemente conexo
                if not direct_reach[i] and not inverse_reach[i]:
                    return False
        return True

    def isDisconnected(self):
        # usa os metodos de fecho transitivo direto e inverso para verificar se o grafo é desconexo
        for u in range(self.n):
            for v in range(self.n):
                if u != v:
                    direct_reach_u = self.directTransitiveClosure(u)
                    direct_reach_v = self.directTransitiveClosure(v)
                    # se para algum par de vértices u e v, u não alcançar v e v não alcançar u, o grafo é desconexo
                    if not direct_reach_u[v] and not direct_reach_v[u]:
                        return True
        return False

    def connectivity(self):
        # retorna a conexidade do grafo: C3, C2, C1 ou C0
        if self.isStronglyConnected():
            return 3
        if self.isSemiStronglyConnected():
            return 2
        if self.isDisconnected():
            return 0
        return 1


        
    #Ex15    
    def getStronglyConnectedComponents(self):
        # inicia a lista de sccs e vetor de visitados
        visited = [False] * self.n
        sccs = []

        for v in range(self.n):
            # se o vértice não foi visitado, calcula o fecho transitivo direto e inverso
            if not visited[v]:
                direct_reach = self.directTransitiveClosure(v)
                inverse_reach = self.inverseTransitiveClosure(v)
                # cria um um scc com a interseccao dos fechos
                scc = [i for i in range(self.n) if direct_reach[i] and inverse_reach[i]]
                sccs.append(scc)
                # marca todos os vértices do scc como visitados
                for u in scc:
                    visited[u] = True

        return sccs

    def reduce(self):
        sccs = self.getStronglyConnectedComponents()
        scc_count = len(sccs)
        # cria um dicionário para mapear os vértices para seus respectivos sccs
        scc_map = {v: i for i, scc in enumerate(sccs) for v in scc}

        # cria uma matriz de adjacência reduzida com os sccs
        reduced_adj = [[0] * scc_count for _ in range(scc_count)]
        for u in range(self.n):
            for v in range(self.n):
                # se u e v são adjacentes, verifica se os sccs de u e v são diferentes
                if self.adj[u][v] == 1:
                    u_scc = scc_map[u]
                    v_scc = scc_map[v]
                    # se os sccs são diferentes, adiciona uma aresta entre os sccs
                    if u_scc != v_scc:
                        reduced_adj[u_scc][v_scc] = 1

        return Grafo(scc_count, reduced_adj)
    

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
    