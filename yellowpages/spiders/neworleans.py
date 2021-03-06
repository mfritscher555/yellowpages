import scrapy
import csv
import os.path
from lxml import html
from lxml import etree
import requests

class neworleansSpider(scrapy.Spider):
    name = "neworleans"

    start_urls = ['https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA',
    'https://www.yellowpages.com/search?search_terms=restaurants&geo_location_terms=New%20Orleans%2C%20LA&page=2']

    def parse(self, response):
        file_name = 'nolaoutputfile35.csv'
        #restaurant_info = response.css('div#main-content')
        restaurants = response.css('div.result')



        if os.path.exists(file_name):
            out_file = open(file_name, 'a')
            csv_writer = csv.writer(out_file)
        else:
            out_file = open(file_name, 'w')
            csv_writer = csv.writer(out_file)
            #csv_writer.writerow( ['name', 'phone_number', 'address', 'city_zip'])
            csv_writer.writerow( ['name'] )

    #    for restaurant in restaurant_info:
    #        name = restaurant
    #        phone_number = restaurant_info.css('div.phones.phone.primary::text').extract()
    #        city_zip = restaurant_info.css('div.locality::text').extract()
    #        csv_writer.writerow( [name, phone_number, address, city_zip] )
    #        #csv_writer.writerow( [name] )
    #        out_file.close()


        for restaurant in restaurants:
            name = restaurant.css('span::text').get()
            print(name)
            csv_writer.writerow( [ name ] )
            out_file.close()

#//*[@img class="csrp"]/@alt="Acme Oyster House"
#[type="submit"]
#//*[@type="submit"]

################# name = restaurant_info.css('a.business-name::text').get() - OUTPUT is only Smitty Seafood (first value only)
