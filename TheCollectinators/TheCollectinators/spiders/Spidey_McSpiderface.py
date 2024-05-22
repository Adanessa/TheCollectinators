import requests
# import scrapy
# from TheCollectinators.items import TheCollectinatorsItem

# class SpideyMcSpiderfaceSpider(scrapy.Spider):
#     name = "spidey_mcspiderface"
#     allowed_domains = ["starfieldwiki.net"]
#     start_urls = ["https://starfieldwiki.net/wiki/Home"]

#     def parse(self, response):
#         for link in response.css('a::attr(href)').getall():
#             if "fauna" in link or "flora" in link:
#                 item = TheCollectinatorsItem()
#                 item['title'] = response.css('title::text').get()
#                 item['link'] = response.urljoin(link)
#                 yield item

import scrapy
from TheCollectinators.items import TheCollectinatorsItem

class SpideyMcSpiderfaceSpider(scrapy.Spider):
    name = "spidey_mcspiderface"
    allowed_domains = ["starfieldwiki.net"]
    start_urls = ["https://starfieldwiki.net/wiki/Starfield:Flora"]

    def parse(self, response):
        # Extract links from the current page
        for link in response.css('.mw-parser-output a::attr(href)').getall():
            yield response.follow(link, self.parse_flora_page)

    def parse_flora_page(self, response):
        # Extract data from the specific element
        for row in response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr'):
            item = TheCollectinatorsItem()
            item['title'] = response.css('title::text').get()
            item['link'] = response.url
            # Extract data from the table rows as needed
            item['data'] = row.xpath('.//text()').getall()
            yield item
