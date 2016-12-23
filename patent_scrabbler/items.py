# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PatentScrabblerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    patent_number = scrapy.Field()
    title = scrapy.Field()
    filing_date = scrapy.Field()
    priority_date = scrapy.Field()
    publish_date = scrapy.Field()
    abstract = scrapy.Field()
    current_assignee = scrapy.Field()
    num_forward_refs = scrapy.Field()
    url = scrapy.Field()
