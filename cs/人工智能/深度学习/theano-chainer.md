Title: Theano-Chainer   
Date: 2019-2-19 22:18:30
slug: Theano-Chainer -issues
category: 深度学习   
tags: 深度学习 机器学习, 人工智能  
Modified: 2019-12-19 22:18:30

[TOC]

# Chainer 

Use cupy....The installation is a bit complex. Need to be careful about the environment variables.

## initialize/update the weight by numpy

Reference to [normal initializer](https://github.com/chainer/chainer/blob/v5.2.0/chainer/initializers/normal.py#L10)

Its implementation is different from PyTorch.


# Theano

要使用 GPU 的话， 需要 pygpu 库， 好像只能用 conda 安装， pip 是找不到这个库的.

We need pygpu library to utilize GPU, so it seems that only conda support pygpu, I can't find the library by pip.

tensorboardX need to use pip to install.