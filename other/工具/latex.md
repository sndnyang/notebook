Title: latex  
Slug: latex-tips  
Date: 2018-04-02 09:05:05  
Author: sndnyang (sndnyangd@gmail.com)     
Tags: 科研, 工具
Category: 科研      
Summary: latex 坑
  
[TOC]

# bad math environment delimiter 

\begin{equation} 替换 $$, 不能嵌套

# label 标签、公式交叉引用

	\begin{equation}
		\begin{aligned}
		p(y=c|x, D_{train}) = & \int p(y=c|x,w)p(w|D_{train})dw \\
		\approx & \int p(y=c|x,w)q^*_{\theta}(w)dw \\
		\approx & \frac{1}{T} \sum_{t=1}^{T} p(y=c|x,\hat{w}_t)  
		\end{aligned}
	\label{bayesian_posterior}
	\end{equation}


	\ref{bayesian_posterior}

	
# No positions in optional float specifier.

\begin{figure}[] or \begin{table}[]

# 表格太宽

	\documentclass{article}
	\usepackage{graphicx}
	\begin{document}

	\begin{table}
	\resizebox{\textwidth}{!}{%
	  \begin{tabular}{cc}
		Knuth & Lamport
	  \end{tabular}}
	\end{table}

	\end{document}
	
# 代码算法显示 input output

	\renewcommand{\algorithmicrequire}{\textbf{Input:}} % Use Input in the format of Algorithm
	\renewcommand{\algorithmicensure}{\textbf{Output:}} % Use Output in the format of Algorithm
