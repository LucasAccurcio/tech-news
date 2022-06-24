def print_menu():
    texto = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair."
    )
    try:
        option = int(input(texto))
        return option
    except ValueError:
        print("Opção inválida!\n\n")


# Requisito 12
def analyzer_menu():
    exit = False
    while (exit is False):
        option = print_menu()
        if option == 0:
            print("Digite quantas notícias serão buscadas:")
        elif option == 1:
            print("Digite o título:")
        elif option == 2:
            print("Digite a data no formato aaaa-mm-dd:")
        elif option == 3:
            print("Digite a tag:")
        elif option == 4:
            print("Digite a categoria:")
        elif option == 5:
            print("Listar top 5 notícias:")
        elif option == 6:
            print("Listar top 5 categorias:")
        elif option == 7:
            exit = True
        else:
            exit = True
