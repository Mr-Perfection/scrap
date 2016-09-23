# -*- coding: utf-8 -*-
import re
import scrapy
from CraigslistScraper.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = [
    "http://sfbay.craigslist.org/search/vgm?"
    ]

    BASE_URL = 'http://sfbay.craigslist.org/'

    def parse(self, response):
        links = response.xpath('//a[@class="hdrlnk"]/@href').extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)

    def parse_attr(self, response):
        match = re.search(r"(\w+)\.html", response.url)
        if match:
            item_id = match.group(1)
            url = self.BASE_URL + "reply/sfb/vgm/" + item_id

            item = DmozItem()
            item["link"] = response.url

            return scrapy.Request(url, meta={'item': item}, callback=self.parse_contact)

    def parse_contact(self, response):
        item = response.meta['item']
        item["attr"] = "".join(response.xpath("//div[@class='anonemail']//text()").extract())
        return item