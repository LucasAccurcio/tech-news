from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search_data = search_news(
        {"title": {"$regex": f"{title}", "$options": "i"}}
    )
    response = []
    for data in search_data:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# função para remover o 0 do dia < 10
def fix_day(day):
    if int(day) > 9:
        return day
    else:
        if(len(day) == 2):
            return day[1]


# função para verificar se a data está no formato correto
# e retornar a data por extenso
def check_date(date):
    list_date = date.split("-")

    if len(list_date) == 3:
        if (
            list_date[0].isdigit()
            and list_date[1].isdigit()
            and list_date[2].isdigit()
            and len(list_date[0]) == 4
            and len(list_date[1]) == 2
            and len(list_date[2]) == 2
        ):
            if (
                int(list_date[2]) <= 31
                and 0 < int(list_date[1]) <= 12
                and 1900 < int(list_date[0]) <= 2999
            ):
                meses = [
                    "janeiro",
                    "fevereiro",
                    "março",
                    "abril",
                    "maio",
                    "junho",
                    "julho",
                    "agosto",
                    "setembro",
                    "outubro",
                    "novembro",
                    "dezembro",
                ]
                list_date[2] = fix_day(list_date[2])
                return (
                    f"{list_date[2]}"
                    + f" de {meses[int(list_date[1]) - 1]}"
                    + f" de {list_date[0]}"
                )
            else:
                raise ValueError
        else:
            raise ValueError
    else:
        raise ValueError


# Requisito 7
def search_by_date(date):
    try:
        written_date = check_date(date)
        search_data = search_news(
            {"timestamp": {"$regex": f"{written_date}", "$options": "i"}}
        )
        response = []
        for data in search_data:
            response.append(
                (data["title"], data["url"]),
            )
        return response
    except ValueError:
        print("Data inválida")


search_by_date("20521-04-04")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
