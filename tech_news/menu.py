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


def get_news_by_quantity():
    try:
        quantidade = int(input("Digite quantas notícias serão buscadas:"))
        noticias = get_tech_news(quantidade)
        print(noticias)
    except ValueError:
        print("Valor incorreto")
    return False


def get_news_by_tittle():
    try:
        titulo = input("Digite o título:")
        noticias = search_by_title(titulo)
        print(noticias)
    except ValueError:
        print("Valor incorreto")
    return False


def get_news_by_data():
    data = input("Digite a data no formato aaaa-mm-dd:")
    noticias = search_by_date(data)
    print(noticias)
    return False


def get_news_by_tag():
    try:
        tag = input("Digite a tag:")
        noticias = search_by_tag(tag)
        print(noticias)
    except ValueError:
        print("Valor incorreto")
    return False


def get_news_by_category():
    try:
        categoria = input("Digite a categoria:")
        noticias = search_by_category(categoria)
        print(noticias)
    except ValueError:
        print("Valor incorreto")
    return False


def get_top_five_news():
    noticias = top_5_news()
    print(noticias)
    return False


def get_top_five_categories():
    noticias = top_5_categories()
    print(noticias)
    return False


def exit():
    print("Encerrando script\n")
    return True


# Requisito 12
def analyzer_menu():
    texto_menu = (
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
    stop = False
    while (stop is False):
        try:
            option = int(input(texto_menu))
            if option > 7:
                sys.stderr.write("Opção inválida\n")
                stop = False
            else:
                dict_functions = {
                    0: get_news_by_quantity,
                    1: get_news_by_tittle,
                    2: get_news_by_data,
                    3: get_news_by_tag,
                    4: get_news_by_category,
                    5: get_top_five_news,
                    6: get_top_five_categories,
                    7: exit,
                }
                stop = dict_functions.get(option)()
        except ValueError:
            print("Opção inválida!\n")
            stop = True


analyzer_menu()
