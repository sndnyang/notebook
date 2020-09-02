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



# 相关



1. Mixup ICLR 2018

2. manifold Mixup ICML 2019

3. AdaMixUp  MixUp as Locally Linear Out-Of-Manifold Regularization   AAAI 2019

4. CutMix ICCV2019(oral)

5. AugMix ICLR2020

6. Puzzle Mix  ICML'20

7. Mixup+SemiSL->MixMatch  NIPS2019 

8. ReMixMatch  ICLR2019

9. Mixup+Defense->Mixup Inference ICLR 2020

10. On Mixup Training Improved Calibration and Predictive Uncertainty  NIPS2019

11. Nonlinear Mixup: Out-Of-Manifold Data Augmentation for Text Classification. AAAI 2020

12. Adversarial Domain Adaptation with Domain Mixup  AAAI2020

13. Active Mixup for Data-Efficient Knowledge Distillation, CVPR2020

14. Adversarial Vertex Mixup, CVPR2020

    

1. Manifold Mixup for Few-shot Learning WACV2020
2. Improving Short Text Classification Through Global Augmentation Methods CD-MAKE 2020
3. Manifold Mixup Improves Text Recognition with CTC Loss  ICDAR2019
4. Spatial Mixup IEEE ACCESS



1. MetaMixup  未中
2. SuperMix （被拒， 未中）
3. Rethinking Image Mixture (unsupervised)   未中
4. GraphMix (ICLR 被拒， 未中)
5. FixMatch (MixMatch->ReMixMatch->FixMatch(+UDA+Cutout)未中)
6. MixUp as Directional Adversarial Training (NIPS2019  ICLR2020 连拒， 未中)

Hongyu Guo,  一人薅了4篇， 2篇AAAI， 2篇 arxiv