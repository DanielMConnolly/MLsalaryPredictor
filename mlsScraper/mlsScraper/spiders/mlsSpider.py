import scrapy
import sys
sys.path.insert(1, '/home/daniel/anaconda3/lib/python3.6/site-packages' )
import logging
import numpy as np

class spyder1(scrapy.Spider):
        name='Wikipedia'
        start_urls=['https://www.mlssoccer.com/players?site_path=players&name=Justin+Hughes&op=Search&form_build_id=form-dXL9K8qWV3QOXkn5q5aIjTFaQAvnogU-wdD3dusmDVQ&form_id=mp7_club_player_search_form']

        def parse(self, response):
                ageString=str( response.css('span.age').extract())
                age=ageString[ageString.find('>')+1:ageString.find('>')+3]
                print age
                print "Daniel"



