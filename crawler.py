import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import bs4


# a crawler for ptt NTUcourse
url = "https://www.ptt.cc/bbs/NTUcourse/index.html"
request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data,"html.parser")
#print(root)
'''
print(root.title)
print(root.title.string)
print()

titles = root.find("div", class_="title")
print(titles)
print(titles.a.string)
print()
'''
titles = root.find_all("div", class_="title")
for title in titles:
    if (title.a != None):
        print(title.a.string)





# a crawler for a website made by myself
'''
url = "https://b09902005.github.io"
request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data,"html.parser")

print(root)
print()
print(root.title.string)
print()
print(root.h3.string)
print()
print(root.li.string)
print()
for i in root.find_all("li"):
    print(i.string)
'''
