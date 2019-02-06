Title: PyTorch问题   
Date: 2018-12-19 22:18:30
slug: PyTorch-issues
category: 深度学习   
tags: 深度学习 机器学习, 人工智能  
Modified: 2018-12-19 22:18:30

[TOC]

# 函数里的内存占用不释放

比如, 使用的函数

    def pairwise_distances(x, y=None):
        """
        Input: x is a Nxd matrix
            y is an optional Mxd matrix
        Output: dist is a NxM matrix where dist[i,j] is the square norm between x[i,:] and y[j,:]
                if y is not given then use 'y=x'.
        i.e. dist[i,j] = ||x[i,:]-y[j,:]||^2
        """
        n = x.size(0)
        d = x.size(1)
        if y is None:
            y = x

        m = y.size(0)
        x_expand = x.unsqueeze(1).expand(n, m, d)
        y_expand = y.unsqueeze(0).expand(n, m, d)

        dist = torch.pow(x_expand - y_expand, 2).sum(2).cpu()
        return dist

如果不在倒数第二行使用 .cpu()， 经常出现，函数返回后，占用的GPU内存不被释放, 有时是覆盖掉，有时干脆累加， 分分钟撑爆GPU内存

# torch 1.0/0.4.1 

	libtorch_python.so: undefined symbol: _Z11libshm_initPKc
	
When I installed the torch 1.0,  there's a libshm.so in the $LD_LIBRARY_PATH.

Just remove the path from $LD_LIBRARY_PATH, and reinstall. 
