from func import adicionar_gasto, listar_gastos, validar_data, validar_valor

def menu():
    while True:
        print("GESTOR DE GASTOS PESSOAL")
        print("1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            data = input("Data (DD/MM/AAAA): ")
            if not validar_data(data):
                print("Data inválida")
                continue

            categoria = input("Categoria: ")
            valor = input("Valor R$: ")

            if not validar_valor(valor):
                print("Valor inválido")
                continue

            adicionar_gasto(data, categoria, valor)

        elif opcao == "2":
            listar_gastos()

        elif opcao == "3":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu()
