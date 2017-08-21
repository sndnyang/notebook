Title: flask开发问题汇总  
Date: 2016-11-07 10:34:35
Category: web开发
tags: web, flask, sql
slug: flask-problem-summary

[TOC]

# sqlalchemy 更新数据问题

要替换，特别是json类型数据，不能在原数据上添加， 没法更新。 需要新建变量，遍历原json数据。

如：

    stored_data = word_dict.data
    new_data = data
    for k in stored_data:
        if k not in new_data:
            new_data[k] = {}
        for e in stored_data[k]:
            if e not in new_data[k]:
                new_data[k][e] = stored_data[k][e]

    word_dict.data = new_data

注：

    使用 copy.deepcopy()

# flask上传文件


