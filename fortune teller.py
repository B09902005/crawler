import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
import bs4
import json

import random

def changetoword(line):
    line = str(line)
    left = line.find('>') + 1
    right = line.find('<',2)
    line = line[left:right]
    left = 0
    while (str.isalpha(line[left]) == False):
        left += 1
    line = line[left:]
    return line.split(" ")[0]

def makelist(url):
    context = makecontexthtml(url)
    (english,chinese) = ([],[])
    paragraph = context.find_all("p")
    for line in paragraph:
        if (line.find("span", lang = "ZH-TW") != None):
            chinese.append(line.span.string)
            line = changetoword(line)
            english.append(line)
    return (english,chinese)

def makecontexthtml(url):
    request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    context = bs4.BeautifulSoup(data,"html.parser")
    return context

def makecontextjson(url):
    request = req.Request(url, headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"})
    with req.urlopen(request) as response:
        data =  response.read().decode("utf-8")
    context = json.loads(data)
    return context

if __name__ == '__main__':
    url = "https://douze.pixnet.net/blog/post/398218087"
    (english,chinese) = makelist(url)
    print('輸入一個問題(如：我今天運勢如何？我等等要做什麼？用一個字形容台大電機？...等等)，我可以用一個字來回答你。(跑一次程式可以問十題)')
    length = len(english)
    for i in range (10):
        question = input()
        num = random.randint(0,length-1)
        print(english[num],chinese[num],'\n')
        
        


