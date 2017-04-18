Title: pelican文章生成
Slug: pelican-ArticlesGenerator  
Date: 2017/4/18 13:29:55
Authors: sndnyang sndnyang.github.io
Category: Python
Tags: Python, 代码阅读
Modified: 2017/4/18 14:09:50

[TOC]

# 引入

接上上回 >[Pelican主程序调用
](learn-python-by-opensource-project-pelican.html#_8) 及 上回[Pelican生成器
](pelican-generator.html)

1. 调用内容生成器，生成 [pelican内容生成器](pelican-generator.html)
    p = get_generator_classes()
    p.generate_context()
2. 调用输出模块 >[pelican-writer](pelican-writer.html)
    writer = self.get_writer()
    p.generate_output(writer)

# generate_context

核心流程

1. 遍历文件[get_files](#)  
        for f in self.get_files(
2. 获取缓存 >[pelican缓存](pelican-CachingGenerator.html)   
        article_or_draft = self.get_cached_data(f, None)
3. 读取文件 <[pelican-Readers类](pelican-reader.html)    
        article_or_draft = self.readers.read_file(
4. 内容验证  
        if not is_valid_content(article_or_draft, f):
5. 翻译（略）   
        self.articles, self.translations = process_translations(all_articles,
6. 更新context上下文   
        self._update_context(('articles', 'dates', 'tags', 'categories',
                              'authors', 'related_posts', 'drafts'))
7. 保存缓存   
        self.save_cache()
        
