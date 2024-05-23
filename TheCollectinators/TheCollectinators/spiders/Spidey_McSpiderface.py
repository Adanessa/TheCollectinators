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

# import scrapy
# from TheCollectinators.items import TheCollectinatorsItem

# class SpideyMcSpiderfaceSpider(scrapy.Spider):
#     name = "spidey_mcspiderface"
#     allowed_domains = ["starfieldwiki.net"]
#     start_urls = ["https://starfieldwiki.net/wiki/Category:Starfield-Planets"]

#     # Initialize a set to store unique titles
#     unique_titles = set()

#     def parse(self, response):
#         self.logger.info(f"Parsing page: {response.url}")

#         # Extract links to planet pages
#         planet_links = response.xpath('//div[@id="mw-pages"]//a[@title]/@href').getall()
#         for link in planet_links:
#             self.logger.info(f"Found planet link: {link}")
#             yield response.follow(link, self.parse_planet_page)

#         # Follow pagination link if present
#         next_page = response.xpath('//a[contains(text(), "next page")]/@href').get()
#         if next_page:
#             next_page = response.urljoin(next_page)
#             self.logger.info(f"Found next page link: {next_page}")
#             yield scrapy.Request(url=next_page, callback=self.parse)
#         else:
#             self.logger.info("No next page link found")

#     def parse_planet_page(self, response):
#         title = response.css('title::text').get()
#         # Add the title to the set of unique titles
#         self.unique_titles.add(title)

#         # Extract data from the first table
#         for row in response.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr'):
#             item = TheCollectinatorsItem()
#             item['title'] = title
#             item['link'] = response.url
#             item['data_from_first_table'] = row.xpath('.//text()').getall()
#             yield item

#         # Extract data from the second table
#         for row in response.xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr'):
#             item = TheCollectinatorsItem()
#             item['title'] = title
#             item['link'] = response.url
#             item['data_from_second_table'] = row.xpath('.//text()').getall()
#             yield item

#         # Print the count of unique titles periodically
#         self.logger.info(f"Unique titles count: {len(self.unique_titles)}")

#     # Optionally, log the final count when the spider closes
#     def closed(self, reason):
#         self.logger.info(f"Final unique titles count: {len(self.unique_titles)}")
# collect links with starfield link tier
# <a class="starfield-link-tier-1"


import scrapy
from bs4 import BeautifulSoup
import re
from TheCollectinators.items import TheCollectinatorsItem

class SpideyMcSpiderfaceSpider(scrapy.Spider):
    name = "spidey_mcspiderface"
    allowed_domains = ["hardcoregamer.com"]
    start_urls = ["https://hardcoregamer.com/db/starfield-all-resources-and-locations/468241/#all-inorganic-resources-in-starfield"]

    def parse(self, response):
        self.logger.info(f"Parsing page: {response.url}")

        # Locate the section by h2 id
        section = response.xpath('//h2[@id="all-inorganic-resources-in-starfield"]/following-sibling::div[@class="table-container"][1]')
        
        # Collect all links within that section
        links = section.xpath('.//a[contains(@class, "starfield-link-tier")]/@href').getall()
        for link in links:
            full_link = response.urljoin(link)
            self.logger.info(f"Found link: {full_link}")
            yield scrapy.Request(url=full_link, callback=self.parse_resource_page)

    def parse_resource_page(self, response):
        self.logger.info(f"Successfully traversed to: {response.url}")

        # Extract data from the specified table
        raw_table_data = response.xpath('//*[@id="article-body"]/div[1]/div[2]').get()

        # Clean up the data
        cleaned_data = self.clean_html_data(raw_table_data)

        # Populate the item
        item = TheCollectinatorsItem()
        item['title'] = response.css('title::text').get()
        item['link'] = response.url
        item['data'] = cleaned_data

        yield item

    def clean_html_data(self, raw_data):
        # Remove newlines and extra whitespace
        data = re.sub(r'\s+', ' ', raw_data)
        # Parse the HTML and remove tags
        soup = BeautifulSoup(data, 'html.parser')
        clean_text = soup.get_text(separator=' ', strip=True)
        return clean_text
