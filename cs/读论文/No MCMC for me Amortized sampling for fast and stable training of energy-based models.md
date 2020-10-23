Title:  No MCMC for me: Amortized sampling for fast and stable training of energy-based models  
Slug:  No_MCMC_for_me_for_EBM    
Date: 2020/10/22 13:14:20    
Category:  论文  
Tags: 论文     
Summary:   天天论文， 搞个频道  

[TOC]





![image-20201022185833693](images/image-20201022185833693.png)



[OpenReview](https://openreview.net/forum?id=ixpSxO9flk3)







# 问题

## 能量模型定义

$$
p_{\theta}(x)=\\
Z(\theta) = 
$$





用于训练能量模型的MCMC/SGLD ， 很慢（就跟PGD一样要很多步），也很不稳定



