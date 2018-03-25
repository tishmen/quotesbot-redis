'''settings.py'''


BOT_NAME = 'quotesbot'

REDIS_HOST = 'redis'
REDIS_PORT = 6379

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
