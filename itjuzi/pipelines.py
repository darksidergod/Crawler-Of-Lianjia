# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request



class ItjuziPipeline(object):
	def __init__(self):
	self.conn = MySQLdb.connect(user='******', '*****', 'lianjia_beijing', 'localhost', charset="utf8", use_unicode=True)
	self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		try:
			self.cursor.execute("""INSERT INTO zufang (info, local,house_layout,house_square,house_orientation,district,floor,building_year,price_month,person_views,tags)  
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                       (item['info'], 
                        item['local'],
			item['house_layout'],
			item['house_square'],
			item['house_orientation'],
			item['district'],
			item['floor'],
			item['building_year'],
			item['price_month'],
			item['person_views'],
			item['tags'],)) 
			self.conn.commit()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		return item
