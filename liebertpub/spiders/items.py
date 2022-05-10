from scrapy.spiders import XMLFeedSpider
from liebertpub.items import LiebertpubItem
# from scrapy_splash import SplashRequest

class ItemsSpider(XMLFeedSpider):
    name = 'items'
    allowed_domains = ['liebertpub.com']
    start_urls = ['https://www.liebertpub.com/action/showFeed?ui=0&mi=3dss5k&ai=sy&jc=fpd&type=etoc&feed=rss']
    iterator = 'html' # you can change this; see the docs
    itertag = 'item' # change it accordingly
    

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url, self.parse_node, args={'wait': 0.5})
    
    
    def parse_node(self, response, selector):
        item = LiebertpubItem()
        
        # item['title'] = selector.xpath('title/text()').get()
        # item['link'] = selector.xpath('link/@href').get()
        # item['creator'] = selector.xpath("dc:creator/text()").get()
        # item['date'] = selector.xpath("dc:date/text()").get()
        # return item
        print(selector.xpath('//title/text()').get())
        print(selector.xpath('//link/text()').get())

