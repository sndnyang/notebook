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



# Load several projects in one directory/windows 一个目录加载多个项目/工程

[方案来源]( https://www.cnblogs.com/mrgavin/p/6382406.html )

PyCharm好用， 但一个比较麻烦的玩意是一个窗口最好只打开一个项目， 主目录要对应， 导入自己写的其他模块才不会有错误提示。 PyCharm is a very useful/helpful/pragmatic tool. But there's an issue that one PyCharm window should only open one project. And the working directory should be the root of the project. Then it won't raise error when loading other modules/packages in my project.

 ![img](https://images2015.cnblogs.com/blog/941639/201702/941639-20170209152610010-288461141.jpg) 



在一个窗口里想同时加载多个项目或主目录没对应上的话， 导入模块就会有错误提示， 虽然有时候有错误提示也能运行， 但对强迫症来说， 恨不得把所有错误警告都消灭掉， 有错误提示就非常不能忍， 而且多数情况下，也确实无法运行。



之前也试过寻找方案，但没找到，这次随手一搜，居然就搜到了

```
Settings->Project->Project Structure->Add Content Root
```



不过不能使用