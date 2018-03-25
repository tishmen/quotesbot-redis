'''items.py'''

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity


class QuoteItem(Item):

    '''Quote item.'''

    text = Field()
    author = Field()
    tags = Field()
    timestamp = Field()


class QuoteLoader(ItemLoader):

    '''Quote item loader.'''

    default_item_class = QuoteItem
    default_output_processor = TakeFirst()
    tags_out = Identity()
