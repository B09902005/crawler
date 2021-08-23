import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

import bs4

# This a crawler for ptt NTUcourse

def printcontext(url):
    context = makecontext(url)
    print(context)
    return
    spans = context.find_all('span', class_ = 'f3')
    for span in spans:
        print(span)
    print()
    return

def printtitle(url):
    context = makecontext(url)
    titles = context.find_all("div", class_="title")
    for title in titles:
        if (title.a != None) and (title.a.string.find('通識') != -1):
            #url = "https://www.ptt.cc" + title.a['href']
            #printcontext(url)
            print(title.a.string)
    return

def prevpage(url):
    context = makecontext(url)
    temp = context.find("a", string="‹ 上頁")
    if (temp.find('"btn wide"') != -1):
        return "https://www.ptt.cc" + temp["href"]
    else:
        return 0

def makecontext(url):
    request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    context = bs4.BeautifulSoup(data,"html.parser")
    return context

if __name__ == '__main__':
    #what = input('輸入你想搜尋的教授或課程名稱。')
    #url = "https://www.ptt.cc/bbs/NTUcourse/search?q=" + what
    url = "https://www.ptt.cc/bbs/NTUcourse/index.html"
    for i in range (3):
        printtitle(url)
        url = prevpage(url)
        if (url == 0):
            break
