#Ex7 e Ex8

class GrafoND:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self,  n=TAM_MAX_DEFAULT, isWeighted=False,):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        self.isWeighted = isWeighted
        # matriz de adjacência
        if isWeighted:
            self.adj = [[float('inf') for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w com peso weight
    def insereA(self, v, w, weight=1):
        #testa de temos a aresta
        if self.isWeighted and self.adj[v][w] == float('inf'):
            self.adj[v][w] = weight
            self.adj[w][v] = weight
        elif not self.isWeighted and self.adj[v][w] == 0:
            self.adj[v][w] = weight
            self.adj[w][v] = weight
        self.m+=1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] != 0 and self.adj[v][w] != float('inf'):
            if self.isWeighted:
                self.adj[v][w] = float('inf')
                self.adj[w][v] = float('inf')
            else:
                self.adj[v][w] = 0
                self.adj[w][v] = 0
            self.m-=1 # atualiza qtd arestas

     #Ex9
    def removeV(self, v):
        for i in range(self.n):
            self.removeA(v, i)

        if self.isWeighted:
            tempAdj = [[float('inf') for i in range(self.n - 1)] for j in range(self.n - 1)]
        else:
            tempAdj = [[0 for i in range(self.n - 1)] for j in range(self.n - 1)]
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

    #Ex10
    def isComplete(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if self.isWeighted and self.adj[i][j] == float('inf'):
                        return False
                    elif self.isWeighted and self.adj[i][j] == 0:
                        return False
        return True
    
    #Ex12
    def Complementary(self):
        if self.isWeighted:
            tempAdj = [[float('inf') for i in range(self.n)] for j in range(self.n)]
        else:
            tempAdj = [[0 for i in range(self.n)] for j in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if self.isWeighted:
                        if self.adj[i][j] == float('inf'):
                            tempAdj[i][j] = 1
                        else:
                            tempAdj[i][j] = float('inf')
                    else:
                        if self.adj[i][j] == 0:
                            tempAdj[i][j] = 1
                        else:
                            tempAdj[i][j] = 0                      
        return tempAdj

 # Ex13
    # Checa se um vértice v está conectado a um vértice w
    def isVConnected(self, v, w):
        visited = [False] * self.n

        def dfs(current):
            if current == w:
                return True
            visited[current] = True
            for neighbor in range(self.n):
                if not self.isWeighted and self.adj[current][neighbor] != 0 and not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                if self.isWeighted and self.adj[current][neighbor] != float('inf') and not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(v)

    # Checa se o grafo é conexo
    def isConnected(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if not self.isVConnected(i, j):
                    return False
        return True

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.isWeighted:
                    if self.adj[i][w] != float('inf'):
                        print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:2d} ", end="") 
                    else:
                        print(f"Adj[{i:2d},{w:2d}] = ∞ ", end="")
                else:
                    if self.adj[i][w] == 1:
                        print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                    else:
                       print(f"Adj[{i:2d},{w:2d}] = 0", end="") 
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
                if self.isWeighted:
                    if self.adj[i][w] != float('inf'):
                        print(f" {self.adj[i][w]:2d} ", end="") 
                    else:
                        print(" ∞  ", end="")
                else:
                    if self.adj[i][w] == 1:
                        print(" 1 ", end="") 
                    else:
                        print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )