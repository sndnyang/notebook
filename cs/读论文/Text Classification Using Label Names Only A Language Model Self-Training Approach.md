Title: Text Classification Using Label Names Only A Language Model Self-Training Approach  
Slug: Text_Classification_Using_Label_Names_Only   
Date: 2020/10/19 19:48:09    
Authors:  sndnyang   
Category: 自然语言处理     
Tags: 论文, 自然语言处理   
Summary:      

[TOC]









![image-20201019195239055](./images/image-20201019195239055.png)

发表于 EMNLP2020 ，[Arxiv](https://arxiv.org/abs/2010.07245v1)  [github](https://github.com/yumeng5/LOTClass) 

















# 问题 Motivation

给数据加标签，成本很高。

Assigning labels to data can be costly and difficult to obtain those labels in real applications.

人只需要基本的类别的描述、形容，即可进行分类，不需要标签

Human can do classification task only based on a small set of words describing the categories to be classified.

所以，这篇论文就试图研究，如何做到只使用每个类的标签名字（体育、娱乐、时事、金融）去做无监督分类。 only using the label name of each class to train classification models on un- labeled data

*注意* ， 本文是NLP的，不是CV的

已知标签、标签名字，

从单词一级思考

再从句子一级思考做分类训练











1. 句子里的单词 和 标签名字 的语义关系
2. 找哪些词表示了类别 category-indicative words，并训练网络
3. 用自训练self-training(伪标签 pseudo label)对模型进行泛化

LOTClass： Label-Name-Only Text Classification



# 方法

**想：**  我记得这篇论文 The Natural Language Decathlon: Multitask Learning as Question Answering [decaNLP](https://decanlp.com/) 把所有NLP处理问题都视作QA

**想：** 还有另一篇 0-标签识别  [Zero-shot Recognition via Semantic Embeddings and Knowledge Graphs](https://arxiv.org/abs/1803.08035)



## 怎么找单词

考虑BERT的掩码

用BERT的MLM(masked language model掩码语言模型)，预测哪些单词在大多数语境下能替换 *标签名 label name*



![find_word](./images/find_word.png)



对每次出现在语料里的标签名， 有一个语境嵌入（表征）向量 $h \in \mathcal{R}^h$, BERT训练出来的，把这个向量传给 MLM的头部元， 得到一个对所有单词V的概率分布， 即每个单词出现在该位置的似然值。
$$
p(w|\bold{h}) = Softmax(W_2\sigma(W_1\bold{h) + \bold{b}}))
$$


![the bert](./images/image-20201019190115596.png)



<img src="./images/sim_words.png" alt="words" style="zoom:50%;" />



这篇论文里， 每句里选前50， 最终 能替换标签名那个词 最多的 前100个单词， 作为类别相关的词汇表。



## 给句子做无标签的类别预测

就看句子里是否有以上的类别指示词（category-indicative words)， 很简单， 但很容易错 error-prone

![two_meanings](./images/image-20201019185114434.png)

需要掩码训练， 在单词被掩掉的情况下， 预测这个单词对应的类别。 这是有语境的，词一级的，有类别这个监督信息的训练。



定义， $w$的预测TOP50单词视作可行替换词，  $w$ 是不是类别 $c_w$的对应词呢？ 那么 $w$ 的50个可行替换词中，有20个正好也出现在 之前学到的$c_w$ 100个类别对应词汇表， 40%的相似词出现在词汇表里，大概率是了。

按以上方式，对所有语料里每个词进行验证， 就能找到 各个类别的对应词——这里不是类别词汇表了——以及$S_{ind}$ 作为类别标签


$$
L_{MCP} = - \sum_{w,c_w \in S_{ind}} \log P(c_w | \bold{h}_w) \\
p(c|\bold{h}) = Softmax(W_c \bold{h} + \bold{b}_c)
$$


mask out the category-indicative word for category prediction 类别对应词必须掩掉，避免模型就是简单记住。

## 自训练 self-training

当前预测分布 $P$ 和 一个伪标签分布 $Q$ 求 KL 散度

$Q$ 可以用 Hard labeling， soft labeling。

Hard labeling: 高于某阀值的那个类别（one-hot） $q_{ij} = \mathbf{1}(p_{ij} > \tau)$

Soft labeling: 不说了~~~$q_{ij} =\frac{p^2_{ij} / f_j}{\sum_{j'} (p^2_{ij'} / f_{j'})}, f_j=\sum_i p_{ij}$



# 总结

这篇论文干了什么事？

























1. 标签名 ->在bert里 -> 50个相近词 -> 每个类别的100词的词汇表
2. 每个单词 $w$ ->在bert里 -> 50个相近词 -> 20/50 词在词汇表里出现的话， $w$ 就是该类的对应词， 训练
3.  self-training

想法：无







