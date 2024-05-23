import scrapy

class ArachnoBotSpider(scrapy.Spider):
    name = "Arachno_Bot"
    allowed_domains = ["inara.cz"]
    start_urls = ["https://inara.cz/starfield/starsystems-list/"]

    def parse(self, response):
        self.logger.info('Parsing main page: %s', response.url)
        
        # Select the table rows directly
        odd_rows = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr[@class="odd"]')
        even_rows = response.xpath('//*[@id="DataTables_Table_0"]/tbody/tr[@class="even"]')
        
        # Yield the odd rows
        for row in odd_rows:
            yield {
                'row_content': row.extract()
            }
        
        # Yield the even rows
        for row in even_rows:
            yield {
                'row_content': row.extract()
            }
