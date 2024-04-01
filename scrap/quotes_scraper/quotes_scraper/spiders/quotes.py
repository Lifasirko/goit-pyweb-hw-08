import scrapy
from scrapy.crawler import CrawlerProcess
import shutil
import json
import os


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'tags': quote.css('div.tags a.tag::text').getall(),
                'author': quote.css('span small::text').get(),
                'quote': quote.css('span.text::text').get().strip('“”')
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


def convert_and_move_file(source, destination):
    with open(source, 'r', encoding='utf-8') as f:
        data = json.load(f)

    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    os.remove(source)  # Optionally, remove the source file after moving


if __name__ == "__main__":
    output_file = 'quotes.json'
    destination_path = r'C:\Users\MikeK\PycharmProjects\in_process\goit-pyweb-hw-08\db\quotes.json'

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': output_file,
    })

    process.crawl(QuotesSpider)
    process.start()  # The script will block here until the crawling is finished

    # Assuming the output file is in the current directory after the crawl
    source_path = os.path.join(os.getcwd(), output_file)
    convert_and_move_file(source_path, destination_path)
