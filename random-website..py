import webbrowser
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
import requests
import random
import string
from asset.domain_list import domain_list

def create_url(minnum, maxnum):
    n = random.randint(minnum, maxnum) #select url length
    random_list = [random.choice(string.ascii_lowercase + string.digits) for n in range(n)]
    random_url = "http://" + "".join(random_list) + "." + random.choice(domain_list) # shape url
    return random_url

def open_random_website(minnum, maxnum):
    opened_url = False

    while (not opened_url):
        try:          
            url = create_url(minnum, maxnum)
            print("try ", url)
            res = requests.head(url)
            res.raise_for_status()
            if res.status_code == 200:
                webbrowser.open(res.url) # open the url
                opened_url = True
                return res.url
        except:
            continue

open_url = open_random_website(1, 10)
print("open ", open_url)