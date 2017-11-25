Title: 使用git在服务器上传部署代码
Slug: use-git-upload-deploy-project  
Date: 2017-08-28 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code   
Tags: git, 部署
Category: 开发工具    
Summary: 如何在服务器上创建GIT库，使得git push之后能自动化部署    
  
[TOC]

# 本地创建

## 安装GIT

[CentOS配置-git安装](config-centOS-install-git)

## 本地创建

    git init // 略
    git remote add 你给远程服务器起的名字 远程服务器链接（例ssh://username@hostname_or_ip/path/to/you/project , 不要乱加 .git后缀）
或

    git clone ssh://username@hostname_or_ip/path/to/you/project [指定文件夹名，默认用远程文件夹名]

# 服务器安装

见[CentOS配置-git安装](http://sndnyang.github.io/config-centOS-install-git.html)

# SSHKEY密钥配置

见[CentOS配置-SSHKEY密钥配置](http://sndnyang.github.io/config-centOS-config-sshkey.html)

# 创建共享裸仓库

    // 先创建文件夹
    git init --bare

# 创建运行库

同本地创建， 本地库、共享裸库、运行库执行顺序不限

创建完毕后， 运行库一定要从共享库中获取一次（比如clone来创建，或pull一次）

# 配置挂钩hooks

## 介绍

在共享库文件夹的 hooks 文件夹下有几个.sample 文件， 含义为(随便一个词典搜一下就知道)：

- pre-, 在...之前
- prepare-, 准备，但我暂时没关注什么用
- post-, 在...之后
- commit, 对应 git commit
- update 或 receive 或 push, 对应 git push，不是所有版本都有 post-receive, 那么post-update也能用

## 配置

选择代表在 git push之后执行的.sample文件， 如 post-update.sample 或 post-receive.sample

    copy it post-update(或post-receive)

并修改文件内容

# post文件

## 操作说明

我们要在从本地git push到服务器共享库后， 自动把代码更新给运行库， 并重启程序

1. 自动导出到运行库    
        git --work-tree=/path/to/you/运行库 --git-dir=/path/to/you/共享库 checkout -f
2. 执行更新、重启命令

## 示例

以python flask建的站为例

    #!/bin/sh
    git --work-tree=/var/www-site/sndnyang --git-dir=/var/www-git/sndnyang.git checkout -f
    /var/www-site/sndnyang/bin/pip install -r /var/www-site/sndnyang/requirements.txt   // 导出后， 安装程序所需第三方库
    cd /var/www-site/sndnyang/XXX  // 不知道有没有意义~~~
    /var/www-site/sndnyang/bin/supervisorctl -c /var/www-site/sndnyang/supervisor.conf restart sndnyang // 用supervisor重启sndnyang程序

## 执行

必须手工运行一次

    ./hooks/post-update(receive)

git push后才会自动执行

# 本地上传

    git push 你给远程服务器起的名字 master(或其他分支？)

示例的观察结果：

    会有 pip install -r requirements.txt 一大堆的提示  
    会有 supervisorctl 运行结果提示

成功
