Title: Deep Bayesian Active Learning with Image Data
Slug: Deep Bayesian Active Learning with Image Data
Date: 2018/5/18 19:48:09
Authors: sndnyang sndnyang.github.io
Modified: 2018/5/18 19:48:09
Category: 论文    
Tags: 论文, 主动学习,  深度学习, 计算机视觉, 人工智能   
Summary:   

[TOC]


# 摘要

1. 深度学习对大数据的依赖
2. 主动学习 active learning 的获取函数（acquisition function）是基于模型不确定性的（model uncertainty）， 而深度学习的方法在模型不确定性上应用不多

所以本文用 Bayesian贝叶斯深度学习来做主动学习， 贝叶斯深度学习可以评估模型不确定性， 进而用不确定性选点

# 主动学习 Active Learning

从少量数据中学习， 不仅能做预测（分类、回归）， 同时能预测自己预测的结果的准确性（不确定性）， 不确定性高的数据则需要专家来进行标注——不确定性高的数据标注后，又有一批数据的预测结果更可信了， 所以能提高数据有效性， 减少人工标注的工作量。 这就是 active learning 的目标、定义。

代码实现中， 从少量训练数据开始，没问题， 比如 MNIST 取20、100、 1000个作为初始数据， 专家标注过程则需要用训练数据的另一部分来代替， 因为不可能在实验中真的弹窗出来请人标注。

代码框架：

	主动学习框架过程
	输入： 初始选定的小训练数据集T， 和 未标注数据集P（pool data set） —— 即，将原始训练集划分成小训练数据集、 未标注集， 有需要的话， 还可以有验证集 validation data set）
	
	使用 T 训练初始模型C（分类或回归都行）
	repeat:
		1. 用 C 对 U 进行标注（预测）
		2. 计算未标注数据集 U 中数据标注结果的不确定性，不确定性高，比如可以用 熵 Entropy 表现， 选择若干 最大熵的数据， 要求人工标注
		3. 把这些数据移到训练集L中， 即用原始训练集里已有的标注 label, 代表 专家人工标注的过程
		4. 使用 L 训练模型C ， 好像一般是训练一个新的， 但也不一定需要重新 训练初始模型C（分类或回归都行）
	
# Bayesian CNN

主要是采样， 采样才有近似后验概率， 不确定性、熵主要用同一数据多次预测结果的后验概率来表示， 所以也需要采样， 需要在 测试阶段也使用 dropout， 进而用 monte carlo 的方式算概率， 所以这叫 MC dropout。 而标准dropout在测试阶段不生效， 同一数据跑多少次结果都相同

# 获取函数 Acquisition Function

## 回归问题

使用predictive variance， 即多次MC dropout误差范围

## 分类问题：

1. 最大熵 Max Entropy:  $$H[y|x, D_{train}] = - \sum_c p(y=c|x, D_{train}) log(y=c|x,D_{train})$$

2. 互信息mutual information最大化BALD： $$ I[y, \omega|x, D_{train}] = H[y|x, D_{train}] - E_{p(\omega|D_{train})}[H[y|x,\omega]]$$

3. 最大化变化率 Variation Ratios： $$ vr[x] = 1-\frac{f_x}{T}$$
$f_x = \sum_tI[y^t=c^*]$ and $c^*$ 是 ${y^t}$的模 mode

4. 最大化均值方差： $$\sigma(x) = \frac{1}{C}\sum_c \sqrt{E_{q(\omega)}[p(y=c|x,\omega)^2]-E_{q(\omega)}[p(y=c|x,\omega)]^2}$$

