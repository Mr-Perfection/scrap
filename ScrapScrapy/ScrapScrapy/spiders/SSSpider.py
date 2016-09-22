from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from ScrapScrapy.items import ScrapscrapyItem

class ScrapscrapySpider(BaseSpider) :
    name = "ss"
    allowed_domains = ["scrapy.org"]
    start_urls = ["http://scrapy.org"]
    def parse(self, response) :
        sel = Selector (response)
        item = ScrapscrapyItem()
        item['Heading'] = sel.xpath('/html/body/div[2]/div/div[1]/div/div[1]/p[1]/text()').extract()
        item['Content'] = sel.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/p/span/text()').extract()
        item['Source_Website'] = "http://scrapy.org/"
        return item