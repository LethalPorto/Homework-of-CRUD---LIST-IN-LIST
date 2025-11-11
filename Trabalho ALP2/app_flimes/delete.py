def deletar(filmes_series):
    while True:
        print(f"\nFilmes já adicionados: {filmes_series}")
        resp = input("Coloque o título do filme que se deseja deletar algo, [1]sair: ").lower()

        if resp == "1":
            print("Voltando ao menu...")
            break

        # Procurar o filme pelo título
        encontrado = False
        for item in filmes_series:
            if item[0].lower() == resp:
                encontrado = True

                print(f"\nFilme encontrado: {resp}")
                print("O que você quer deletar?")
                TGAP = int(input("(1) Título  (2) Gênero  (3) Ano  (4) Plataforma"))

                if TGAP == 1:
                    filmes_series.remove(item)
                elif TGAP == 2:
                    item[1] = ""
                elif TGAP == 3:
                    item[2] = ""
                elif TGAP == 4:
                    item[3] = ""


                print("\nAlteração feita!")
                break

        if not encontrado:
            print("Título não encontrado.")


