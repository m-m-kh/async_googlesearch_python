import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from time import time
from aiohttp import ClientSession
import asyncio



async def search(txt:str,stop:int = 10):
    if stop > 10 :
        stop = 10
    txt = txt.replace(' ','+')
    async with  ClientSession() as req:
        req.headers.update({"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"})
        async with req.get(f'https://www.google.com/search?q={txt}') as req:
            res = await req.text()
            bs4 = BeautifulSoup(res,'html.parser')
            bs4 = bs4.findAll('a')
            c = 0
            urls = []
            for i in bs4:
                if c == stop:
                    break
                else:
                    if i['href'].startswith('/url?q=http'):
                        l = urlparse(i['href'],'http')
                        l = parse_qs(l.query)['q'][0]
                        urls.append(l)
                        c+=1
            return urls
                

r = asyncio.run(search('اهنگ اب و هوای عالی 128 و 320'))
print(r)



