# Henrique - create.py
# Função para criar novo filme

def adicionar(filmes_series):
    filme_serie = []

    print("\nNovo Filme:\n")

    # Pegando os dados
    while True:
        titulo = input("Título: ")

        tem = False
        for item in filmes_series:
            if item[0].lower() == titulo.lower():
                tem = True
                break

        if tem:
            print("Esse filme/serie já existe...")
        else:
            break

    genero = input("Gênero: ")

    while True:
        try:
            ano = int(input("Ano de Lançamento: "))
            break
        except ValueError:
            print("Digite um número válido...")

    plataforma = input("Plataforma: ")

    # colocando os valores na linha
    filme_serie.append(titulo)
    filme_serie.append(genero)
    filme_serie.append(ano)
    filme_serie.append(plataforma)

    # Jogando na matriz
    filmes_series.append(filme_serie)

    print(f"\nNovo filme/serie adicionado com sucesso! ({filme_serie[0]} ({filme_serie[2]}) - {filme_serie[1]} - {filme_serie[3]})")

if __name__ == "__main__":
    adicionar([['teste', 'qualquer', 2025, 'sigaa']])