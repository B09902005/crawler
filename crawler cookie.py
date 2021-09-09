import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

import urllib

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

def findarticle(url):
    num = 0
    href = []
    while (True):
        context = makecontext(url)
        titles = context.find_all("div", class_="title")
        for title in titles:
            if (title.a != None):
                href.append("https://www.ptt.cc" + title.a["href"])
                print(num,title.a.string)
                num += 1
        url = prevpage(url)
        if (url == 0):
            break
    return href

def prevpage(url):
    context = makecontext(url)
    temp = context.find("a", string="‹ 上頁")
    if (temp.find('btn wide disabled') == -1):
        return "https://www.ptt.cc" + temp["href"]
    else:
        return 0

def makecontext(url):
    request = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")
    context = bs4.BeautifulSoup(data,"html.parser")
    return context

if __name__ == '__main__':
    what = input('輸入你想搜尋的教授或課程名稱。')
    url = "https://www.ptt.cc/bbs/NTUcourse/search?q=" + urllib.parse.quote(what)
    href = findarticle(url)
    num = int(input('\n請輸入你想進入的文章的編號。'))
    url = href[num]
    printcontext(url)
