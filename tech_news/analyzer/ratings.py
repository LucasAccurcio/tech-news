import pymongo
from tech_news.database import get_collection


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
    collection = get_collection()
    data_list = collection.aggregate(
        [
            {
                "$group": {
                    "_id": "$category",
                    "total": {"$sum": 1}
                },
            },
            {
                "$sort": {"total": -1},
            },
            {
                "$limit": 5
            },
        ]
    )

    response = []
    for data in data_list:
        response.append(data["_id"])

    return response
