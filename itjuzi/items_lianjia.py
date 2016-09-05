# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	info = scrapy.Field()
	local = scrapy.Field()
	house_layout = scrapy.Field()
	house_square = scrapy.Field()
	house_orientation = scrapy.Field()
	district = scrapy.Field()
	floor = scrapy.Field()
	building_year = scrapy.Field()
	price_month = scrapy.Field()
	person_views = scrapy.Field()
	tags = scrapy.Field()
