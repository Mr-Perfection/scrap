from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from RecursiveScraper.items import RecursivescraperItem

class   RecursiveScraperSpider(CrawlSpider) :
    name = "rs"
    allowed_domains = ["cse.iitd.ernet.in"]
    start_urls = ["http://www.cse.iitd.ernet.in/~naveen"]
    rules = (
        Rule(SgmlLinkExtractor(allow=("cse\.iltd\.ernet\.in/\~naveen/.*", )), callback='parse_item', follow= True),
        )
    
    def   parse_item(self, response) :
        sel = Selector(response)
        item = RecursivescraperItem()
        item['URL'] = response.request.url
        item['content'] = sel.xpath('/html/body/table/tbody/tr[3]/td[1]/text()[1]').extract()
        return item
        
    
    