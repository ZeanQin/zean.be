#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Zean Qin'
SITENAME = u'Zean Qin'
SITEURL = '' # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

# make sure files in the 'images' and 'pdfs' folder are copied to the output directory during site generation
STATIC_PATHS = ['images', 'pdfs']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
  'table': ['table', 'table-striped', 'table-hover'],
  'img': ['img-fluid'],
  'blockquote': ['blockquote'],
}

# Social widget
# SOCIAL = (('GitHub', 'https://github.com/zeanqin'),
#     ('LinkedIn', 'https://www.linkedin.com/in/zeanqin/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False

# Theme Settings ==================================================

THEME = 'themes/pelican-alchemy/alchemy'

SITESUBTITLE = 'Tech, life and a little bit of everything else'
SITEIMAGE = '/images/profile.jpg'
# index.html head <meta> description
ESCRIPTION = 'Zean Qin\' official website.'

# Blogroll
LINKS = (
#     ('Link A', 'http://getpelican.com/'),
#     ('Link B', 'http://python.org/'),
)

ICONS = [
         ('github', 'https://github.com/zeanqin'),
         ('linkedin', 'https://www.linkedin.com/in/zeanqin/'),
         ('feed', '/feeds/all.atom.xml'),
]

PYGMENTS_STYLE = 'monokai'
RFG_FAVICONS = True

HIDE_AUTHORS = True
GOOGLE_ANALYTICS = 'UA-90723209-1'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
