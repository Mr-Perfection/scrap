# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ScrapscrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Heading = Field()
    Content = Field()
    Source_Website = Field()
    pass
