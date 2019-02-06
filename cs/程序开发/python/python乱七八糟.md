Title: python乱七八糟
Slug: something-strange-on-python    
Date: 2017/4/24 22:25:32
Authors: sndnyang sndnyang.github.io
Modified: 2017/4/24 22:26:28
Category: Python  
Tags: Python  

[TOC]

# 说明

一堆乱七八糟的东西


# scipy 安装不了

windows下 scipy 安装有问题，报错~~~什么 MKL的，忘了，没记录

# numpy 安装

pip 安装虽然也行，但好像不全

安装这里的 numpy

    http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

# 不知道这个是什么

AttributeError: MSVCCompiler instance has no attribute 'compiler_so'

error: Unable to find vcvarsall.bat

似乎需要在 windows下指定 mingw的环境，所以 

python setup.py build -c mingw32

还需要安装mingw， 不然什么 gcc，及头文件都没有。


# 文件格式不识别

Cython error: C:\Python27\libs/libpython27.a: error adding symbols: File format not recognized

gendef c:/Windows/System32/python27.dll
dlltool -U -d python27.def -l libpython27.dll.a
cp libpython27.dll.a c:/Python27/libs

# 生成0KB文件

## gendef

放到 /mingw??/bin 下， 即可

## dlltool

我是这样解决的：
通过cmd命令进入.dll和.def文件所在目录，再运行dlltool.exe，即可。注意，在命令行输入dlltool的完整路径名。如下图所示。

[百度贴吧](http://tieba.baidu.com/p/3804600448)

# _imp __Py_InitModule4

Python: undefined reference to `_imp __Py_InitModule4'

[stackoverflow](http://stackoverflow.com/questions/2842469/python-undefined-reference-to-imp-py-initmodule4)


Look in:

C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin


# __pyx_t_5numpy_int32_t

http://blog.csdn.net/jiajunlee/article/details/50373815#q9-invalid-conversion-from-const-int-to-int


# 

compiler = os.path.basename(sysconfig.get_config_var("CC"))
compiler = "C:\MinGW\bin\gcc.exe"

https://github.com/pyne/pyne/issues/27

# python 2 3, cPickle and pickle 

	python 3 pickle 'ascii' codec can't decode byte 0x8a in position 3: ordinal
	
解决方案： [website](https://blog.csdn.net/qq_41185868/article/details/79039604)

	.load(f,encoding='bytes')


