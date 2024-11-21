## Igor Benites Moura - 10403462
## Rodrigo Machado de Assis Oliveira de Lima - 10401873

## Classe main, implementando um menu de opções para manipulação de um grafo.

## O histórico de alterações do código está disponível no GitHub do projeto:
## https://github.com/RodrigoLime/TeoriaDosGrafos/tree/main/Projeto

from Grafo import Grafo

def menu():
    g = Grafo()
    while True:
        print("\nMenu de Opções:")
        print("1. Ler grafo de Arquivo")
        print("2. Inserir Vértice")
        print("3. Inserir Aresta")
        print("4. Remover Vértice")
        print("5. Remover Aresta")
        print("6. Mostrar Conteúdo do Arquivo")
        print("7. Mostrar Grafo")
        print("8. Verificar Conexidade")
        print("9. Mostrar Grafo Reduzido")
        print("10. Calcular Centralidade de Vértices")
        print("11. Sair e Atualizar Arquivo")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            g.initFile('grafo.txt')
        elif opcao == 2:
            rotulo = input("Rótulo do vértice: ")
            g.insereV(rotulo)
        elif opcao == 3:
            v1 = int(input("Vértice 1: "))
            v2 = int(input("Vértice 2: "))
            peso = int(input("Peso da aresta: "))
            g.insereA(v1, v2, peso)
        elif opcao == 4:
            id_vertice = int(input("Número do vértice a remover: "))
            g.removeV(id_vertice)
        elif opcao == 5:
            v1 = int(input("Vértice 1 da Aresta a Remover: "))
            v2 = int(input("Vértice 2 da Aresta a Remover: "))
            g.removeA(v1, v2)
        elif opcao == 6:
            g.showFile('grafo.txt')
        elif opcao == 7:
            g.showRotulos()
        elif opcao == 8:
            conexidade = g.conexidade()
            if conexidade == 3:
                print("\nGrafo é fortemente conexo (C3).")
            elif conexidade == 2:
                print("\nGrafo é semi-fortemente conexo (C2).")
            elif conexidade == 1:
                print("\nGrafo é simplesmente conexo (C1).")
            else:
                print("\nGrafo é desconexo (C0).")
        elif opcao == 9:
            print("Grafo Reduzido:")
            gr = g.grafoReduzido()
            gr.showIds()
        elif opcao == 10:
            p = g.pagerank()
            print("\nPageRank:")

            # Imprime os valores de PageRank ordenados com seus índices de vértice correspondentes
            i = 1
            for index, value in p:
                print(f"{i}: Vértice {index}: ({g.rotulos[index]})")
                i += 1

        elif opcao == 11:
            g.updateFile('grafoatt.txt')
            print("Arquivo atualizado e programa encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
