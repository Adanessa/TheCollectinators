import scrapy


class ArachnoBotSpider(scrapy.Spider):
    name = "Arachno_Bot"
    allowed_domains = ["iara.cz"]
    start_urls = ["https://inara.cz/starfield/starsystems-list/"]

    def parse(self, response):
        pass
