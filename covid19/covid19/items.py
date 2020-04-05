# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    countries = scrapy.Field()
    total_cases = scrapy.Field()
    new_cases = scrapy.Field()
    total_recovered = scrapy.Field()
    active_cases = scrapy.Field()
    total_cases_per_million = scrapy.Field()
    new_deaths = scrapy.Field()
    death_per_million = scrapy.Field()
    total_deaths = scrapy.Field()
