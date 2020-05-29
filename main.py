import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

import datetime

class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://inshorts.com/en/read').text
        self.keywords = keywords

    def parser_search(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.findAll("a", {"class": "clickable"})
        self.saved_links = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.saved_links.append(link)
    def store(self):
        client= MongoClient('localhost',27017)
        result_db =client.scrapitbro
        collection=result_db.test_collection
        for link in self.saved_links:
            result_db.test_collection.insert_one({link.text :str(link)})
                    
                   
       


    
s = Scraper(['GDP','modi','PM','donated','coronavirus','Covid','Coronavirus','covid','Bollywood'])
s.parser_search()
#print(s.saved_links)
s.store()
