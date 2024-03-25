import json
from db.models import Author, Quote


def load_authors():
    with open('db/authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author.objects(fullname=author_data['fullname']).first()
            if not author:
                author = Author(**author_data)
                author.save()
                print(f'Автор {author.fullname} доданий.')


def load_quotes():
    with open('db/qoutes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author = Author.objects(fullname=quote_data['author']).first()
            if author:
                # Оновлення посилання на автора у даних цитати
                quote_data['author'] = author
                # Пошук цитати за текстом цитати і автором
                quote = Quote.objects(quote=quote_data['quote'], author=author).first()
                # Якщо цитата не знайдена, створіть нову
                if not quote:
                    quote = Quote(**quote_data)
                    quote.save()
                    print(f'Цитата додана: {quote.quote}')
                else:
                    print(f'Цитата вже існує: {quote.quote}')
