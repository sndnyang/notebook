Title: windows问题处理
Slug: some-issues-on-windows    
Date: 2017/5/20 10:39:58
Authors: sndnyang sndnyang.github.io
Modified: 2017/5/20 10:42:00
Category: 操作系统    
Tags: 操作系统, windows   

[TOC]

# 没有新建或新建文件夹无反应

[原文](http://blog.163.com/winter_0578/blog/static/487948022011162496354/)

使用了方法一：

把下面一段代码存在一个记事本上，再选择另存为1.cmd，最后运行！


    regsvr32 /u /s igfxpph.dll 
    reg delete HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers /f 
    reg add HKEY_CLASSES_ROOT\Directory\Background\shellex\ContextMenuHandlers\new /ve /d {D969A300-E7FF-11d0-A93B-00A0C90F2719}

