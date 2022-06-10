import scrapy
import csv
import os
from lxml import html
from lxml import etree
import requests

class tester2Spider(scrapy.Spider):
    name = "tester2"

    start_urls = ['https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA',
    'https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA&page=2']

    def parse(self, response):
        file_name = 'nolaoutputfile39.csv'
        # restaurant_info = response.css('div#main-content')
        restaurants = response.css('div.result')

        if os.path.exists(file_name):
            out_file = open(file_name, 'a')
            csv_writer = csv.writer(out_file)
        else:
            out_file = open(file_name, 'w')
            csv_writer = csv.writer(out_file)
            csv_writer.writerow( ['name', 'phone_number', 'address', 'city_zip'])


        for restaurant in restaurants:
            name = restaurant.css('span::text').get()
            print(name)
            csv_writer.writerow( [ name ] )

        out_file.close()
