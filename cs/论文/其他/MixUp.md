Title: Mixup
Slug: mixup-method
Date: 2020/5/04 19:48:09
Authors: sndnyang sndnyang.github.io
Modified: 2020/5/04 12:46:38
Category: 论文    
Tags: 论文, 深度学习
Summary:   

[TOC]

# 方法

$$
\begin{array}{l}
\tilde{x}=\lambda x_{i}+(1-\lambda) x_{j} \\
\tilde{y}=\lambda y_{i}+(1-\lambda) y_{j}
\end{array}
$$

**Mixup** extends the training distribution by incorporating the prior knowledge that **linear

interpolations** of feature vectors should lead to linear interpolations of the associated targets.

![image-20200504233144918](E:\project\blog\content\cs\论文\其他\images\mixup)`

## 其他

这篇论文方法非常简单， 不过细看下发现还有很多内容被忽略。

目的是解决以下问题：

- 记忆训练数据
- 对抗样本
- 同时能提高准确率

Empirical Risk Minimization(ERM) 经验风险最小化原则（可看李航《统计学习方法》）

1. 最小化经验风险只能在训练集上做到 -> 会导致网络记住数据而无泛化能力
2. 训练数据越多， 神经网络规模就应该越大 -> 矛盾是： 要保证ERM的可收敛性， 则网络（模型）的规模（size）不能随训练数据的增加一起变大


Vicinal Risk Minimization (VRM) 邻域风险最小化, 进行数据增广（data augmentation)


# 个人总结

## 疑问：

The size of these state-of-theart neural networks scales linearly with the number of training examples. ？？？ 还有这回事？


## 有意思的

learning theory

VC-complexity 不变， the convergence of ERM is guaranteed as long as the size of the learning machine (e.g., the neural network) does not increase with the number of training data. 

## 

