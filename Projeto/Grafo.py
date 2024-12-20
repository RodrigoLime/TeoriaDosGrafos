## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

import os
from collections import deque

# Grafo como uma lista de adjacência
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        # foi criada uma lista de adjacencia auxiliar para armazenar os pesos das arestas
        self.listaAdjPesos = [[] for i in range(self.n)]
        # lista dos rotulos dos vértices
        self.rotulos = [" " for i in range(self.n)]
        self.tipo = 0
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w, peso):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            print("\nVértice inválido")
            return

        if v == w:
            print("\nArestas entre o mesmo vértice não são permitidas")
            return

        if w not in self.listaAdj[v]:
            self.listaAdj[v].append(w)
            self.listaAdjPesos[v].append(peso)
            self.m+=1
            if peso != 0:
                print(f"\nAresta ({v}, {w}) inserida com sucesso.")
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if v < 0 or v >= self.n or w < 0 or w >= self.n:
            print("\nVértice inválido")
            return
        
        if w in self.listaAdj[v]:
            index = self.listaAdj[v].index(w)
            self.listaAdj[v].pop(index)
            self.listaAdjPesos[v].pop(index)
            self.m-=1
            print(f"\nAresta ({v}, {w}) removida com sucesso.")
        else:
            print(f"\nAresta ({v}, {w}) não existe no grafo.")

    # insere um vértice no Grafo
    def insereV(self, rotulo):
        self.listaAdj.append([])
        self.listaAdjPesos.append([])
        self.rotulos.append(rotulo)
        self.n += 1
        print(f"\nVértice {rotulo} inserido com sucesso.")

    # remove um vértice do Grafo        
    def removeV(self, v):
        if v < 0 or v >= self.n:
            print("\nVértice inválido")
            return

        self.m -= len(self.listaAdj[v])
        
        # Remove arestas que tem v como origem
        self.listaAdj[v] = []
        self.listaAdjPesos[v] = []
        
        # Remove arestas que tem v como destino
        for i in range(self.n):
            if v in self.listaAdj[i]:
                index = self.listaAdj[i].index(v)
                self.listaAdj[i].pop(index)
                self.listaAdjPesos[i].pop(index)
                self.m -= 1

        # Atualiza os índices dos vértices
        for i in range(self.n):
            self.listaAdj[i] = [x - 1 if x > v else x for x in self.listaAdj[i]]
            if i > v:            
                self.listaAdj[i-1] = self.listaAdj[i]
                self.listaAdjPesos[i-1] = self.listaAdjPesos[i]

        # Remove o ultimo vértice da lista de adjacência
        self.listaAdj.pop()
        self.listaAdjPesos.pop()


        # Remove o vértice da lista de rotulos
        self.rotulos.pop(v)

        self.n -= 1
        print(f"\nVértice {v} removido com sucesso.")

    def grauEntrada (self, v):
        # Retorna o grau de entrada do vértice v
        grau = 0
        for i in range(self.n):
            if v in self.listaAdj[i]:
                grau += 1
        return grau
    
    def grauEntradaPonderado (self, v):
        # Retorna o grau de entrada ponderado do vértice v
        grau = 0
        for i in range(self.n):
            if v in self.listaAdj[i]:
                index = self.listaAdj[i].index(v)
                grau += self.listaAdjPesos[i][index]
        return grau

    def grauSaida (self, v):
        # Retorna o grau de saída do vértice v
        return len(self.listaAdj[v])
    
    def grauSaidaPonderado (self, v):
        # Retorna o grau de saída ponderado do vértice v
        grau = 0
        for i in range(len(self.listaAdj[v])):
            grau += self.listaAdjPesos[v][i]
        return grau

    def grau (self, v):
        # Retorna o grau do vértice v
        return self.grauEntrada(v) + self.grauSaida(v)
    
    def grauPonderado (self, v):
        # Retorna o grau ponderado do vértice v
        return self.grauEntradaPonderado(v) + self.grauSaidaPonderado(v)

    #Algoritmo de PageRank
    def pagerank(self, d=0.85, max_iterations=100, tol=1.0e-6):
        """
        Calcula o PageRank para cada vértice no grafo, considerando os pesos das conexões.
        
        Parametros: 
        d (float): Fator de amortecimento.
        max_iterations (int): Número máximo de iterações.
        tol (float): Tolerância para a convergência.
        
        Returns:
        list: Lista de tuplas contendo o índice do vértice e seu valor de PageRank em ordem decrescente de valor adquirido.
        """
        # Passo 1: Inicializa o PageRank de cada vértice
        n = self.n
        pagerank = [1.0 / n] * n
        new_pagerank = [0.0] * n

        # Passo 2: Itera até a convergência
        for _ in range(max_iterations):
            # Calcula a soma dos PageRanks dos vértices sem arestas de saída
            dangling_sum = sum(pagerank[i] for i in range(n) if not self.listaAdj[i])

            for i in range(n):
                new_pagerank[i] = (1 - d) / n
                new_pagerank[i] += d * dangling_sum / n
                for j in range(n):
                    if i in self.listaAdj[j]:
                        index = self.listaAdj[j].index(i)
                        peso = self.listaAdjPesos[j][index]
                        new_pagerank[i] += d * pagerank[j] * peso / sum(self.listaAdjPesos[j])

            # Verifica a convergência
            if sum(abs(new_pagerank[i] - pagerank[i]) for i in range(n)) < tol:
                break

            pagerank, new_pagerank = new_pagerank, [0.0] * n
        
        # Adiciona os índices aos valores de PageRank
        pagerank_with_indices = list(enumerate(pagerank))

        # Ordena os valores de PageRank em ordem decrescente
        pagerank_with_indices.sort(key=lambda x: x[1], reverse=True)

        return pagerank_with_indices
    
    def fechoTransitivoDireto(self, v):
        # usa busca em largura para encontrar todos os vértices que são alcançáveis a partir de v
        alcance = [0] * self.n
        fila = deque([v])
        alcance[v] = 1

        # enquanto a fila não estiver vazia, verifica os vértices adjacentes
        while fila:
            atual = fila.popleft()
            for vizinho in self.listaAdj[atual]:
                if not alcance[vizinho]:
                    alcance[vizinho] = 1
                    fila.append(vizinho)

        return alcance

    def fechoTransitivoInverso(self, v):
        # usa busca em largura para encontrar todos os vértices que alcançam v
        alcance = [0] * self.n
        fila = deque([v])
        alcance[v] = 1

        # enquanto a fila não estiver vazia, verifica os vértices adjacentes
        while fila:
            atual = fila.popleft()
            for i in range(self.n):
                if atual in self.listaAdj[i] and not alcance[i]:
                    alcance[i] = 1
                    fila.append(i)

        return alcance
    
    def fortementeConexo(self):
        # usa os metodos de fecho transitivo direto e inverso para verificar se o grafo é fortemente conexo
        for v in range(self.n):
            fecho_direto = self.fechoTransitivoDireto(v)
            fecho_inverso = self.fechoTransitivoInverso(v)
            
            # se nao for uma interseccao completa entre os fechos, o grafo nao é fortemente conexo
            if not all(fecho_direto) or not all(fecho_inverso):
                return False
        return True
    
    def semiFortementeConexo(self):
        # usa os metodos de fecho transitivo direto e inverso para verificar se o grafo é semi-fortemente conexo
        for v in range(self.n):
            fecho_direto = self.fechoTransitivoDireto(v)
            fecho_inverso = self.fechoTransitivoInverso(v)
            
            for i in range(self.n):
                # se um vértice não for alcançável por v ou não alcançar v, o grafo não é semi-fortemente conexo
                if not fecho_direto[i] and not fecho_inverso[i]:
                    return False
        return True

    def desconexo(self):
        # Cria o grafo não direcionado equivalente pois direcao em grafos s-conexos não importa
        NDGraph = Grafo(self.n)
        NDGraph.listaAdj = [[] for _ in range(self.n)]
        
        for i in range(self.n):
            for j in self.listaAdj[i]:
                NDGraph.insereA(i, j, 0)
                NDGraph.insereA(j, i, 0)

        # usa o metodo de fecho transitivo direto em pares de vertices para verificar se o grafo é desconexo
        for u in range(self.n):
            fecho_direto = NDGraph.fechoTransitivoDireto(u)
            for v in range(self.n):
                if u != v and not fecho_direto[v]:
                    return True
                
        return False

    def conexidade(self):
        # retorna a conexidade do grafo: C3, C2, C1 ou C0
        if self.fortementeConexo():
            return 3
        if self.semiFortementeConexo():
            return 2
        if self.desconexo():
            return 0
        return 1

    def componentesFortementeConexos(self):
        # inicia a lista de sccs e vetor de visitados
        visitado = [False] * self.n
        sccs = []

        for v in range(self.n):
            # se o vértice não foi visitado, calcula o fecho transitivo direto e inverso
            if not visitado[v]:
                fecho_direto = self.fechoTransitivoDireto(v)
                fecho_inverso = self.fechoTransitivoInverso(v)
                # cria um um scc com a interseccao dos fechos
                scc = [i for i in range(self.n) if fecho_direto[i] and fecho_inverso[i]]
                sccs.append(scc)
                # marca todos os vértices do scc como visitados
                for u in scc:
                    visitado[u] = True

        return sccs

    def grafoReduzido(self):
        sccs = self.componentesFortementeConexos()
        scc_contagem = len(sccs)
        # cria um dicionário para mapear cada vértices ao seu respectivo scc
        scc_map = {v: i for i, scc in enumerate(sccs) for v in scc}

        # cria uma lista de adjacência reduzida com os sccs
        reduced_adj = [[] for _ in range(scc_contagem)]
        for u in range(self.n):
            for v in self.listaAdj[u]:
                u_scc = scc_map[u]
                v_scc = scc_map[v]
                # se os sccs são diferentes, adiciona uma aresta entre os sccs
                if u_scc != v_scc and v_scc not in reduced_adj[u_scc]:
                    reduced_adj[u_scc].append(v_scc)

        reducedGraph = Grafo(scc_contagem)
        reducedGraph.m = sum(len(adj) for adj in reduced_adj)
        reducedGraph.listaAdj = reduced_adj
        return reducedGraph

    # Inicializa o grafo a partir de um arquivo
    def initFile(self, nomeArq):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, nomeArq)
        try:
            with open(file_path, "r", encoding="utf-8") as arq:
                self.tipo = int(arq.readline().strip())
                self.n = int(arq.readline().strip())
                self.rotulos = [''] * self.n
                self.listaAdj = [[] for i in range(self.n)]
                self.listaAdjPesos = [[] for i in range(self.n)]
                for _ in range(self.n):
                    line = arq.readline().strip()
                    parts = line.split(' ', 1)
                    id = int(parts[0])
                    rotulo = parts[1].strip('"')
                    self.rotulos[id] = rotulo
                    print(f"Vértice {id}: {rotulo} inserido")
                m = int(arq.readline())
                for _ in range(m):
                    line = arq.readline().strip()
                    a, b, peso = map(int, line.split())
                    self.insereA(a, b, peso)
                print("\nGrafo lido do arquivo grafo.txt.")

        except FileNotFoundError:
            print(f"Erro: O arquivo '{nomeArq}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nomeArq}': {e}")
    
    # Atualiza o arquivo de entrada do grafo
    def updateFile(self, nomeArq):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, nomeArq)
        with open(file_path, "w", encoding="utf-8") as arq:
            arq.write(f"{self.tipo}\n")
            arq.write(f"{self.n}\n")
            for i in range(self.n):
                arq.write(f"{i} \"{self.rotulos[i]}\"\n")
            arq.write(f"{self.m}\n")
            for i in range(self.n):
                for j in range(len(self.listaAdj[i])):
                    arq.write(f"{i} {self.listaAdj[i][j]} {self.listaAdjPesos[i][j]}\n")
                
        arq.close()
    
    # Apresenta as informações do arquivo de entrada do grafo
    def showFile(self, nomeArq):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, nomeArq)
        try:
            with open(file_path, "r", encoding="utf-8") as arq:
                tipo = int(arq.readline().strip())
                n = int(arq.readline().strip())
                rotulos = {}
                for _ in range(n):
                    line = arq.readline().strip()
                    parts = line.split(' ', 1)
                    id = int(parts[0])
                    rotulo = parts[1].strip('"')
                    rotulos[id] = rotulo
                m = int(arq.readline().strip())
                arestas = []
                for _ in range(m):
                    line = arq.readline().strip()
                    a, b, peso = map(int, line.split())
                    arestas.append((a, b, peso))

                print(f"\nTipo do grafo: {tipo}")
                print(f"\nVértices: {n}")
                for i in range(n):
                    print(f"{i}: {rotulos[i]}")
                print(f"\nArestas: {m}")
                for a, b, peso in arestas:
                    print(f"{a} {b}, peso {peso}")

        except FileNotFoundError:
            print(f"Erro: O arquivo '{nomeArq}' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nomeArq}': {e}")
    
        
	# Apresenta o Grafo contendo número de vértices, arestas e a lista de adjacência
    # com os identificadores dos vértices
    def showIds(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )

    # Apresenta o Grafo contendo número de vértices, arestas e a lista de adjacência
    # com os rótulos dos vértices e o peso das arestas
    def showRotulos(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            # Checa se o vértice possui um rótulo
            if i < len(self.rotulos) and self.rotulos[i]:
                label = self.rotulos[i]
            else:
                label = f"Vertex {i}"  # Rotulo padrao caso nao tenha sido definido

            print(f"\n{label}: ", end="")
            for w in range(len(self.listaAdj[i])):
                vertice = self.listaAdj[i][w]
                peso = self.listaAdjPesos[i][w]

                # Checa se o vértice possui um rótulo
                if vertice < len(self.rotulos) and self.rotulos[vertice]:
                        # Se possuir, usa o rótulo
                        rotulo = self.rotulos[vertice]
                else:
                        rotulo = f"Vertex {vertice}"  # Rotulo padrao caso nao tenha sido definido

                print(f"{rotulo} - peso {peso}, ", end="") 

        print("\n\nfim da impressao do grafo.")
        