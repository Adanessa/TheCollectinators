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
        data_items = []
        for table in response.xpath('//table'):
            data = table.extract()

            # Clean up the data using BeautifulSoup
            soup = BeautifulSoup(data, 'html.parser')
            cleaned_data = soup.get_text()

            # Store cleaned data in data item
            data_item = TheCollectinatorsItem()
            data_item['data'] = cleaned_data
            data_items.append(data_item)

        # Extract data from column 1 and store in planets item
        planets_item = TheCollectinatorsItem()
        planets_data = [cell.xpath('.//text()').get() for cell in response.xpath('//table//tr/td[1]')]
        planets_item['planets'] = planets_data
        yield planets_item

        # Extract data from column 2 and store in resources item
        resources_item = TheCollectinatorsItem()
        resources_data = [cell.xpath('.//text()').get() for cell in response.xpath('//table//tr/td[2]')]
        resources_item['resources'] = resources_data
        yield resources_item

        return data_items
