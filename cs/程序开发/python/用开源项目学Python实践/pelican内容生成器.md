Title: pelican内容生成器
Slug: pelican-generator    
Date: 2017/4/15 14:24:50
Authors: sndnyang sndnyang.github.io
Modified: 2017/4/15 14:26:08
Category: Python
Tags: Python, 代码阅读
Summary: pelican是如何解析文件的，生成器generator  

[TOC]

# 引入

接上回 >[Pelican主程序调用](learn-python-by-opensource-project-pelican.html#_8)

1. 调用内容生成器，生成 [pelican内容生成器](pelican-generator.html)
    p = get_generator_classes()
    p.generate_context()
2. 调用输出模块 >[pelican-writer](pelican-writer.html)
    writer = self.get_writer()
    p.generate_output(writer)

得到一个 generator 列表， 再去生成内容

所以我们来看 Genertator 类

# Generator

基础类

## __init__

关键，调用 <[pelican-Readers类](pelican-reader.html)，读取内容

        self.readers = Readers(self.settings, readers_cache_name)

读取文件系统

        simple_loader = FileSystemLoader(os.path.join(theme_path,
                                         "themes", "simple", "templates"))

其他函数暂略，

完成了 Generator的初始化， 我们来看 generate_context(), Generator类中没有该函
数，直接出现成几个子类中， 所以我们要看看几个子类。

一般只用到两个类, 看看它们各自是如何 generator_context的:

1. <[博客文章生成类](pelican-ArticlesGenerator.html#generate_context)
2. <[其他页面生成](pelican-PagesGenerator.html#generate_context)

## 选择writer

>[pelican-writer](pelican-writer.html)

## 输出

generate_output函数也是只在子类中存在

1. <[博客文章生成类](pelican-ArticlesGenerator.html#generate_output)
2. <[其他页面生成](pelican-PagesGenerator.html#generate_output)

# 结束

重要细节后续补充

