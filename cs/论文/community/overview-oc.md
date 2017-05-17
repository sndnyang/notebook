Title: 社区覆盖问题总结   
Date: 2016-03-04
Slug: overlap_communities_survey  
category: 数据挖掘
Tags: 社区发现, CS, 算法

[TOC]

# 算法

## 1. Clique Percolation
中文名？派系过滤

### 假设

群落由 完全连通子图的重叠集合组成——a community consists of overlapping sets of fully connected subgraphs

### 思路

detects communities by searching for adjacent cliques

### 扩展内容

1. 派系(Cliques)。在一个无向网络图中，“派系”指的是至少包含3个点的最大完备子图。这个概念包含3层含义：①一个派系至少包含三个点。②派系是完备的，根据完备图的定义，派系中任何两点之间都存在直接联系。③派系是“最大”的，即向这个子图中增加任何一点，将改变其“完备”的性质。
2. n-派系(n-Cliques)。对于一个总图来说，如果其中的一个子图满足如下条件，就称之为n-派系：在该子图中，任何两点之间在总图中的距离(即捷径的长度)最大不超过n。从形式化角度说，令d(i,j)代表两点和n在总图中的距离，那么一个n-派系的形式化定义就是一个满足如下条件的拥有点集的子图，即：d(i,J)\le n，对于所有的，n_i,n_j\in N,来说，在总图中不存在与子图中的任何点的距离不超过n的点。
3. n-宗派(n—Clan)。所谓n-宗派(n—Clan)是指满足以下条件的n-派系，即其中任何两点之间的捷径的距离都不超过n。可见，所有的n-宗派都是n-派系。
4. k-丛(k-Plex)。一个k-丛就是满足下列条件的一个凝聚子群，即在这样一个子群中，每个点都至少与除了k个点之外的其他点直接相连。也就是说，当这个凝聚子群的规模为n时，其中每个点至少都与该凝聚子群中n-k个点有直接联系，即每个点的度数都至少为n—k。

### 某个的步骤之一

1. begins by identifying all cliques of size k in a network, a new graph is constructed such that each vertex represents one of these k-cliques

### 结论
more like pattern matching rather than finding communities since they aim to find specific, localized structure in a network.

## 2. Line Graph and Link Partitioning
中文名？连接划分

### 思路
1. partitioning links
2. A node in the original graph is called overlapping if links connected to it are put in more than one cluster.

## 3. Local Expansion and Optimization

中文名？局部增广和优化

### 思路
1. based on growing a natural community or a partial community
2. rely on a local benefit function that characterizes the quality of a densely connected group of nodes

## 4. Fuzzy Detection
中文名？模糊检测

### 思路
quantify the strength of association between all pairs of nodes and communities

### 例子

Non-negative Matrix Factorization 

## 5. Agent-Based and Dynamical Algorithms

中文名？基于啥的动态算法

### 思路

label propagation algorithm by allowing a node to have multiple labels

## 6. others

中文名——无法分类 :)

# 评估方法

## 1. Normalized Mutual Information
中文名？标准互信息

## 2. Omega Index


# 结论
