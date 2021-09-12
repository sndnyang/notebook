Title: NVAE: A Deep Hierarchical Variational Autoencoder
Slug: NVAE
Date: 2020/10/21 23:48:09
Authors:  论文  
Category: 论文    
Tags: 论文
Summary:   

[TOC]















![nvae_title](./images./image-20201021233022061.png)

发表NIPS2020  [Arxiv](http://arxiv.org/abs/2007.03898)












<div style="page-break-after: always;"></div>





# 问题

VAE的多数研究， 都集中在统计方面， 比如 近似分布和真实后验分布的差别。没有太多研究网络结构的工作，都是直接拿分类任务的网络结构。

但问题是：

1. VAE 最 ?  化 输入和隐变量的  ?,  所以网络应该保留输入的信息内容， 但根据信息瓶颈学说，分类任务会丢失信息——这话显然不是指全扔了~~~
2. VAE 面对过参数(over-parameterization)时，反应不一样respond differently（就并不好的意思？），因为 边缘对数似然marginal log-likelihood只依赖于生成模型， 解码器（生成）过参数化可能影响 测试的log-likelihood。
3. KL散度的无界性， 训练 非常深的VAE 同样不稳定（GAN/MCMC/VAE~~~没一个稳定的）



所以本文*make VAEs great again*， 通过结构设计， 和使之稳定（谱正则化spectral regularization）





