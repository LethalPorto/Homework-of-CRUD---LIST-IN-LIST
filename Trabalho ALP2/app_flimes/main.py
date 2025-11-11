# main.py
import app_filmes
# Se não salvou nada ainda
filme_series = []

while True:
    print("\nMenu:\n")
    print("[1] Cadastrar filme/serie [2] Atualizar filme [3]Leitura dos filmes  [4]Deletar um filme")
    print("[0] Sair")

    opcao = input("\nOpção: ")

    if opcao == "1":
        app_flimes.adicionar(filme_series)
    elif opcao == "2":
        app_flimes.atualizar(filme_series)
    elif opcao == "3":
        app_flimes.ler(filme_series)
    elif opcao == "4":
        app_flimes.deletar(filme_series)
    elif opcao == "0":
        print("\nAdeus...")
        break
    else:
        print("Opção inválida!\n")

