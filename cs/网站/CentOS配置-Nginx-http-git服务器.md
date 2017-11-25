Title: CentOS配置-Nginx用作git的HTTP服务器
Date: 2017-08-27 20:44:20
slug: config-centOS-install-git-nginx-server
tags: Linux, CentOS, git
summary: centos 配置 Nginx给GIT当服务器， 没成功
Type: code

# 总

没成功

折腾了一天， 经历了 

1. nginx 路径匹配错误——根路径习惯问题
2. 密码错误（password mismatch）, 因为 htpasswd 需要 加参数 -d, 没有这个参数生成的密码不被 nginx 支持
3. 文件和文件夹权限问题（403）， 一直没发现 Nginx 跑的 work process 用户是 nginx， 我的服务器权限是root， 花的时间最多
4. 502 怀疑是 git-http-backend 的问题， nginx 应该是没问题了， 只有超时， 不是 fcgi的问题就是 git-http-backend的问题，但查不出来

花了6、7个小时搞不定， 最后还是回归到了 ssh 如何加代理上， 3分钟搞定~~~
