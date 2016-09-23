# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# -*- coding: utf-8 -*-
import re
from scrapy.item import Item, Field

# item class included here
class DmozItem(Item):
    # define the fields for your item here like:
    link = Field()
    attr = Field()