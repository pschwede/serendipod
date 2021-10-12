#!/usr/bin/env python

PROJECT_NAME = "serendipod"
VERSION = '0.0.2'
URL_FYYD = 'https://fyyd.de/newest/0'
URL_CHANNEL_IMAGE = ''
RE_TITLE_FILTER = r'^Podcast'
RE_FOOTNOTE = r'\([0-9]+\)$'
TEMPLATE_STRING = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
        <channel>
            <title>{{ title|e }}</title>
            <link>{{ link }}</link>
            <description>{{ description|e }}</description>
            {% if image %}<image>{{ image }}</image>{% endif %}
            <language>{{ language|d('de-de') }}</language>
            <copyright>{{ copyright }}</copyright>
            <generator>{{ generator }} {{ version }}</generator>
            <lastBuildDate>{{ now }}</lastBuildDate>
            {% for entry in entries %}<item>
                <title>{{ entry['title']|e }}</title>
                <description>{{ entry['description']|e }}</description>
                <itunes:image href="{{ entry['image'].replace('"', '\\"') }}"/>
                <pubDate>{{ entry['pubDate'] }}</pubDate>
                <link>{{ entry['link'] }}</link>
                <enclosure url="{{ entry['url'] }}"/>
                <guid isPermalink="false">{{ entry['guid'] }}</guid>
            </item>{% endfor %}
        </channel>
</rss>"""
