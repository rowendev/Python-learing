import urllib.request as req

url = 'https://www.ptt.cc/bbs/Stock/index.html'
#count = input('輸入執行爬蟲次數:')

print('現在所在網址:',url)
print('進行爬蟲中...')
#def getData(url):
    
request = req.Request(url, headers={
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    })

with req.urlopen(request) as response:
        data = response.read().decode()

import bs4

    #debug
import collections
collections.Callable = collections.abc.Callable

root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all('div', class_='title')
    
for title in titles:
        if title.a != None:
            print(title.a.string)
        

    #nextLink = root.find('a', string = title.a.string)
    #print('next link:',nextLink['href'])
    #return nextLink['href']


#for dotime in range(int(count)+1):
    
#getData(pageURL)
   
