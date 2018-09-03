kernel 1:

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