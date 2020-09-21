Title: 神经网络的单点对抗攻击  
Date: 2020-4-6 16:20:20  
slug: adversarial-features-not-bugs
category: 论文  
tags: adversarial, 论文  

[TOC]

# 概述

## 提问

After read the title  AEs are not bugs, they are features.

THe first question: what are features? in the datasets? how can we capture those features. Types? non-robust and robust? Can the generator or optimizer optimize to learn it with a specific network?

bugs? yes, previously researchers think those are bugs. That's natural thoughts.

So if I'm the author. How can I find this observation. 是怎么发现这一现象的， 不这不是现象， 他们只是试着换了一个思维方式。 既然是特征， 特征一定 能提取， 就一定 有方法提取特征， 再去评估特征的 特征， 应该是这样了。
基本分析就是这样， 接下来猜 方法、算法。
既然特征是存在类别， 并且是学出来的， 但没有label标记哪些是， 他的模型是怎么学的呢， 这个是真有意思， 跟我的工作也比较接近， 把特征提出来， 留下的又是什么， 如果是01式的提取就最好的， 对吧。 可以试试。 方法还是没想到， 加油！怎么改进也还太着急， 
