import requests
import time
import parsel
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)

    url_news = selector.css(".cs-overlay-link::attr(href)").getall()
    return url_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)

    next_page = selector.css(".next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)

    title = selector.css("h1.entry-title::text").get()
    url = selector.xpath("//link[@rel='canonical']/@href").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    comments_count = selector.css("div.comment-respond").getall()
    summary = selector.css("div.entry-content p").getall()
    # https://pt.stackoverflow.com/questions/192176/como-remover-tags-em-um-texto-em-python
    summary = re.sub('<[^>]+?>', '', summary[0])
    summary = re.sub('&amp;', '&', summary)
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    news_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments_count),
        "summary": summary,
        "tags": tags,
        "category": category
    }

    return news_data


# Requisito 5
def get_tech_news(amount):
    indice = 0
    URL_BASE = "https://blog.betrybe.com"
    data = []
    while indice < amount:
        get_page_content = fetch(URL_BASE)
        get_url_news = scrape_novidades(get_page_content)
        for url in get_url_news:
            news_content = fetch(url)
            data.append(scrape_noticia(news_content))
            indice += 1
            if (indice == amount):
                break
        URL_BASE = scrape_next_page_link(get_page_content)
    create_news(data)
    return data


get_tech_news(5)
