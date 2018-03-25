'''run.py'''

import scrapy

from scrapy.crawler import CrawlerProcess

from spiders import QuotesSpider


def main():
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()


if __name__ == '__main__':
    main()
