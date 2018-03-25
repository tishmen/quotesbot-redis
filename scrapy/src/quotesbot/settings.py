'''settings.py'''


BOT_NAME = 'quotesbot'
SPIDER_MODULES = ['quotesbot.spiders']

REDIS_HOST = 'redis'
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
