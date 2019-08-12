Title: Git的一些问题
Slug: issues-of-git  
Date: 2018-04-02 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code   
Tags: git, 部署
Category: 开发工具    
Summary: Git使用时遇到的一些问题 
  
[TOC]

# git 符号/软链接 问题

问题描述：有一些常用函数的代码会被不同项目使用， 但又经常觉得之前写得不好，进而时不时地又改动一下， 所以希望用符号链接把代码摘出来， 同时git还要支持符号链接, 特别是windows系统。

Description: How to let git to support symbolic links? And what's the right command to create symbolic links in windows.

## git 支持符号链接


[git config core.symlinks true](https://stackoverflow.com/questions/11728882/how-to-get-git-on-windows-to-ignore-symbolic-links)

## windows系统的符号链接

git bash的ln -s实际上是创建了一个副本， PASS。 mklink /d 创建的链接， git 不支持， 请使用 

    mklink /j link target

Related error:

1. git  fatal: pathspec 'xxx' is beyond a symbolic link. Solution: use mklink 

# git status中文名

[Git实用小技巧：git status 中文文件名编码问题解决](https://blog.csdn.net/mlq8087/article/details/52174834)

在默认设置下，中文文件名在工作区状态输出，查看历史更改概要，以及在补丁文件中，文件名的中文不能正确地显示，而是显示为八进制的字符编码

通过将Git配置变量 core.quotepath 设置为false，就可以解决中文文件名称在这些Git命令输出中的显示问题，

示例：

    $ git config --global core.quotepath false


＃ Git本地多用户配置

编辑 ~/.ssh/config

    Host git.iboxpay.com
        HostName git.iboxpay.com  //这里填你们公司的git网址即可
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa_gitlab
        User zhangjun

    # github
    Host github.com
        HostName github.com
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa_github
        User ZJsnowman

[参考来源](https://blog.csdn.net/jack_0817/article/details/55668892)


