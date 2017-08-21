Title: Python功能实现  
Date: 2017/4/24 22:25:32
slug: python-function-implement
Authors: sndnyang sndnyang.github.io
Modified: 2017/4/24 22:26:28
Category: Python  
Tags: Python  

[TOC]

# 中文、汉字字符判断

    def check_contain_chinese(check_str):
         for ch in check_str.decode('utf-8'):
             if u'\u4e00' <= ch <= u'\u9fff':
                 return True
         return False
