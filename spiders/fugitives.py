# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags

def format_value(self, value):
	return "stupid shit is running {}".format(value)

class Fugitive(scrapy.Item):
	name = scrapy.Field(
		output_processor = MapCompose(unicode.strip),
		input_processor= MapCompose(remove_tags)
		)
	alias = scrapy.Field(input_processor = MapCompose(unicode.strip))
	violations = scrapy.Field(input_processor = MapCompose(format_value))
	race = scrapy.Field(input_processor = MapCompose(format_value))
	sex = scrapy.Field(input_processor = MapCompose(format_value))
	height = scrapy.Field(input_processor = MapCompose(format_value))
	weight = scrapy.Field(input_processor = MapCompose(format_value))
	hair_color = scrapy.Field(input_processor = MapCompose(format_value))
	eye_color = scrapy.Field(input_processor = MapCompose(format_value))
	dob = scrapy.Field(input_processor = MapCompose(format_value))
	last_known_addr = scrapy.Field(input_processor = MapCompose(format_value))
	ncic = scrapy.Field(input_processor = MapCompose(format_value))
	jurisdiction = scrapy.Field(input_processor = MapCompose(format_value))
	notes = scrapy.Field(input_processor = MapCompose(format_value))
