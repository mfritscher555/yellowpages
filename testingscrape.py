import scrapy
import csv
import os.path
from lxml import html
import requests

class neworleansSpider(scrapy.Spider):
    name = "neworleans"

    start_urls = ['https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA']

    def parse(self, response):
        file_name = 'nolaoutputfile16.csv'
        restaurant_info = response.css('div.info-section.info-primary')

        if os.path.exists(file_name):
            out_file = open(file_name, 'a')
            csv_writer = csv.writer(out_file)
        else:
            out_file = open(file_name, 'w')
            csv_writer = csv.writer(out_file)
            csv_writer.writerow( ['name', 'phone_number'])

        for restaurant in restaurant_info:
            name = restaurant_info.css('span::text').extract()
            phone_number = restaurant_info.css('div.phones.phone.primary::text').extract()
            csv_writer.writerow( [name, phone_number] )
            out_file.close()
