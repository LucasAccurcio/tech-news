from tech_news.database import search_news
from datetime import datetime


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
def remove_zero_from_day(day):
    if int(day) > 9:
        return day
    else:
        if len(day) == 2:
            return day[1]


# função para retornar a data por extenso
def write_date(date):
    list_date = date.split("-")

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
    list_date[2] = remove_zero_from_day(list_date[2])
    return (
        f"{list_date[2]}"
        + f" de {meses[int(list_date[1]) - 1]}"
        + f" de {list_date[0]}"
    )


# Requisito 7
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
        written_date = write_date(date)
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
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search_data = search_news(
        {"tags": {"$elemMatch": {"$regex": f"{tag}", "$options": "i"}}}
    )
    response = []
    for data in search_data:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# Requisito 9
def search_by_category(category):
    search_data = search_news(
        {"category": {"$regex": f"{category}", "$options": "i"}}
    )
    response = []
    for data in search_data:
        response.append(
            (data["title"], data["url"]),
        )
    return response
