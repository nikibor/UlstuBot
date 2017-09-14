import feedparser

def Parse_scv():
    data_parsed = feedparser.parse('https://news.yandex.ru/Ulyanovsk/index.rss')
    result = []
    for news in data_parsed['entries']:
        result.append(news['title'])
    return result
