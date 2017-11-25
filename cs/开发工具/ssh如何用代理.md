Title: Git如何使用代理     
Slug: git-use-proxy  
Date: 2017-08-28 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code   
Tags: git, 部署, ssh       
Category: 开发工具    
Summary: 主要是 git如何用代理上传服务器， 特别是SSH方式   
  
[TOC]

# http/https

最简单

    git config --global http.proxy 'socks5://127.0.0.1:1081'
    git config --global https.proxy 'socks5://127.0.0.1:1081'

类似的

    git config --global http.proxy 'http://127.0.0.1:1081'
    git config --global https.proxy 'http://127.0.0.1:1081'

取消

    git config --global --unset http.proxy
    git config --global --unset https.proxy

# ssh

首先， git push时可以用 GIT_SSH 来提供SSH隧道， 所以我们要写一个脚本。

    export GIT_SSH="/g/project/map/socks5_proxy_ssh"

脚本内容， 第一行显然是（我在 windows下用 git bash, cmd版本没看）

    #!/bin/sh

执行的命令当然是 ssh xxx， 建立 ssh连接， 不过我们需要提供参数(选项 option)，让它的连接经过代理。使用

    ssh -h

看到 [-o option]， 详细的可配置项——我没找到官方文档， 总之，代理的选项叫 ProxyCommand。所以， 格式为：

    ssh -o ProxyCommand="connect-to-proxy-命令" "$@"

"$@" 是 shell脚本命令行全部参数的意思。

接下来就是用命令连接到你的代理了。

windows下，使用的是 connect 命令

    connect -S 127.0.0.1:1081 %h %p

linux下则是 nc 命令

    nc -x 127.0.0.1:3000 %h %p

%h表示目标地址，%p是目标端口

完成

## 吐槽

一开始看着http.proxy 没当回事， ssh上传一直不成功， 后来突然想通了， 这是 http/https， 不是 ssh协议， 难怪git一直push不上去， 初看 ssh 配置代理好像很麻烦（特别是一眼没看到 windows版本的，万一没有呢）， 于是研究了下 [用Nginx配置git的HTTP服务器](config-centOS-install-git-nginx-server.html)， 一研究5个小时没结果。 回头再用 ssh配代理， 5分钟搞定， 这样浪费时间会死人的！！！
