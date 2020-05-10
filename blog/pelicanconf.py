#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'Tom Goren'
SITENAME = "Notes to self"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = False

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

LINKS = ''
SOCIAL = ''
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = ["images"]
THEME = f'./pelican-elegant'
PYGMENTS_STYLE = 'monokai'
GOOGLE_ANALYTICS = 'G-QB9VCC5RPZ'
