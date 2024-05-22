import requests
import scrapy
from TheCollectinators.items import TheCollectinatorsItem

class SpideyMcSpiderfaceSpider(scrapy.Spider):
    name = "spidey_mcspiderface"
    allowed_domains = ["starfieldwiki.net/wiki/Home"]
    start_urls = ["https://starfieldwiki.net/wiki/Home"]

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            item = TheCollectinatorsItem()
            item['title'] = response.css('title::text').get()
            item['link'] = response.urljoin(link)
            yield item
