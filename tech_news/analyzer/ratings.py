from typing import Counter
import pymongo
from tech_news.database import get_collection, find_news


# Requisito 10
def top_5_news():
    collection = get_collection()
    data_sorted = list(
        collection.find({}, {"title": 1, "url": 1, "_id": False})
        .sort(
            [
                ("comments_count", pymongo.DESCENDING),
                ("title", pymongo.ASCENDING),
            ]
        )
        .limit(5)
    )

    response = []

    for data in data_sorted:
        response.append(
            (data["title"], data["url"]),
        )
    return response


# Requisito 11
def top_5_categories():
    data = find_news()
    lista = []
    for d in data:
        lista.append(d["category"])

    categories = Counter(lista).most_common()
    response = []

    counter = 0
    for category in categories:
        if counter == 5:
            break
        response.append(category[0])
        counter += 1
    print(response)
    return response
