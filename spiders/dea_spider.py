import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from fugitives import Fugitive
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst

def clean_text(text):
	return ' '.join(i.strip().rstrip() for i in text if i.strip())

class DEASpider(CrawlSpider):
	"""simple data extractor for DEA fugitives"""
	name = "DEA"
	start_urls = ['https://www.dea.gov/fugitives/all?\
			field_fugitive_fname_value=&field_fugitive_lname_value=&\
			field_fugitive_sex_value=All&organization=All&\
			sort_bef_combine=created%20DESC&sort_by=created&\
			sort_order=DESC&page=1']
	allowed_domains = ['dea.gov']
	#for x in xrange(1,2):
	'''
	1-3 for testing purposes.
	There are 73 pages, I can get this number with one request of the main page
	OR I can make this a while there is a responce to go get more pages
	'''
	#	start_urls.append(
	#		'https://www.dea.gov/fugitives/all?\
	#		field_fugitive_fname_value=&field_fugitive_lname_value=&\
	#		field_fugitive_sex_value=All&organization=All&\
	#		sort_bef_combine=created%20DESC&sort_by=created&\
	#		sort_order=DESC&page={}'.format(x)
	#	)
	rules = (Rule (LinkExtractor(allow=('/fugitives/'),)
		,callback="parse_items"),
	)

	def parse(self, response):
		yield Request(response.url, callback=self.get_items)

	def parse_items(self, response):
		my_body = re.sub(r'\\+[n]', '', '{}'.format(response.body))
		my_body = re.sub(r's{2,}', '', '{}'.format(my_body))
		response.body.replace(response.body, my_body)
		fugitive = Fugitive()

		fugitive["name"] = clean_text(response.xpath('.//article/div[1]/div/div[2]/h1/text()').extract())
		fugitive["alias"] = clean_text(response.xpath('.//div[@class="field field--aka"]/text()').extract())
		fugitive["violations"] = clean_text(response.xpath('.//div[@class="field field--violations"]/div/text()').extract())
		fugitive["race"] = response.xpath('.//table/tbody/tr[1]/td[2]/text()').extract()
		fugitive["sex"] = response.xpath('.//table/tbody/tr[2]/td[2]/text()').extract()
		fugitive["height"] = clean_text(response.xpath('.//table/tbody/tr[3]/td[2]/text()').extract())
		fugitive["weight"] = clean_text(response.xpath('.//table/tbody/tr[4]/td[2]/text()').extract())
		fugitive["hair_color"] = response.xpath('.//table/tbody/tr[5]/td[2]/text()').extract()
		fugitive["eye_color"] = clean_text(response.xpath('.//table/tbody/tr[6]/td[2]/text()').extract())
		fugitive["dob"] = clean_text(response.xpath('.//table/tbody/tr[7]/td[2]/text()').extract())
		fugitive["last_known_addr"] = clean_text(response.xpath('.//table/tbody/tr[8]/td[2]/text()').extract())
		fugitive["ncic"] = clean_text(response.xpath('.//table/tbody/tr[9]/td[2]/text()').extract())
		fugitive["jurisdiction"] = clean_text(response.xpath('.//table/tbody/tr[10]/td[2]/text()').extract())
		fugitive["notes"] = clean_text(response.xpath('.//table/tbody/tr[11]/td[2]/div/text()').extract())

		yield fugitive

	def get_items(self, response):
		for href in response.xpath('.//div/h3/a/@href').getall():
			yield scrapy.Request(response.urljoin('https://www.dea.gov{}'.format(href)), callback=self.parse_items)



