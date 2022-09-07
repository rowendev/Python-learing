from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import collections #debug
collections.Callable = collections.abc.Callable
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.chickpt.com.tw/cases
count = input('Enter count:')
position = input('Enter position:')
time = 1
print(type(url))

#for page in range(int(count)):
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for tag in tags:
    if(time > int(position)):break
    else:time = time + 1
    url = tag.get('href', None)
    print(url)
