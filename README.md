# Serendipod

[![subscribe rss feed](https://img.shields.io/badge/%F0%9F%94%8A%20RSS-subscribe-orange)](https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss) [![antennapod](https://img.shields.io/badge/Subscribe%20with-Antennapod-blue)](https://github.com/AntennaPod/AntennaPod) ![build](https://github.com/pschwede/serendipod/workflows/build/badge.svg) ![issues](https://img.shields.io/github/issues/pschwede/serendipod) 
[![toot](https://img.shields.io/badge/share%20on%20Mastodon%20-%20mastodon?logo=Mastodon&logoColor=white&labelColor=%235b4be1&color=grey&link=https%3A%2F%2Fsharetomastodon.github.io%2F%3Ftitle%3DNeed%2520some%2520serendipity%2520in%2520your%2520podcast%2520feed%26url)](https://sharetomastodon.github.io/?title=Need%20some%20serendipity%20in%20your%20podcast%20feed&url=https://github.com/pschwede/serendipod)

The newest episodes of the newest podcast series from [fyyd.de](https://fyyd.de) are converted to a single podcast feed.

## Subscribe

Click on [the podcast feed](https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss) to open it in your default app or copy and paste its URL into your app:

* en: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss```
* zh: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.zh.rss```
* es: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.es.rss```
* pt: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.pt.rss```
* fr: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.fr.rss```
* de: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.de.rss```
* jp: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.jp.rss```

## Run the bot yourself

Installation:

```
git clone https://github.com/pschwede/serendipod.git serendipod
cd serendipod
python3 -mvenv env
source env/bin/activate
pip install -r requirements.txt
```

Aggregate the newest feed:

```
./cron.sh en feed.rss
```
