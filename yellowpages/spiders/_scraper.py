import scrapy
import csv
import os.path
from lxml import html
from lxml import etree
import requests

class neworleansSpider(scrapy.Spider):
    name = "nola"
    start_urls = ['https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA',
    'https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA&s=default&page=2']
    #start = 0
    #rest_ids = []

    def parse(self, response):
        file_name = 'nolaoutputfile.csv'
        #restaurant_info = response.css('div#main-content')
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
            phone_number = restaurant.css('div.phones.phone.primary::text').get()
            address = restaurant.css('div.street-address::text').get()
            city_zip = restaurant.css('div.locality::text').get()
            print(name, phone_number, address, city_zip)
            csv_writer.writerow( [ name, phone_number, address, city_zip ] )


        out_file.close()
