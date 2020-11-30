## create script to crawl sites
## https://dev.to/fprime/how-to-create-a-web-crawler-from-scratch-in-python-2p46
## beautyful soup, http, https, cors, search for SO questions related
import requests    
import re    

class PyCrawler(object):    
    def __init__(self, starting_url):    
        self.starting_url = starting_url                       
        self.visited = set()    

    def start(self):    
        pass                 

if __name__ == "__main__":    
    crawler = PyCrawler()    
    crawler.start()
