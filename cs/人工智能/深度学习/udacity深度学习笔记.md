Title: udacity深度学习笔记   
Date: 2016-10-25 23:15
slug: udacity-deep-learning-notes
category: 机器学习   
tags: CS, 机器学习, 人工智能, 深度学习  

[TOC]

# 总结

udacity的课程还是讲得不深入，蜻蜓点水式的讲了一点内容， 记不了多少内容。 没做他提供的练习， 感觉不是很值得。

## 大纲

四部分：

1. 基础？   
    1. 逻辑回归做分类——然而好像没给出模型式子，只给了损失函数
    2. 随机优化（随机梯度下降）
    3. 数据和参数调试——并没有讲多少的样子
2. 初试   
    1. 深度网络
    2. 正则化
3. 卷积神经网络 convolution neural network
4. 应用   
    1. 嵌入 embedings
    2. 词向量 Word2Vec
    3. Recurrent Models
    4. LSTM

## softmax

$$
S(y_i) = \frac{e^{y_i}}{\sum_j e^{y_j}}
$$

## One-Hot encoding

没整明白

## cross-entropy

熵

## 

**输入**， 经过线性模型（逻辑回归）转成， **Logits**， 再经过softmax转成， **概率值**， 再与**one-hot encoding labels** 一起计算 cross entropy。

以上就是 multinomial logistic classification

## 其他

提到以下内容：

1. SGD 随机梯度下降
-  rule of 30-- 影响到验证集中30个样例的可以被相信
-  交叉验证可能很慢，所以更多数据往往是正确方法
-  SGD技巧：       
    1. 动量(momentum): 即保存梯度的移动平均（running average): $$ M = 0.9M + \Delta J$$, 没确认视频里的符号是什么。
    2. 学习速率衰减(learning rate decay)
-  Rectified linear units(ReLUs)
-  前向反向传播forward/back propagation
-  early termination: stop before overfitting
-  $L_2$ regularization
-  dropout 丢弃法
-  cnn    
    - pooling 池化， max pooling 和 mean pooling
    - 1x1 conv
    - inception
- 应用一堆 

