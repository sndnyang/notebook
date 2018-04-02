Title: Git的一些问题
Slug: issues-of-git  
Date: 2018-04-02 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code   
Tags: git, 部署
Category: 开发工具    
Summary: Git使用时遇到的一些问题 
  
[TOC]

# git status中文名

[Git实用小技巧：git status 中文文件名编码问题解决](https://blog.csdn.net/mlq8087/article/details/52174834)

在默认设置下，中文文件名在工作区状态输出，查看历史更改概要，以及在补丁文件中，文件名的中文不能正确地显示，而是显示为八进制的字符编码

通过将Git配置变量 core.quotepath 设置为false，就可以解决中文文件名称在这些Git命令输出中的显示问题，

示例：

    $ git config --global core.quotepath false