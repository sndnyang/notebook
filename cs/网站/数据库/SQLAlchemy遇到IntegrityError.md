Title: SQLAlchemy遇到IntegrityError  
Slug: SQLAlchemy-IntegrityError-duplicate
Date: 2017-09-06 14:28:45  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code
Tags: SQLAlchemy
Summary: SQLAlchemy when IntegrityError, duplicate key, many to many append, how to deal it.重复键，多对多添加时出现怎么办？
  
[TOC]

# 模板

    try:
        tag_obj = query_add_interests(tag, major)
        if professor and tag_obj:
            professor.interests.append(tag_obj)
            db.session.flush()
    except IntegrityError:
        db.session.rollback()

# 介绍

1. db.session.flush()
2. db.session.rollback()

## 参考

[flush](https://stackoverflow.com/questions/24522290/cannot-catch-sqlalchemy-integrityerror)
