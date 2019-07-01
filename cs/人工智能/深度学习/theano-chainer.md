Title: Theano-Chainer   
Date: 2019-2-19 22:18:30   
slug: Theano-Chainer-issues   
category: 深度学习   
tags: 深度学习 机器学习, 人工智能  
Modified: 2019-12-19 22:18:30    

[TOC]

# Chainer 

## Installation to use GPU 安装


The backend is cupy. Choose the right version of cuda.

Chainer 后端用的是cupy，需要根据cuda版本选择。

If your cudnn path is not in the $CUDA_PATH directory, you must set:

如果你的 cudnn 安装位置和 cuda不是同一个文件夹， 安装前必须设置以下环境变量：

    export CFLAGS=-I/path/to/cudnn/include
    export LDFLAGS=-L/path/to/cudnn/lib
    export LD_LIBRARY_PATH=/path/to/cudnn/lib:$LD_LIBRARY_PATH

Refer to these two links: [install cupy](https://docs-cupy.chainer.org/en/latest/install.html#install-cupy), and [install cudnn](https://docs-cupy.chainer.org/en/latest/install.html#installing-cudnn-and-nccl)


## initialize/update the weight by numpy

Reference to [normal initializer](https://github.com/chainer/chainer/blob/v5.2.0/chainer/initializers/normal.py#L10)

Its implementation is different from PyTorch. 


# Theano

要使用 GPU 的话， 需要 pygpu 库， 好像只能用 conda 安装， pip 是找不到这个库的.

We need pygpu library to utilize GPU, so it seems that only conda support pygpu, I can't find the library by pip.

tensorboardX need to use pip to install.



## 安装建议 suggestion

python 2.7 直接使用 conda install theano pygpu 



python 3 可能更有效方式， 分两步

1. conda install pygpu  or  conda install theano pygpu
2. update theano using pip. pip install theano==1.0.4



### Error information

1. Mixed dnn version. The header is version xxx  while the library is version  yyyy
2. theano seems not work > 3.5
3. conda only has theano==1.0.2, but I encounter the 1. mixed dnn version problem.