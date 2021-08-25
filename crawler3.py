import ssl    # for mac
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

import bs4   # for HTML
import json  # for JSON

# This a crawler for kkday.com that shows the titles of articles in it

def makecontext_html(url):  # HTML form
    request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    context = bs4.BeautifulSoup(data,"html.parser")
    return context

def makecontext_json(url):  # JSON form (lists and dicts)
    request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    context = json.loads(data)
    return context

def printtitle(url):   # This is written with observing source code of the website
    context = makecontext_json(url)
    attributes = context["data"]["homepage_product_group"]
    for i in range (len(attributes)):
        #print(attributes[i]["title"])
        products = attributes[i]["prod_list"]
        if (type(products) == type([])):
            for j in range (len(products)):
                print("  ",products[j]["price"],"  ",products[j]["name"])
        else:
            for product in products:
                print("  ",products[product]["price"],"  ",products[product]["name"])
        print()
    return

## Due to AJAX, we need to observe the website first and find JHX to find what we want
if __name__ == '__main__':
    url = "https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=f8cf87824ffba975d6741d8e36b6623a"
    printtitle(url)
