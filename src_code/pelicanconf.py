#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#### TITLE AND AUTHOR SETTINGS ####
AUTHOR = u'Richie'
SITENAME = u"Tao Lin"
SITESUBTITLE = 'AKA. Richie'
SITEURL = 'http://taolinrichie.com'

#### INPUT AND OUTPUT SETTING ####
ARTICLE_EXCLUDES = ['files']
PATH = 'content'
STATIC_PATHS = ['files', 'images']
EXTRA_PATH_METADATA = {'files/CNAME':{'path':'CNAME'},'files/README.md':{'path':'README.md'}}
OUTPUT_PATH = '../richielin.github.io/'

#### TIMEZONE AND LANGUAGE SETTING ####
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#### THEME SETTINGS ####
THEME = '/home/richie/projects/pelican_themes/BT3-Flat'

# Other pics
FAVICON = "images/icon-r.jpg"
ICON = "images/icon-r.jpg"
SHORTCUT_ICON = "images/icon-r.jpg"
HEADER_IMAGE = "images/icon-r.jpg"
BACKGROUND_IMAGE = 'images/bg-pic.jpg'

# About me
PERSONAL_PHOTO = "images/avatar-274x274.png"
PERSONAL_INFO = "<p align='left'>Hi! This is Tao Lin and people call me Richie.</p> <p align='left'>I am a data scientist currently working as a research analyst for The Misdemeanor Justice Project at John Jay College of Criminal Justice, City University of New York.</p> <p align='left'>I am also a prior Professional Marketing Manager at Pepsi Beverage West North-China Region.</p> <p align='left'>I graduated from Texas A&M International University with a Master's degree in Management Information System.</p> <p align='left'>The title picture was taken on my first visit to New York City, an amazing place belongs to all dreamers. :)</p>"

# LOADING SETTING
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True

# List style
ARCHIVE_LIST = False

# POSTING LIMIT
POST_LIMIT = 1
DISPLAY_PAGES_ON_MENU = True

#### THEME SETTINGS ENDS ####



# Blogroll
LINKS = (('The Misdemeanor Justice Project','http://misdemeanorjustice.org'),
	('Evan Misshula', 'https://Misshula.org'),
	('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (('linkedin','https://www.linkedin.com/in/taolinrichie/'),
          ('twitter','https://twitter.com/richiefreaky'),
	  ('github', 'https://github.com/richielin'),
	  ('envelope', 'mailto:richielin321@gmail.com'),

	 )

#### GOOGLE ANALTICS SEETINGS ####
GOOGLE_ANALYTICS = 'UA-103174172-1'
GOOGLE_ANALYTICS_DOMAIN = 'taolinrichie.com'


DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Copy right
COPYRIGHT = '2017 &copy; All Rights Reserved. This website is developed under Python, enpowered by Pelican. Thanks to Ken Lai for this amazing theme. Thanks to Evan Misshula and Adam Fera for the inspiration and guide in the development.'


