#!/usr/bin/env python3
import feedparser
from jinja2 import Template
from datetime import datetime
import re
import random
import html
from bs4 import BeautifulSoup
import requests
import json
from typing import List, Dict

from config import *

MATCHER_TITLE = re.compile(RE_TITLE_FILTER)
MATCHER_FOOTNOTE = re.compile(RE_FOOTNOTE)
MATCHER_FYYD = re.compile(r"https://fyyd\.de/podcast[^\"]+")
MATCHER_EPISODE = re.compile(r"https://fyyd\.de/episode/[^\"]+")
random.seed(123)


def get_footnote_text(soup, footnote):
    if not footnote:
        return ""
    tds = soup.select('table:nth-child(7) tr td')
    for fn_num, info in zip(tds[0::2], tds[1::2]):
        if fn_num.text == footnote:
            return info.text
    return ""


def translate(feed):
    entries = list()
    for entry in feed['entries']:
        if not MATCHER_TITLE.match(entry.title):
            continue
        soup = BeautifulSoup(html.unescape(entry.content)[0]['value'], features='html.parser')
        tds = soup.select('table:nth-child(3) tr td') 
        for producer, ahref in zip(tds[0::2], tds[1::2]):
            a = ahref.select('a')[0]
            text = a.text
            footnote = get_footnote_text(soup, ([""] + MATCHER_FOOTNOTE.findall(text))[-1])
            text = MATCHER_FOOTNOTE.sub("", text)
            url = a.attrs['href']
            entries.append({
                    'title': f'{producer.text} - {text}',
                    'description': f'{producer.text} - {text}.<br/>{footnote}',
                    'pubDate': entry['updated'],
                    'link': url, # TODO proper link
                    'url': url,
                    'guid': url
                    })
    return entries

def pick_fyyd_feed(url:str, num_results:int = 10) -> List[Dict]:
    entries = list()
    response = requests.get(url)
    for i, x in enumerate(MATCHER_FYYD.findall(response.text)):
        if i > num_results:
            break
        response = requests.get(x)
        response = requests.get(MATCHER_EPISODE.findall(response.text)[0]+"/pp-json")
        content = json.loads(response.text)
        item = content['episode']
        item.update(content['podcast'])
        if 'mp3' not in content['episode']['media']:
            continue
        entries.append({
            'title': html.unescape(content['episode']['title']),
            'description': content['episode']['description'] + "\nFeed: " + content['podcast']['feed'],
            'link': [content['episode']['media'][k] for k in content['episode']['media']][0],
            'url': content['episode']['url'],
            'guid': content['episode']['url'],
            'pubDate': '',
            'source': content['podcast']['feed']
            #'image': content['episode']['coverUrl']
        })
    return entries


def main(outpath: str) -> int:
    translated = pick_fyyd_feed(URL_FYYD)
    composed = Template(TEMPLATE_STRING).render( \
            title='Serendipod',
            link="https://github.com/pschwede/serendipod",
            description='Scraped from https://fyyd.de',
            image=URL_CHANNEL_IMAGE,
            generator=PROJECT_NAME,
            version=VERSION,
            now=datetime.now().strftime("%a, %d %b %Y %X +0200"),
            entries=translated \
            )

    if not outpath:
        print(composed)
        return 0

    with open(outpath, 'w') as outfile:
        outfile.write(composed)
        return 0
    return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(outpath=sys.argv[1] if len(sys.argv)>1 else None))
