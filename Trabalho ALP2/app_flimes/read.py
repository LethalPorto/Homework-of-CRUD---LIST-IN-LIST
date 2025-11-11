# Vitor e Henrique
# E Gustavo Cavarzan
# read.py

def mostrar_filme_serie(filme):
    for i in range(4):
        if i == 0:
            print("Título: ", end= ' ')
        elif i == 1:
            print("Gênero: ", end= ' ')
        elif i == 2:
            print("Ano: ", end= ' ')
        elif i == 3:
            print("Plataforma: ", end= ' ')
            
        print(filme[i], end=' ')
    print()


def ler(filme_series):
    while True:
        while True:
            try:
                print("\nLer:\n")
                print("1) Ver todos os filmes\n2) Ver filmes de uma plataforma\n3) Ver filmes entre certos anos\n4) Ver filmes por gênero\n5) Buscar um filme específico\n0) Voltar ao menu principal")
                opcao = int(input("Opção: "))
                if opcao < 0 or opcao > 5:
                    print('ERRO. Digite apenas números entre 0 e 5')
                else:
                    break
            except ValueError:
                print('ERRO. Digite apenas números')
        if opcao == 0:
            return

        elif opcao == 1:
            for filme in filme_series:
                mostrar_filme_serie(filme)
        elif opcao == 2:
            plataforma = input("digite o nome do plataforma: ")
            for filme in filme_series:
                if plataforma == filme [3]:
                    mostrar_filme_serie(filme)

        elif opcao == 3:
            ano1 = int(input("digite o ano para começar : "))
            ano2 = int(input("digite o ano para terminar : "))
            if ano1 > ano2:
                for filme in filme_series:
                    if filme[2] >= ano2 and filme[2] <= ano1:
                        mostrar_filme_serie(filme)

            if ano1 < ano2:
                for filme in filme_series:
                    if filme[2] <= ano2 and filme[2] >= ano1:
                        mostrar_filme_serie(filme)

        elif opcao == 4:
            genero = input("digite o genero dos filmes: ")
            for filme in filme_series:
                if genero == filme[1]:
                    mostrar_filme_serie(filme)
                    
        elif opcao == 5:
            titulo = input("digite o nome do filme: ")
            for filme in filme_series:
                if titulo == filme[0]:
                    mostrar_filme_serie(filme)
                    
if __name__ == "__main__":
    ler ([['vtromaniq','terror',2010,'netflix',],['vitormania','desenho', 2000,'prime video']])