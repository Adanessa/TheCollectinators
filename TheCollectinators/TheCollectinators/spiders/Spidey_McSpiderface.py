import scrapy


class SpideyMcSpiderface(scrapy.Spider):
    name = "Link_Crawler"
    allowed_domains = ["something.com"]
    start_urls = ["https://something.com"]

    def parse(self, response):
        pass
