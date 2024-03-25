import json
import re

import redis

from db.connect import connect
from db.load_data import load_authors, load_quotes
from db.models import Quote, Author

# Підключення до Redis
r = redis.Redis(host='localhost', port=6379, db=0)
connect = connect


def get_cached_result(key):
    print("Юзаєм кеш")
    if r.exists(key):
        return json.loads(r.get(key))
    return None


def cache_result(key, result):
    print("Кешуємо результат")
    r.set(key, json.dumps(result), ex=3600)  # Зберігати результат на 1 годину


# def search_by_author(name):
#     # Знайти автора за ім'ям
#     author = Author.objects(fullname=name).first()
#     if not author:
#         print("Автор не знайдений.")
#         return []
#
#     # Знайти цитати за об'єктом автора
#     quotes = Quote.objects(author=author)
#     quotes_list = [quote.quote for quote in quotes]
#     return quotes_list

def search_by_author_partial(name_partial):
    regex = re.compile('^{}.*'.format(re.escape(name_partial)), re.IGNORECASE)
    authors = Author.objects(fullname=regex)
    quotes_list = []
    for author in authors:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            quotes_list.append(quote.quote)
    return quotes_list


def search_and_cache_by_author_partial(name_partial):
    cache_key = f'author:{name_partial}'
    cached_result = get_cached_result(cache_key)
    if cached_result is not None:
        return cached_result
    result = search_by_author_partial(name_partial)
    cache_result(cache_key, result)
    return result


# def search_by_tag(tag):
#     cache_key = f'tag:{tag}'
#     if r.exists(cache_key):
#         print("Використовуємо кеш.")
#         return json.loads(r.get(cache_key))
#     else:
#         quotes = Quote.objects(tags=tag)
#         quotes_list = [quote.quote for quote in quotes]
#         r.set(cache_key, json.dumps(quotes_list), ex=120)
#         return quotes_list

def search_by_tag_partial(tag_partial):
    regex = re.compile('^{}.*'.format(re.escape(tag_partial)), re.IGNORECASE)
    quotes = Quote.objects(tags=regex)
    return [quote.quote for quote in quotes]


def search_and_cache_by_tag_partial(tag_partial):
    cache_key = f'tag:{tag_partial}'
    cached_result = get_cached_result(cache_key)
    if cached_result is not None:
        return cached_result
    result = search_by_tag_partial(tag_partial)
    cache_result(cache_key, result)
    return result


if __name__ == "__main__":
    load_authors()
    load_quotes()
    while True:
        command = input("Введіть команду: ")
        if command == "exit":
            break
        cmd, value = command.split(":")
        if cmd == "name":
            quotes = search_and_cache_by_author_partial(value.strip())
            for quote in quotes:
                print(quote)
        elif cmd == "tag":
            quotes = search_and_cache_by_tag_partial(value.strip())
            for quote in quotes:
                print(quote)

"""
docker run --name {some-redis} -d redis
docker run --name goit-pyweb-hw-08-redis -p 6379:6379 -d redis
name: Steve Martin
tag:life
tags:life,live
name:st
tag:li
"""
