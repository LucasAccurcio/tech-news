import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories,
)


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
    while exit is False:
        option = print_menu()

        if option == 0:
            try:
                quantidade = int(
                    input("Digite quantas notícias serão buscadas:")
                )
                noticias = get_tech_news(quantidade)
                print(noticias)
                exit = True
            except ValueError:
                print("Valor incorreto")
                exit = True

        elif option == 1:
            try:
                titulo = input("Digite o título:")
                noticias = search_by_title(titulo)
                print(noticias)
                exit = True
            except ValueError:
                print("Valor incorreto")
                exit = True

        elif option == 2:
            data = input("Digite a data no formato aaaa-mm-dd:")
            noticias = search_by_date(data)
            print(noticias)
            exit = True

        elif option == 3:
            try:
                tag = input("Digite a tag:")
                noticias = search_by_tag(tag)
                print(noticias)
                exit = True
            except ValueError:
                print("Valor incorreto")
                exit = True

        elif option == 4:
            try:
                categoria = input("Digite a categoria:")
                noticias = search_by_category(categoria)
                print(noticias)
                exit = True
            except ValueError:
                print("Valor incorreto")
                exit = True

        elif option == 5:
            noticias = top_5_news()
            print(noticias)
            exit = True

        elif option == 6:
            noticias = top_5_categories()
            print(noticias)
            exit = True

        elif option == 7:
            print("Encerrando script\n")
            exit = True

        else:
            sys.stderr.write("Opção inválida\n")
            exit = True


# analyzer_menu()
