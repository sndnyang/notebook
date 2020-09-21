Title: FindBugs总结
Date: 2016-3-3 21:20:20
slug: findbugs_summary
category: 软件工程
tags: 论文, CS, 软件工程  

[TOC]

原文: Finding Bugs is Easy by David Hovemeyer, William Pugh

# 摘要

旧方法基于 formal methods 和 复杂程序分析， 难用， 无作用


bug patterns  -  detectors

简单的自动技术在遇到常规错误和难解特性时都有用

# 导论

## conclusion

1. 不存在这种bug, 过于明显，以至于在实际代码中没有找到例子——发现的bug中，有些十分明显， 让我们吃惊， 即使是在生产应用和库里
2. 现代OO语言的高度复杂性， 对语言特性及API的滥用是屡见不鲜的。 
3. 自动bug检测可以在 程序正确性 上起到巨大作用

