Title: 核函数kernel function汇总
Date: 2018-11-15 22:18:30
slug: kernel-function
category: 机器学习   
tags: 机器学习, 人工智能  
Modified: 2018-11-25 22:18:30



1. 多项式核函数



2. 高斯核函数

   RBF(radial basis function) 函数
   $$
   k(x, x') = exp(-\frac{1}{h} || x - x'||^2)
   $$
   对应 gradient:
   $$
   \nabla_xk(x, x') = \sum \frac{2}{h} (x' - x)k(x, x')
   $$

3. KL-div 核函数
   $$
   k(x, x') = k(P(x) - P(x')) = P(x) log{\frac{P(x)}{P(x')}}
   $$
   对应 gradient:
   $$
   \begin{aligned}
   \nabla_x k(x, x') = & \nabla(P(x)\log P(x) - P(x)\log P(x')) \\
   = & \nabla(P(x) \log P(x)) - \log P(x') \nabla P(x) \\
   = & \log P(x) \nabla P(x) + P(x) \nabla \log P(x) - \log P(x') \nabla P(x) \\
   = & P(x) \log P(x) \nabla \log P(x) + P(x) \nabla \log P(x) - P(x) \log P(x') \nabla \log P(x) \\
   = & (\log P(x) + 1 - \log P(x')) P(x) \nabla \log P(x) \\
   = & (P(x) \log \frac{P(x)}{P(x')} + P(x)) \nabla \log P(x) \\
   = & (k(x, x') + P(x) ) \nabla \log P(x)
   \end{aligned}
   $$
   
   
1. RBF(radial basis function) 函数
   $$
   x = \theta \\
   k(x, x') = exp(-\frac{1}{h} || x - x'||^2)
   $$
   对应 gradient:
   $$
   \nabla_xk(x, x') = \sum \frac{2}{h} (x' - x)k(x, x')
   $$

2. RBF(radial basis function) 函数

$$
x = \theta \\
k(x, x') = k(P(x), P(x')) = exp(-\frac{1}{h} || P(x) - P(x')||^2)
$$

对应 gradient:
$$
\nabla_xk(x, x') = \sum \frac{2}{h} (\nabla P(x') - \nabla P(x)) k(P(x), P(x'))
$$

1. 