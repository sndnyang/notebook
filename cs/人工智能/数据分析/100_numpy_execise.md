Title: 100个numpy小练习   
Date: 2017-04-11 21:15
slug: 100-numpy-excercises
category: 数据分析     
tags: CS, 数据分析, python 

# 100 个numpy小练习

The goal is both to offer a quick reference for new and old users and to
provide also a set of exercices for those who teach. If you remember
having asked or answered a (short) problem, you can send a pull request.
The format is:

本教程的目标是为新手老手提供快速参考及一系列练习题。

#. Find indices of non-zero elements from [1,2,0,0,4,0]

   .. code:: python

      # Author: Somebody

      print np.nonzero([1,2,0,0,4,0])
Here is what the page looks like so far:
<http://www.loria.fr/~rougier/teaching/numpy.100/index.html>


## 译者注

前面是基础应用， 所以可以练一练， 但后面部分感觉偏 科学计算， 我没怎么遇到这样的问题， 所以也没翻译下来， 另外， 我有一些地方没看懂。

# Note

这段Note 我就不管了

The level names came from an old-game (Dungeon Master)


Repository is at: <https://github.com/rougier/numpy-100>


The corresponding [IPython
notebook](https://github.com/rougier/numpy-100/blob/master/README.ipynb)
is available from the github repo, thanks to the
[rst2ipynb](https://github.com/esc/rst2ipynb) conversion tool by
[Valentin Haenel](http://haenel.co)


Thanks to Michiaki Ariga, there is now a [Julia
version](https://github.com/chezou/julia-100-exercises).


## Neophyte 新手

Import the numpy package under the name `np`

导入numpy包， 命名为np


```python
import numpy as np
from neophyte import *
```

Print the numpy version and the configuration.



```python
print np.__version__
```

请编写相应代码（一般就一行或几行）， 使 assert 通过。

练习使用示例：

将 [1,2,5,6,90] 转成 np.array

练习1 Create a null vector of size 10

创建一个 长度为10，每个值都为0的向量 （或长度为任意）， 重点是 零向量、0向量的生成


```python
# 给 your_xxx 赋值
your_vector = None

assert check1(your_vector), "0 向量生成出错"
assert isinstance(your_vector, np.ndarray), "转换 np.array 失败"
```



练习2 Create a null vector of size 10 but the fifth value which is 1

生成一个长度为10的0向量， 修改第5个元素的值 = 1。 重点：向量按下标修改、赋值


```python
your_vector = None

assert check2(your_vector), "向量下标修改出错"
```

练习3. Create a vector with values ranging from 10 to 49

创建从 10到49的向量， 重点是区间范围， 如 range()


```python
your_vector = None
assert check3(your_vector), "生成某区间向量出错"
```

练习4. Create a 3x3 matrix with values ranging from 0 to 8

创建3x3矩阵， 值从0到8。 重点是array的变形， 数组、矩阵的size变换


```python
your_vector = None
assert check4(your_vector), "某区间向量转换成指定行列矩阵出错"
```

练习5. Find indices of non-zero elements from [1,2,0,0,4,0]

查找 [1,2,0,0,4,0] 里的非零元素，并返回下标。

重点： numpy 里 非零 非0 函数


```python
test_case = [1,2,0,0,4,0]
your_vector = None
assert check5(your_vector, test_case), "向量非0元素索引出错"
```

练习6. Create a 3x3 identity matrix

生成单位矩阵的方法


```python
your_matrix = None
assert check6(your_vector), "生成单位矩阵出错"
```

练习7. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

对角矩阵 ， 对角线下


```python
your_matrix = None
assert check7(your_matrix), "对角矩阵变换出错"
```

练习8. Create a 3x3x3 array with random values

多维array, 随机数值。 随机初始化


```python
np.random.seed(2)
dim = (3, 3, 3)
your_array = None
assert check8(your_array, dim), "生成指定维度 随机数值 array 出错"
```

下面可以对比代码


```python
%load neophyte.py
```

## Novice 新手2


```python
from novice import *
```

2.1 Create a 8x8 matrix and fill it with a checkerboard pattern

创建8x8矩阵， 赋值模式：

[[0 1 0 1 0 1 0 1]  
 [1 0 1 0 1 0 1 0]  
 [0 1 0 1 0 1 0 1]  
 [1 0 1 0 1 0 1 0]  
 [0 1 0 1 0 1 0 1]  
 [1 0 1 0 1 0 1 0]  
 [0 1 0 1 0 1 0 1]  
 [1 0 1 0 1 0 1 0]]

重点， array 下标 步调， 批量赋值


```python
your_matrix = None
assert check1(your_matrix), "checkerboard模板失败"
```

2.2 Create a 10x10 array with random values and find the minimum and maximum
values

10x10 随机矩阵中的最大最小值



```python
np.random.seed(25)
your_vector = None
ymin, ymax = 0, 0
assert check2(ymin, ymax), "最值检查"
```

2.3 Create a checkerboard 8x8 matrix using the tile function

使用 tile 函数实现 2.1 的矩阵。



```python
your_matrix = None
assert check3(your_matrix), "checkerboard模板失败"
```

2.4 Normalize a 5x5 random matrix (between 0 and 1)

对5x5随机矩阵进行归一化


```python
np.random.seed(30)
Z = np.random.random((5,5))
your_matrix = None
assert check4(your_matrix), "矩阵归一化失败"
```

2.5 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

数组、矩阵相乘， 矩阵乘法， 非对位相乘


```python
x = np.ones((5,3))
y = np.ones((3,2))
your_matrix = None
assert check5(your_matrix), "矩阵相乘错误"
```

2.6 Create a 5x5 matrix with row values ranging from 0 to 4

创建矩阵， 每行都是 0到4， 不知道这个重点是什么。

矩阵matrix和数组（向量vector）相加的结果


```python
Z = None
assert check6(Z), "错误"
```

    [[ 0.  1.  2.  3.  4.]
     [ 0.  1.  2.  3.  4.]
     [ 0.  1.  2.  3.  4.]
     [ 0.  1.  2.  3.  4.]
     [ 0.  1.  2.  3.  4.]]
    [0 1 2 3 4]
    

2.7 Create a vector of size 10 with values ranging from 0 to 1, both
excluded

创建向量， 平均分， 值范围0到1，但不含0与1.

重点 线性空间 方法 line space


```python
Z = None
assert check7(Z), "矩阵错误"
```

2.8 Create a random vector of size 10 and sort it

创建长度为10的向量， 并排序


```python
np.random.seed(30)
Z = None
assert check8(Z), "矩阵错误"
```

2.9 Consider two random array A anb B, check if they are equal.

判断浮点数数组、矩阵、向量的相近， 是否相等


```python
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = None
assert check9(equal, A, B), "错误"
```


    

    NameErrorTraceback (most recent call last)

    <ipython-input-4-a48e828cbe69> in <module>()
          2 B = np.random.randint(0,2,5)
          3 equal = None
    ----> 4 assert check9(equal, A, B), "错误"
    

    NameError: name 'check9' is not defined


2.10 Create a random vector of size 30 and find the mean value

平均值 方法


```python
Z = np.random.random(30)
m = None
assert check9(Z, m), "错误"
```


```python
%load novice.py
```

## Apprentice 新手3


```python
from apprentice import *
```

3.1 Make an array immutable (read-only)

使 数组、矩阵 不可改


```python
Z = None
assert check1(Z), "错误"
```

3.2 Consider a random 10x2 matrix representing cartesian coordinates,
convert them to polar coordinates

创建 笛卡儿坐标数据 10x2 , 转成 极坐标


```python
Z = np.random.random((10,2))
R = None
T = None
assert check2(Z, R, T), "错误"
```

3.3 Create random vector of size 10 and replace the maximum value by 0

寻找最大值 及 坐标， 同理 最小值、 平均值等


```python
Z = np.random.random(10)
Z[Z.argmax()] = 0
print Z
```

3.4 Create a structured array with `x` and `y` coordinates covering the
[0,1]x[0,1] area.

看不懂， 结构数组 x,y坐标， 覆盖 什么鬼


```python
Z = np.zeros((10,10), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,10),
                             np.linspace(0,1,10))
print Z
```

    [[( 0.        ,  0.        ) ( 0.11111111,  0.        )
      ( 0.22222222,  0.        ) ( 0.33333333,  0.        )
      ( 0.44444444,  0.        ) ( 0.55555556,  0.        )
      ( 0.66666667,  0.        ) ( 0.77777778,  0.        )
      ( 0.88888889,  0.        ) ( 1.        ,  0.        )]
     [( 0.        ,  0.11111111) ( 0.11111111,  0.11111111)
      ( 0.22222222,  0.11111111) ( 0.33333333,  0.11111111)
      ( 0.44444444,  0.11111111) ( 0.55555556,  0.11111111)
      ( 0.66666667,  0.11111111) ( 0.77777778,  0.11111111)
      ( 0.88888889,  0.11111111) ( 1.        ,  0.11111111)]
     [( 0.        ,  0.22222222) ( 0.11111111,  0.22222222)
      ( 0.22222222,  0.22222222) ( 0.33333333,  0.22222222)
      ( 0.44444444,  0.22222222) ( 0.55555556,  0.22222222)
      ( 0.66666667,  0.22222222) ( 0.77777778,  0.22222222)
      ( 0.88888889,  0.22222222) ( 1.        ,  0.22222222)]
     [( 0.        ,  0.33333333) ( 0.11111111,  0.33333333)
      ( 0.22222222,  0.33333333) ( 0.33333333,  0.33333333)
      ( 0.44444444,  0.33333333) ( 0.55555556,  0.33333333)
      ( 0.66666667,  0.33333333) ( 0.77777778,  0.33333333)
      ( 0.88888889,  0.33333333) ( 1.        ,  0.33333333)]
     [( 0.        ,  0.44444444) ( 0.11111111,  0.44444444)
      ( 0.22222222,  0.44444444) ( 0.33333333,  0.44444444)
      ( 0.44444444,  0.44444444) ( 0.55555556,  0.44444444)
      ( 0.66666667,  0.44444444) ( 0.77777778,  0.44444444)
      ( 0.88888889,  0.44444444) ( 1.        ,  0.44444444)]
     [( 0.        ,  0.55555556) ( 0.11111111,  0.55555556)
      ( 0.22222222,  0.55555556) ( 0.33333333,  0.55555556)
      ( 0.44444444,  0.55555556) ( 0.55555556,  0.55555556)
      ( 0.66666667,  0.55555556) ( 0.77777778,  0.55555556)
      ( 0.88888889,  0.55555556) ( 1.        ,  0.55555556)]
     [( 0.        ,  0.66666667) ( 0.11111111,  0.66666667)
      ( 0.22222222,  0.66666667) ( 0.33333333,  0.66666667)
      ( 0.44444444,  0.66666667) ( 0.55555556,  0.66666667)
      ( 0.66666667,  0.66666667) ( 0.77777778,  0.66666667)
      ( 0.88888889,  0.66666667) ( 1.        ,  0.66666667)]
     [( 0.        ,  0.77777778) ( 0.11111111,  0.77777778)
      ( 0.22222222,  0.77777778) ( 0.33333333,  0.77777778)
      ( 0.44444444,  0.77777778) ( 0.55555556,  0.77777778)
      ( 0.66666667,  0.77777778) ( 0.77777778,  0.77777778)
      ( 0.88888889,  0.77777778) ( 1.        ,  0.77777778)]
     [( 0.        ,  0.88888889) ( 0.11111111,  0.88888889)
      ( 0.22222222,  0.88888889) ( 0.33333333,  0.88888889)
      ( 0.44444444,  0.88888889) ( 0.55555556,  0.88888889)
      ( 0.66666667,  0.88888889) ( 0.77777778,  0.88888889)
      ( 0.88888889,  0.88888889) ( 1.        ,  0.88888889)]
     [( 0.        ,  1.        ) ( 0.11111111,  1.        )
      ( 0.22222222,  1.        ) ( 0.33333333,  1.        )
      ( 0.44444444,  1.        ) ( 0.55555556,  1.        )
      ( 0.66666667,  1.        ) ( 0.77777778,  1.        )
      ( 0.88888889,  1.        ) ( 1.        ,  1.        )]]
    

3.5 Print the minimum and maximum representable value for each numpy scalar type

最大可表示值


```python
for dtype in [np.int8, np.int32, np.int64]:
   print np.iinfo(dtype).min
   print np.iinfo(dtype).max
for dtype in [np.float32, np.float64]:
   print np.finfo(dtype).min
   print np.finfo(dtype).max
   print np.finfo(dtype).eps
```

Create a structured array representing a position (x,y) and a color
(r,g,b)



```python
 Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                   ('y', float, 1)]),
                    ('color',    [ ('r', float, 1),
                                   ('g', float, 1),
                                   ('b', float, 1)])])
print Z
```

3.6 Consider a random vector with shape (100,2) representing coordinates,
find point by point distances

100个平面点间的距离计算， scipy 科学计算的接口


```python
Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print D

# Much faster with scipy
import scipy.spatial
Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print D
```

3.7 Generate a generic 2D Gaussian-like array

2维高斯数组


```python
X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
D = np.sqrt(X*X+Y*Y)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
print G
```

3.8 How to tell if a given 2D array has null columns ?

两维数组 是否存在 null列，空列， 那空行呢？


```python
# Author: Warren Weckesser

Z = np.random.randint(0,3,(3,10))
print (~Z.any(axis=0)).any()
```

3.9 Find the nearest value from a given value in an array

寻找 数组（向量）中 与给定值最接近， flat 接口


```python
Z = np.random.uniform(0,1,10)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print m
```

## Journeyman

Consider the following file:

1,2,3,4,5
6,,,7,8
,,9,10,11
How to read it ?

numpy 读取 csv、矩阵 文件


```python
Z = np.genfromtxt("missing.dat", delimiter=",")
```

Consider a generator function that generates 10 integers and use it to
build an array

用生成器来创建数组


```python
def generate():
    for x in xrange(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print Z
```

Consider a given vector, how to add 1 to each element indexed by a
second vector (be careful with repeated indices) ?

给定一个向量， 用另一个向量作为下标， 给相应下标的该向量 +1 加一


```python
# Author: Brett Olsen

Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print Z
```

How to accumulate elements of a vector (X) to an array (F) based on an
index list (I) ?

看不懂


```python
# Author: Alan G Isaac

X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
print F
```

    [ 0.  7.  0.  6.  5.  0.  0.  0.  0.  3.]
    

Considering a (w,h,3) image of (dtype=ubyte), compute the number of
unique colors

寻找 特殊（独一） unique



```python
# Author: Nadav Horesh

w,h = 16,16
I = np.random.randint(0,2,(h,w,3)).astype(np.ubyte)
F = I[...,0]*256*256 + I[...,1]*256 +I[...,2]
n = len(np.unique(F))
print np.unique(I)
```

Considering a four dimensions array, how to get sum over the last two
axis at once ?

四维数组， 如何一次对后两维？axis 求和。


```python
A = np.random.randint(0,10,(3,4,3,4))
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print
```

Considering a one-dimensional vector D, how to compute means of subsets
of D using a vector S of same size describing subset indices ?



```python
# Author: Jaime Fernández del Río

D = np.random.uniform(0,1,100)
S = np.random.randint(0,10,100)
D_sums = np.bincount(S, weights=D)
D_counts = np.bincount(S)
D_means = D_sums / D_counts
print D_means
```

Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3
consecutive zeros interleaved between each value ?

在向量所有值之间插入


```python
# Author: Warren Weckesser

Z = np.array([1,2,3,4,5])
nz = 3
Z0 = np.zeros(len(Z) + (len(Z)-1)*(nz))
Z0[::nz+1] = Z
print Z0
```

Consider an array of dimension (5,5,3), how to mulitply it by an array
with dimensions (5,5) ?

5x5x3维数组， 与 5x5组数组 相乘， 高维与低维相乘， 像卷积神经网络里的？


```python
A = np.ones((5,5,3))
B = 2*np.ones((5,5))
print A * B[:,:,None]
```

How to swap two rows of an array ?



```python
# Author: Eelco Hoogendoorn

A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print A
```

## Craftsman

Consider a one-dimensional array Z, build a two-dimensional array whose
first row is (Z[0],Z[1],Z[2]) and each subsequent row is shifted by 1
(last row should be (Z[-3],Z[-2],Z[-1])



```python
# Author: Joe Kington / Erik Rigtorp
from numpy.lib import stride_tricks

def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.itemsize, a.itemsize)
    return stride_tricks.as_strided(a, shape=shape, strides=strides)
Z = rolling(np.arange(10), 3)
print Z
```

Consider a set of 10 triplets describing 10 triangles (with shared
vertices), find the set of unique line segments composing all the
triangles.



```python
# Author: Nicolas P. Rougier

faces = np.random.randint(0,100,(10,3))
F = np.roll(faces.repeat(2,axis=1),-1,axis=1)
F = F.reshape(len(F)*3,2)
F = np.sort(F,axis=1)
G = F.view( dtype=[('p0',F.dtype),('p1',F.dtype)] )
G = np.unique(G)
print G
```

Given an array C that is a bincount, how to produce an array A such that
np.bincount(A) == C ?



```python
# Author: Jaime Fernández del Río

C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print A
```

How to compute averages using a sliding window over an array ?

如何使用 滑动窗口计算平均值


```python
# Author: Jaime Fernández del Río

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
Z = np.arange(20)
print moving_average(Z, n=3)
```

## Artisan

Considering a 10x3 matrix, extract rows with unequal values (e.g.
[2,2,3])



```python
# Author: Robert Kern

Z = np.random.randint(0,5,(10,3))
E = np.logical_and.reduce(Z[:,1:] == Z[:,:-1], axis=1)
U = Z[~E]
print Z
print U
```

Convert a vector of ints into a matrix binary representation.



```python
# Author: Warren Weckesser

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128])
B = ((I.reshape(-1,1) & (2**np.arange(8))) != 0).astype(int)
print B[:,::-1]

# Author: Daniel T. McDonald

I = np.array([0, 1, 2, 3, 15, 16, 32, 64, 128], dtype=np.uint8)
print np.unpackbits(I[:, np.newaxis], axis=1)
```

## Adept

Consider an arbitrary array, write a function that extract a subpart
with a fixed shape and centered on a given element (pad with a `fill`
value when necessary)

# Author: Nicolas Rougier

Z = np.random.randint(0,10,(10,10))
shape = (5,5)
fill  = 0
position = (1,1)

R = np.ones(shape, dtype=Z.dtype)*fill
P  = np.array(list(position)).astype(int)
Rs = np.array(list(R.shape)).astype(int)
Zs = np.array(list(Z.shape)).astype(int)

R_start = np.zeros((len(shape),)).astype(int)
R_stop  = np.array(list(shape)).astype(int)
Z_start = (P-Rs//2)
Z_stop  = (P+Rs//2)+Rs%2

R_start = (R_start - np.minimum(Z_start,0)).tolist()
Z_start = (np.maximum(Z_start,0)).tolist()
R_stop = np.maximum(R_start, (R_stop - np.maximum(Z_stop-Zs,0))).tolist()
Z_stop = (np.minimum(Z_stop,Zs)).tolist()

r = [slice(start,stop) for start,stop in zip(R_start,R_stop)]
z = [slice(start,stop) for start,stop in zip(Z_start,Z_stop)]
R[r] = Z[z]
print Z
print R
Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to
generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ...,
[11,12,13,14]] ?



```python
# Author: Stéfan van der Walt

Z = np.arange(1,15,dtype=uint32)
R = stride_tricks.as_strided(Z,(11,4),(4,4))
print R
```

## Expert

Consider two arrays A and B of shape (8,3) and (2,2). How to find rows
of A that contain elements of each row of B regardless of the order of
the elements in B ?



```python
# Author: Gabe Schwartz

A = np.random.randint(0,5,(8,3))
B = np.random.randint(0,5,(2,2))

C = (A[..., np.newaxis, np.newaxis] == B)
rows = (C.sum(axis=(1,2,3)) >= B.shape[1]).nonzero()[0]
print rows
```

Extract all the contiguous 3x3 blocks from a random 10x10 matrix.



```python
# Author: Chris Barker

Z = np.random.randint(0,5,(10,10))
n = 3
i = 1 + (Z.shape[0]-3)
j = 1 + (Z.shape[1]-3)
C = stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
print C
```

Create a 2D array subclass such that Z[i,j] == Z[j,i]



```python
# Author: Eric O. Lebigot
# Note: only works for 2d array and value setting using indices

class Symetric(np.ndarray):
    def __setitem__(self, (i,j), value):
        super(Symetric, self).__setitem__((i,j), value)
        super(Symetric, self).__setitem__((j,i), value)

def symetric(Z):
    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)

S = symetric(np.random.randint(0,10,(5,5)))
S[2,3] = 42
print S
```

Consider a set of p matrices wich shape (n,n) and a set of p vectors
with shape (n,1). How to compute the sum of of the p matrix products at
once ? (result has shape (n,1))



```python
# Author: Stéfan van der Walt

p, n = 10, 20
M = np.ones((p,n,n))
V = np.ones((p,n,1))
S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
print S

# It works, because:
# M is (p,n,n)
# V is (p,n,1)
# Thus, summing over the paired axes 0 and 0 (of M and V independently),
# and 2 and 1, to remain with a (n,1) vector.
```

## Master

Given a two dimensional array, how to extract unique rows ?


## Note

See
[stackoverflow](http://stackoverflow.com/questions/16970982/find-unique-rows-in-numpy-array/)
for explanations.



```python
# Author: Jaime Fernández del Río

Z = np.random.randint(0,2,(6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void, Z.dtype.itemsize * Z.shape[1])))
_, idx = np.unique(T, return_index=True)
uZ = Z[idx]
print uZ
```

## Archmaster

（原文仅到Archmaster, 后续自己添加的) 恭喜完成本练习， 对 numpy 应该掌握得比较好了。



```python
# %load checker.py

import numpy as np

def check1(x):
    if x is None:
        return False
    right = np.zeros(len(x))
    return np.array_equal(x, right)

def check2(x):
    if x is None:
        return False
    right = np.zeros(len(x))
    right[4] = 1
    return np.array_equal(x, right)

def check3(x):
    if x is None:
        return False
    right = np.arange(10, 50)
    return np.array_equal(x, right)

def check4(x):
    if x is None:
        return False
    right = np.arange(9).reshape(3,3)
    return np.array_equal(x, right)
    
if __name__ == "__main__":
    
    right = np.arange(9).reshape(3,3)
    print right
    assert check4(right)
    
```
