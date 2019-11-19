#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#### TITLE AND AUTHOR SETTINGS ####
AUTHOR = u'Richie'
SITENAME = u'Richie Lin'
#SITESUBTITLE = 'aka. Richie'
SITESUBHEADER = 'Time\'s Limited, Gotta Keep Moving.'
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
THEME = '../BT3-Flat'

# Other pics
FAVICON = "/images/icon-r.jpg"
ICON = "/images/icon-r.jpg"
SHORTCUT_ICON = "/images/icon-r.jpg"
HEADER_IMAGE = "/images/icon-r.jpg"
BACKGROUND_IMAGE = '/images/bg-pic.jpg'

# About me
PERSONAL_PHOTO = "/images/avatar-274x274.png"
PERSONAL_INFO = '<p align="left">Hi! I am Tao Lin and I like people to call me Richie.</p> <p align="left">I am a data scientist currently working as a research associate for The Data Collaborative for Justice at John Jay College of Criminal Justice, the City University of New York. I am also a technical consultant at the New York City Mayor\'s Office of Criminal Justice.</p> <p align="left">Before I started the journey in the Criminal Justice field, I was a Marketing Manager at Pepsi Beverage of West North-China West Region.</p>'

# LOADING SETTING
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True

# List style
ARCHIVE_LIST = False

# POSTING LIMIT
POST_LIMIT = 1
DISPLAY_PAGES_ON_MENU = True

#### Working samples ####
WORK_DESCRIPTION = " "
WORK_LIST = (
	('link',
		'files/resume/resume.png', 
		'Resume', 
		' ',
		'files/resume/resume.pdf' 
		), 
	('link',
		'files/2003-2006 NYC SQF mapping/SQF_icon.png',
		'NYPD 2003 - 2006 Stop, Question and Frisk Mapping',
		'An analysis at MJP',
		'files/2003-2006 NYC SQF mapping/03-06NYC_SQF_maping.html'
		),
	('link',
		'files/GermanCreditAnalysis/index.png',
		'Prediction methods analysis with the German Credit Data set',
		'A presentation at RangTech',
		'https://rpubs.com/zmqplintao/139641'
		),
	('link',
		'files/NBA_conference paper/img_NBA_conf_paper1.png',
		'Predicting Sports Outcomes with a Rank-And-Choose Variable Selection Process',
		"An Analysis published at ABDA.15 conference during my Master's",
		'http://worldcomp-proceedings.com/proc/p2015/ABD6305.pdf'
		)
)

#INDEX_CN = True


#### THEME SETTINGS ENDS ####



# Blogroll
LINKS = (('Data Collaborative for Justice','https://datacollaborativeforjustice.org/'),
			('NYC Mayor\'s Office of Criminal Justice','https://criminaljustice.cityofnewyork.us/')
)

# Social widget
SOCIAL = (('linkedin','https://www.linkedin.com/in/taolinrichie/'),
	  ('github', 'https://github.com/richielin'),
	  ('envelope', 'mailto:richielin321@gmail.com')
	 )

#### GOOGLE ANALTICS SEETINGS ####
GOOGLE_ANALYTICS = 'UA-103174172-1'
GOOGLE_ANALYTICS_DOMAIN = 'taolinrichie.com'


DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Copy right
COPYRIGHT = '2019 &copy; All Rights Reserved.'
