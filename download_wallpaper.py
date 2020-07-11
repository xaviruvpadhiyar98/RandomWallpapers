#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

useragent = UserAgent().random
   
def download_image(img_url):
    img_bytes = get('https://i.redd.it/' + img_url).content
    if len(img_bytes) > 2048:
        with open(img_url, 'wb') as img_file:
            img_file.write(img_bytes)

url = 'https://www.reddit.com/r/wallpapers/top/?t=week'

headers = {
    'authority': 'www.reddit.com',
    'origin': 'https://www.reddit.com',
    'user-agent': useragent,
    'content-type': 'text/plain',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.reddit.com/r/wallpapers/top/?t=week',
}

s = get(url, headers=headers)
imgs = BeautifulSoup(s.content, 'html.parser').findAll('img')

wallpapers = []
if len(imgs) > 5:
    for x in imgs:
        if 'preview.redd.it/' in x['src'] and 'award' not in x['src']:
            start = x['src'].find('it/') + 3
            if 'png' in x['src']:
                end = x['src'].find('.png', start)
                wallpapers.append(x['src'][start:end] + '.png')
            elif 'jpg' in x['src']:
                end = x['src'].find('.jpg', start)
                wallpapers.append(x['src'][start:end] + '.jpg')       
            
with ThreadPoolExecutor() as executor:
    for url in wallpapers:
        executor.submit(download_image, url)
print("Done")
