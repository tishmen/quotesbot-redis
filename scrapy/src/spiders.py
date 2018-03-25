'''quotes.py'''

from datetime import datetime

from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from items import QuoteLoader


class QuotesSpider(RedisSpider):

    '''Quotes spider.'''

    name = 'quotes'
    redis_key = 'quotes:start_urls'

    def _load_item(self, quote):
        '''Load quote item.'''
        loader = QuoteLoader(selector=quote)
        loader.add_xpath('text', './span[@class="text"]/text()')
        loader.add_xpath('author', './/small[@class="author"]/text()')
        loader.add_xpath('tags', './/div[@class="tags"]/a[@class="tag"]/text()')
        loader.add_value('timestamp', datetime.utcnow().isoformat())
        return loader.load_item()

    def parse(self, response):
        '''Parse quote and return to engine.'''
        for quote in response.xpath('//div[@class="quote"]'):
            yield self._load_item(quote)
        next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url:
            yield Request(response.urljoin(next_url))
