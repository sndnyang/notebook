Title: 支持向量机系列二之对偶化
Date: 2016-4-19
slug: svm-2-dual
category: 机器学习
tags: CS, AI, Machine Learning
Modified: 2016-05-3
summary: 支持向量机对偶化

[TOC]

## 免责说明

本文参考以下文献：

1. pluskid支持向量机系列博文，特别是图片引用 [pluskid-svm](http://blog.pluskid.org/?page_id=683)
2. Andrew Ng在斯坦福的cs229讲义， [cs229](http://cs229.stanford.edu/materials.html)
3. jerrylead 博文 [jerrylead-svm](http://www.cnblogs.com/jerrylead/archive/2011/03/13/1982684.html), pluskid 的公式显示出问题， 看着头大

在下文笔较烂， 恐贻笑大方。 不过因为是markdown 写的， 有不足， 改进比较方便， 所以欢迎提出意见及建议，找出问题， 谢谢。

# 导读

在上一篇 [svm介绍](http://zhimind.com/tutorial/a94364d4-4f6f-41bd-8b57-6c749efc46f4) 中， 我们已经得到了如下一个公式：

$$ 
\begin{align} 
&\min_{w,b} \frac{1}{2}\|w\|^2 \\
& 
\begin{array}
&
s.t., y_i(w^Tx_i+b)\geq 1, i=1,\ldots,m\\ \end{array}
\end{align}
$$ 

这个式子或者说优化问题 大家都说是有现成的优化方法来求解， 所以完成了一部分内容。

既然已经能用了， 为什么还要继续讲下去， 肯定是有更优的方案。 这也是明摆的事。

如果说上面的多数内容是普通读者(会来学习svm或机器学习的人)能顺利理解每一步公式的话， 后面的内容对于很多人就困难得多了， 特别是对高数没学好的（比如我）来说。

我现在强行凑文章， 也不合适， 还是得先学好数学了再说。

