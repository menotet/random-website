import webbrowser
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
import requests
import random
import string
import argparse

from asset.app_domain_list import app_domain_list

class Random_website():
    def __init__(self):
        self.domain_list # need domain list file
    
    def create_url_log(self, url):
        with open("url_log.txt", "a") as f:
            f.truncate(0)
            f.write(str(url))
            f.write("\n")

    def create_url(self, minnum, maxnum):
        n = random.randint(minnum, maxnum) #select url length.
        random_list = [random.choice(string.ascii_lowercase + string.digits) for n in range(n)]
        random_url = "http://" + "".join(random_list) + "." + random.choice(self.domain_list) # shape url.
        return random_url

    def open_random_website(self, minnum, maxnum):
        url_list = []
        opened_url = False

        while (not opened_url):
            try:          
                url = self.create_url(minnum, maxnum)
                print("try ", url)
                url_list.append(url)
                res = requests.head(url, timeout = 3.5)
                res.raise_for_status()
                if res.status_code == 200:
                    webbrowser.open(res.url) # open the url.
                    opened_url = True
                    return res.url, url_list
            except:
                continue

if __name__ == "main":
    random_website = Random_website
    random_website.domain_list = app_domain_list
    open_url = random_website.open_random_website(4, 60)
    random_website.create_url_log(open_url[0])
    print("open ", open_url[0])