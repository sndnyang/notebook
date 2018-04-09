Title: bash emacs编辑模式   
Slug: bash-emacs-model    
Date: 2018/4/6 18:55:05
Authors: sndnyang sndnyang.github.io
Modified: 2018/4/6 9:18:56
Tags: shell, bash, emacs

[TOC]


# emacs模式的热键操作：

## 对于字符（ctrl）：

            前移一个字符：ctrl+f

            后移一个字符：ctrl+b

            删除前一字符：ctrl+h

            删除后一字符：ctrl+d

## 对于单词（esc）：

            前移一个单词：esc+f

            后移一个单词：esc+b

            删除前一单词：esc+ctrl+h，或ctrl+w

            删除后一单词：esc+d

            恢复最后删除的项：ctrl+y

## 对于行（ctrl）：

           移到行首：ctrl+a

           移到行尾：ctrl+e

           从光标所在删除直到行首：ctrl+u

           从光标所在删除直到行尾：ctrl+k

           移到前一行：ctrl+p

           移到后一行：ctrl+n

## 对于历史文件（esc）：

           移动到历史文件的首行：esc+<

           移动到历史文件的末行：esc+>

           在历史文件中反向搜索：ctrl+r

# 命令行补齐：

## 通用热键：

           试图补齐命令行：tab

           列出所有可能的备选项：esc+?

## 补齐文件名（/）：

           试图补齐文件名：esc+/

           列出所有备选文件名：ctrl+x+/

## 补齐用户名（~）：

            试图补齐用户名：esc+~

            列出所有备选用户名：ctrl+x+~

## 补齐主机名（@）：

            试图补齐主机名：esc+@

            列出所有备选主机名：ctrl+x+@

## 补齐内置变量（$）：

            试图补齐变量名：esc+$

            列出所有备选变量名：ctrl+x+$

## 补齐命令名（!）：

            试图补齐命令名：esc+!

            列出所有备选命令名：ctrl+x+!

## 补齐历史列表中的命令 名：esc+tab

# 杂项命令：

1. 清 屏：ctrl+l
2. 反转光 标所在字符及其前面的字符：ctrl+t
3. 从光标处开始的整个单词大写：esc+u
4. 从光标处开始的整个单词小写：esc+l
5. 将光标处的单词的首字母大写：esc+c