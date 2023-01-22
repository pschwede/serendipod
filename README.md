# Serendipod

[![subscribe rss feed](https://img.shields.io/badge/%F0%9F%94%8A%20RSS-subscribe-orange)](https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss) ![build](https://github.com/pschwede/serendipod/workflows/build/badge.svg) ![issues](https://img.shields.io/github/issues/pschwede/serendipod) [![antennapod](https://img.shields.io/badge/Subscribe%20with-Antennapod-blue)](https://github.com/AntennaPod/AntennaPod) [![tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fpschwede%2Fserendipod)](https://twitter.com/intent/tweet?text=r%2FEpisodes%20of%20the%newest%20podcasts%20series%3A%0Ahttps%3A%2F%2Fgithub.com%2Fpschwede%2Fserendipod)

The newest episodes of the newest podcast series from [fyyd.de](https://fyyd.de) are converted to a single podcast feed.

## Subscribe

Click on [the podcast feed](https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss) to open it in your default app or copy and paste its URL into your app:

en: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss```
zh: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.zh.rss```
es: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.es.rss```
pt: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.pt.rss```
fr: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.fr.rss```
de: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.de.rss```
jp: ```https://raw.githubusercontent.com/pschwede/serendipod/main/feed.jp.rss```

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
