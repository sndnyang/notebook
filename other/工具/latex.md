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


# 疯狂吐槽AAAI模板

    \usepackage{amsmath,amsfonts}

这两个ams包没有默认加入， 坑死我了。


# 三段式表格


```
\usepackage[flushleft]{threeparttable}


\begin{center}

\begin{threeparttable}

\begin{tabular}{lc}

\toprule

\midrule

\midrule

\bottomrule

\end{tabular}

\end{threeparttable}

\end{center}

```



# newif

使用newif定义一个逻辑（二值）变量`logvar` 

 define a logical variable `logvar` as follows:

```latex
\newif\iflogvar
\newif\iflogvar\logvarfalse
\newif\iflogvar\logvartrue
\newif\if@logvar\@logvarfalse
```

第一种

By default, it is set to `false`. We can set it to `true` by:

```latex
\logvartrue
```

# 边缘空白过多

[remove white space after table](https://mylatexnotes.wordpress.com/2017/09/13/table-remove-white-space-after-table/)

```latex
\vspace{-4mm}
\end{figure}
\end{table}
```

But the instruction in AAAI said that don't use vspace. 但AAAI的模板里明确说了不要用vspace。