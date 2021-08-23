import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import bs4


# a crawler for ptt NTUcourse


def printout(context):
    titles = context.find_all("div", class_="title")
    for title in titles:
        if (title.a != None):
            print(title.a.string)
    print()

def prevpage(context):
    temp = context.find("a", string="‹ 上頁")
    return "https://www.ptt.cc" + temp["href"]
    
if __name__ == '__main__':
    url = "https://www.ptt.cc/bbs/NTUcourse/index.html"
    for i in range (3):
        request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        
        context = bs4.BeautifulSoup(data,"html.parser")
        printout(context)
        url = prevpage(context)
