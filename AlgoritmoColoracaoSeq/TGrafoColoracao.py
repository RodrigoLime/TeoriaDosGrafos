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
        self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m+=1
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m-=1 # atualiza qtd arestas


    # Algoritmo de Coloração Sequencial
    def coloracao_sequencial(self):
        C = [set() for _ in range(self.n)]
        k = 0
        for i in range(self.n):
            while True:
                if all(self.adj[i][j] == 0 or j not in C[k] for j in range(self.n)):
                    C[k].add(i)
                    break
                else:
                    k += 1
            k = 0

        # Filtra os conjuntos vazios
        C = [subset for subset in C if subset]
        return C


    

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
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
                if self.adj[i][w] != 0:
                    print(f" {self.adj[i][w]:2d} ", end="") 
                else:
                    print(" ∞  ", end="")

            print("\n")
        print("\nfim da impressao do grafo." )