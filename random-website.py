import webbrowser
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout
import requests
import random
import string
from asset.domain_list import domain_list

def create_url_log(url_list):
    with open("url_log.txt", "a") as f:
        f.truncate(0)
        f.write(str(url_list))
        f.write("\n")

def create_url(minnum, maxnum):
    n = random.randint(minnum, maxnum) #select url length
    random_list = [random.choice(string.ascii_lowercase + string.digits) for n in range(n)]
    random_url = "http://" + "".join(random_list) + "." + random.choice(domain_list) # shape url
    return random_url

def open_random_website(minnum, maxnum):
    url_list = []
    opened_url = False

    while (not opened_url):
        try:          
            url = create_url(minnum, maxnum)
            print("try ", url)
            url_list.append(url)
            res = requests.head(url, timeout = 3.5)
            res.raise_for_status()
            if res.status_code == 200:
                webbrowser.open(res.url) # open the url
                opened_url = True
                return res.url, url_list
        except:
            continue

open_url = open_random_website(4, 60)
create_url_log(open_url[1])
print("open ", open_url[0])