import scrapy


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['172.17.0.2:1337']
    start_urls = ['http://172.17.0.2:1337/']

    def parse(self, response):
        pass
