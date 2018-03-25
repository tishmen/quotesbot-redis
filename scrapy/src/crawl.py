'''run.py'''

import scrapy

from scrapy.crawler import CrawlerProcess

from spiders import QuotesSpider


settings = {
    'REDIS_HOST': 'redis',
    'SCHEDULER': 'scrapy_redis.scheduler.Scheduler',
    'DUPEFILTER_CLASS': 'scrapy_redis.dupefilter.RFPDupeFilter',
    'ITEM_PIPELINES': {
        'scrapy_redis.pipelines.RedisPipeline': 300
    }
}


if __name__ == '__main__':
    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider)
    process.start()
