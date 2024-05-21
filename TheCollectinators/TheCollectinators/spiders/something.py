import scrapy


class SomethingSpider(scrapy.Spider):
    name = "something"
    allowed_domains = ["something.com"]
    start_urls = ["https://something.com"]

    def parse(self, response):
        pass
