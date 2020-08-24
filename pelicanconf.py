#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

if sys.getdefaultencoding() != 'utf8':
    reload(sys)
    sys.setdefaultencoding('utf8')

            
AUTHOR = u'sndnyang'
SITENAME = u'科探空谷'

# TODO: 这个是我的网站名
DISQUS_SITENAME = 'sndnyang'
SITEURL = 'http://sndnyang.github.io'

MARKUP=('rst', 'md', 'markdown', 'dmd')
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = r'E:\project\blog\pelican\pelican-elegant'
PLUGIN_PATHS = [r'E:\project\blog\pelican\pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'ipynb.liquid']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc', 'problem']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

LANDING_PAGE_ABOUT = {'title': '科学，探索，空间，成长', 
        "details": '''简历CV: English <a href="https://1drv.ms/b/s!AgCFFlwzHuH8jFHCJF5oSfcxHGx3" target="_blank">English CV</a>
        中文 <a href="https://1drv.ms/b/s!AgCFFlwzHuH8jFK01spW4z0pYUGt " target="_blank">中文简历</a><br>
        微博： <a href="https://www.weibo.com/u/2405149384" target="_blank">微博主页</a>
        知乎： <a href="https://www.zhihu.com/people/jiandanminzhi" target="_blank">知乎主页</a><br>
        蜻蜓读论文：<br>
        B站: <a href="https://space.bilibili.com/17529417" target="_blank">Bilibili</a><br>
        Youtube: <a href="https://www.youtube.com/channel/UCwyMgDylnGQ-Wf4N00RmWJw" target="_blank">频道主页</a><br>
        公众号: zhimind <br><img src="/images/qrcode_zhimind.jpg"/>
        '''}

DEFAULT_PAGINATION = 10

PROJECTS = [{'name': '知维图',
    'url': 'http://zhimind.com',
    'description': 'zhimind a project I hope to push the education field forward! Make'
    'a difference by all means 知维图 智能交互教学实验'},
    {'name': '大学录取条件信息库',
    'url': 'http://www.zhimind.com/oversea/research.html',
    'description': 'GPA、截止日期、学费，研究方向、招生意向等信息，勉强有个爬虫爬研究方向、招生意向，但需要人工定制关键字'},
    {'name': 'Educational Policy Analytics',
    'url': 'https://nitro2.cs.gsu.edu',
    'description': 'Educational Policy Analytics, text mining'},
    {'name': 'gpa 计算器',
    'url': 'gpa_calculator.html',
    'description': '就是一个多功能多算法的GPA计算器,拒绝一行行手工输入'},
    {'name': '个人开发的外语学习工具合集',
    'url': 'tools_for_foreign_language_learning.html',
    'description': '自己编写的多个外语学习工具'},
    {'name': '一些小玩意合集',
    'url': 'http://sndnyangd.appspot.com/',
    'description': '某个算法课程布置的小作业实现，包括红包、点名、二维布料裁剪、代码查重（抄袭）'},
    {'name': 'Deep Q Network Player',
    'url': 'https://github.com/sndnyang/GamePlayer',
    'description': '''a project use Deep Q Network(DQN) to auto learn how to play game with screen capture and computer vision and plan for a really complicated\complex practise system for all kinds of AI technologies.
    深度强化学习来玩游戏，但尽量不接入游戏源代码，采用连续截图、计算机视觉分析图片的方式来代替游戏直接的状态数据，'''},
    {'name': 'algorithm vis study',
    'url': 'ds_alg_code.html',
    'description': 'a project use ideas from tryregex, elegatorsaga, based on'
    'vis.js to learn algorithm (Unavailable)'},
    {'name': '幻灯片',
    'url': 'slides_set.html',
    'description': '制作的文本幻灯片集合， 应该多数是读论文的笔记'},    
    {'name': '其他',
    'url': '/other.html',
    'description': '之前不小心把markdown笔记全部删了， 只剩html， ' 
        '有些文件不想重新制作'}]

#disqus_identifier = "sndnyang.github.io"   

RECENT_ARTICLES_COUNT = 15
COMMENTS_INTRO  = "this man is lazy, nothing left"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

WEIBO_ID = "2405149384"
SITEMAP= {'format': 'xml'}