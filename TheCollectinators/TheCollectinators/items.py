# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# class TheCollectinatorsSystem(scrapy.Item):
#     system_name = scrapy.Field()
#     planets = scrapy.Field()

# class TheCollectinatorsPlanet(scrapy.Item):
#     system = scrapy.Field()
#     planet = scrapy.Field()
#     day = scrapy.Field()
#     hab_rank = scrapy.Field()
#     resources = scrapy.Field()
#     level = scrapy.Field()
#     details = scrapy.Field()


class TheCollectinatorsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    data = scrapy.Field()
    data_from_first_table = scrapy.Field()
    data_from_second_table = scrapy.Field()