#!/usr/bin/env python

PROJECT_NAME = "serendipod"
VERSION = '0.0.3'
URL_FYYD = 'https://fyyd.de/discover/hot'
LANGUAGE = 'en'
URL_CHANNEL_IMAGE = ''
RE_TITLE_FILTER = r'^Podcast'
RE_FOOTNOTE = r'\([0-9]+\)$'
TEMPLATE_STRING = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
        <channel>
            <title>{{ title|e }}</title>
            <link>{{ link }}</link>
            <atom:link href="https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss" rel="self" type="application/rss+xml" />
            <description>{{ description|e }}</description>
            {% if image %}<image><title>{{ title }}</title><url>{{ image }}</url><link>https://raw.githubusercontent.com/pschwede/serendipod/main/feed.rss</link></image>{% endif %}
            <language>{{ language|d('de-de') }}</language>
            <copyright>{{ copyright }}</copyright>
            <generator>{{ generator }} {{ version }}</generator>
            <lastBuildDate>{{ now }}</lastBuildDate>
            {% for entry in entries %}<item>
                <title>{{ entry['title']|e }}</title>
                <description>{{ entry['description']|e }}</description>
                {% if entry['pubDate'] %}<pubDate>{{ entry['pubDate'] }}</pubDate>{% endif %}
                {% if entry['image'] %}<itunes:image href="{ entry['image'] }/>{% endif %}
                <link>{{ entry['link'] }}</link>
                <enclosure type="audio/mpeg" length="1" url="{{ entry['url'] }}"/>
                <guid>{{ entry['guid'] }}</guid>
                {% if source %}<source>{{ source }}</source>{% endif %}
            </item>{% endfor %}
        </channel>
</rss>"""
