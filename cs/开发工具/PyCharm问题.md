Title: PyCharm的一些问题
Slug: issues-of-pycharm  
Date: 2019-02-02 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)     
Tags: PyCharm    
Category: 开发工具    
Summary: PyCharm使用时遇到的一些问题  
  
[TOC]

# can't find .so only in pycharm

	ImportError: libcudnn.so.7: cannot open shared object file: No such file or directory
	
1. run pycharm from terminal.

2. There is an another way in Ubuntu/CentOS/Linux/Unix: change the quick start file:`etbrains-pycharm.desktop`, which can be found in `/usr/share/applications/` or `~/.local/share/applications/`, just depends on pycharm's installation.
then modify this line:

	```shell
	Exec = /...
	```

	into

	```shell
	Exec = bash -i -c /...
	```

then restart your pycharm, u'll find bug fixed.

因为 PyCharm默认的桌面/菜单应用 加载不了 ~/.bashrc， 所以一些额外的库找不到， 使用 LD_LIBRARY_PATH 这些方案很麻烦， 比较方便的有两种：

1. 从命令行启动
2. 修改PyCharm 桌面应用文件， 在`/usr/share/applications/` 或 `~/.local/share/applications/`里面， 修改
		```
		Exec = /path/pycharm.sh
		```
		改成

		```
		Exec = bash -i -c /path/pycharm.sh
		```
        
# ssh远端开发，找不到远端的包， nothing to show

使用 2018.1 版本能显示， 不过 os, traceback 等一些也看不到， 2018.3 以上就开始无法显示， 有说使用ip地址、删除~/.pycharm_helper 可以解决这问题， 但我试了没成功。

Using version 2018.1 can show most packages. But I can't find os,traceback etc. If I use the pycharm higher than 2018.3, it will show that nothing to show. In the forum, someone said using ip address, deleting ~/.pycharm_helper directory will solve this issue. However I tried both, neither works.
