import scrapy
from bs4 import BeautifulSoup
from TheCollectinators.items import TheCollectinatorsItem

class SpideyMcSpiderfaceSpider(scrapy.Spider):
    name = "spidey_mcspiderface"
    allowed_domains = ["hardcoregamer.com"]
    start_urls = ["https://hardcoregamer.com/db/starfield-all-locations-systems-planets-moons/464902/#all-systems-in-starfield"]

    def parse(self, response):
        self.logger.info('Parsing main page: %s', response.url)

        # Locate all tables on the page
        tables = response.xpath('//table')

        # Set to store unique links
        unique_links = set()

        # Iterate over each table
        for table in tables:
            # Extract links from the 4th column of the table
            links = table.xpath('.//tr/td[4]//a')
            for link in links:
                # Extract href and text of the link
                href = link.xpath('./@href').get()
                text = link.xpath('./text()').get()

                # Check if the link is not a duplicate
                if href not in unique_links:
                    unique_links.add(href)

                    # Save text of the link in system item
                    system_item = {
                        'text': text,
                        'link': href
                    }
                    yield system_item

                    # Follow the link to collect data
                    yield response.follow(href, callback=self.parse_data)

    def parse_data(self, response):
        self.logger.info('Parsing data page: %s', response.url)

        # Extract data from all tables on the page
        planets = []
        resources = []

        for table in response.xpath('//table'):
            rows = table.xpath('.//tr')

            for row in rows:
                planet = row.xpath('./td[1]').get()
                resource = row.xpath('./td[2]').get()

                if planet:
                    planet_text = self.clean_text(planet)
                    planets.append(planet_text)
                
                if resource:
                    resource_text = self.clean_text(resource)
                    resources.append(resource_text)

        item = TheCollectinatorsItem()
        item['planets'] = planets
        item['resource'] = resources
        yield item

    def clean_text(self, text):
        # Function to clean up text by removing newline characters and extra spaces
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text(separator=' ').strip()
