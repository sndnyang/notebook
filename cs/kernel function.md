kernel function



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
   