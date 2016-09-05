# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	house_code = scrapy.Field()
	price_total = scrapy.Field()
	ctime = scrapy.Field()
	title = scrapy.Field()
	frame_hall_num = scrapy.Field()
	tags = scrapy.Field()
	house_area = scrapy.Field()
	community_id = scrapy.Field()
	community_name = scrapy.Field()
	is_two_five = scrapy.Field()
	frame_bedroom_num = scrapy.Field()
