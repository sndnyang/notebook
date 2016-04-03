Title: FOCS总结 
Slug: FOCS_summary
Date: 2016-03-01
category: 研究
Tags: 论文

[TOC]

# 基本定义
图： G(V, E)

目标—— 找到一簇子图(全部并正确)， 每个子图都是一个团（community)
即 $ S = \{S_i | S_i \subset V \} $

团（community)： 子图中任意点在该子图中的连通性 高于 非团的子图

定义 包含点 $ v_j $ 的团的集合为：

$$ S(v_j) = \{S_i | v_j \in S_i \land S_i \in S \} $$

disjoint cluster:   

$$ |S(v_j)| \le 1 $$

overlapped cluster: > 1

定义 $ N(v_j) $ 为 $v_j$ 的邻接点

定义 $ N_i(v_j) $ 为 $v_j$ 在团 $S_i$ 的邻接点， 即 
$$ N_i(v_j) =\{v_k | (v_j, v_k) \in E \land v_k \in S_i \} $$

# 新概念定义

团连通性 community connectedness, 即点 $v_j$在团$S_i$邻点超阈值个数 除以 该团点数, 代表 点对应团的归属性。

$$ \zeta^i_j = \frac{|N_i(v_j)|-K+1}{|S_i| - K} if |N_i(v_j)| > K, else, 0 $$

邻接连通性 neighborhood connectedness， 即 点 $v_j$在团$S_i$邻点数 除以 $v_j$的总邻点数， 代表 点加入新团的可能性

$$ \xi^i_j = \frac{|N_i(v_j)|}{|N(v_j)|}  $$ 

外围结点 peripheral node: $v_i$的团邻接点

$$ Added_i = \{v_k|v_k \in N(v_i) \land v_k \in S_i \}, \forall S_i \in S^l $$

# 步骤

## 初始化

初始化全部有K个以上邻接点的点， 由它及其邻接点组成团 $S_i$

定义该阶段的外围结点

## 脱离阶段

1. 对前面所有团里的点 $ V_j$, 计算相应的

	1. 团连通性 $ \zeta^i_j $
	2. 邻接连通性 $ \xi^i_j $

2. 将[0, 1] 区间划分为 $max(20, N(v_j))$ 块， 每块初始化为0.
3. 根据团连通性分数， 统计各区间 点的个数。
4. 标记 最右的非0元， 并开始向左遍历， 直到：
	1. 遍历完毕 或
	2. 遇到某区间，<=标记值(最右非零元)， 且<=左边区间值， 这个值选为 留存阈值 stay cut-of of \zeta
5. 外围结点 $v_k \in Added_i $ 排除出 $S_i$ , 当团连通性分数 $ \zeta^i_k $ 比留存阈值低。
6. Removal of only
peripheral nodes ensures that nodes that form the core of a
community are never eliminated

## 扩充阶段

对上一阶段处理后的团中所有点$v_j$， 当以下条件满足：
1. 该点未入 $ S_i$团
2. 该点选入 $S_i$团的可能性高（即 邻接连通性 $\xi^i_j$ 高于选中阈值 join cut-off ）

join cut-off 选中阈值的计算方式与 stay 相同

## 去重阶段



# 代码描述

## 参考链接

[focs-code](/focs-notebook.html)


{% notebook cs/论文/FOCS.ipynb %}




