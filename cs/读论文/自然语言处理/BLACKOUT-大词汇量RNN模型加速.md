Title: BLACKOUT-大词汇量RNN模型加速
Slug: BLACKOUT-SPEEDING-UP-RECURRENT-NEURAL-NETWORK-LANGUAGE-MODELS-WITH-LARGE-VOCABULARIES
Date: 2017/9/28 19:48:09
Authors: sndnyang sndnyang.github.io
Modified: 2017/9/28 12:46:38
Category: 自然语言处理    
Tags: 论文, 自然语言处理,  RNN, 人工智能   
Summary:   

[TOC]


# 摘要

论文[^1]

方法特点： 近似算法，通过 discriminative loss（是什么得看后面介绍） 和 weighted sampling strategy（具体得看后面）来训练RNN语言模式

像 DropOut(深度学习里的那个)的外层扩展， 因为都是采样吧~~~

# 导论

## 历史介绍

### Bengio的神经网络语言模型

处理n元模型里的数据稀疏问题。

方案：用连续（非离散）向量空间来表达历史上下文。 连续值非离散值， 就能计算错误率。 

初学者还没看过这篇

### 递归神经网络

处理固定词数问题， 用递归隐藏层可以表示任意长度的上下文（句子）。

很经典——初学者没看过具体内容（那个隐藏层里的函数用什么没看过）， 更没实现过， 接下来看看。

没学过也不能装学过~~~

主要问题是， 矩阵运算遇到超大词汇向量怎么办。

所以要想办法降维、 近似， 降低计算量。

## 

## 实现细节

# 实验

目前还看不懂实验部分


# 啰嗦点其他的

很久没看了（本来看得就少）， 申请不顺利（说不挑，我对排名是不挑，但别的方面上总之自作孽了）， 难过。

[^1]: BLACKOUT: SPEEDING UP RECURRENT NEURAL NETWORK
LANGUAGE MODELS WITH VERY LARGE VOCABULARIES, Shihao Ji, S. V. N. Vishwanathan, Nadathur Satish, Michael J. Anderson, Pradeep Dubey

