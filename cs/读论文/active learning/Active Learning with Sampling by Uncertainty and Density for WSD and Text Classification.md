Title: Active Learning with Sampling by Uncertainty and Density for WSD and Text Classification
Slug: Active Learning with Sampling by Uncertainty and Density for WSD and Text Classification
Date: 2018/5/18 19:48:09
Authors: sndnyang sndnyang.github.io
Modified: 2018/5/18 19:48:09
Category: 论文    
Tags: 论文, 自然语言处理,  深度学习, 主动学习, 人工智能   
Summary:   

[TOC]


# 摘要

两个问题

1. 不确定性采样时， 容易选择离群点
2. 初始训练数据集优化

对应方法：

1. SUD: Sampling by Uncertainty and Density
2. SBC: Sampling By Clustering

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
	

# 不确定性评估Uncertainty Measures

又名获取函数 Acquisition Function

## 1. 最大熵 

Max Entropy:  

$$H[y|x, D_{train}] = - \sum_c p(y=c|x, D_{train}) log(y=c|x,D_{train})$$

## 2. 密熵

即密度加熵， 作者使用 二者相乘而不是 $ \lambda * DS(x) + (1-\lambda)*Entropy(x)$

KNN-density K-Nearest-Neighbor-Based density



