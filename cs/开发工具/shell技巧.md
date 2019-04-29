Title: bash技巧  
Slug: shell-bash-tricks    
Date: 2017/4/17 18:55:05
Authors: sndnyang sndnyang.github.io
Modified: 2017/4/24 9:18:56
Tags: shell, bash, ksh  

[TOC]

# Emacs 模式快捷键

注： 对VIM比较熟悉，就不写了

[参考网页1](http://www.xuexixinde.com/xitong/62.html) 和 [参考2](http://www.linuxde.net/2011/11/1877.html)

## 光标移动

        Ctrl-a：移动到行首
        Ctrl-e：移动到行尾
        Ctrl-b：向左移动一个字符
        Ctrl-f：向右移动一个字符
        Esc-b：向左移动一个单词
        Esc-f：向右移动一个单词

## 删除
        Ctrl-h：删除光标左方的字符
        Ctrl-d：删除光标所在的字符
        Esc-d：删除从光标开始到单词结束
        Ctrl-w：删除从光标开始到单词首部
        Ctrl-k：删除光标右边的所有字符
        Ctrl-u：删除光标左方的所有字符

## 复原操作
        Ctrl-_：恢复之前的状态

## 粘贴
        Ctrl-y：把之前删除的字符或字符串，贴到光标所在位置

## 重复操作
        Esc-操作次数 操作动作：指定操作次数，重复执行指定的操作

## 历史指令相关
        Ctrl-r：向前搜索历史指令
        Ctrl-p：调出上一个指令
        Ctrl-n：调出下一个指令
        Esc-<：调出编号最小的历史指令
        Esc->：移动到编号最大的历史指令的后面，就是现命令行

## 补齐
        Esc-~：补齐用户名
        Esc-$：补齐变量名
        Esc-@：补齐主机名

## 大小写转换
        Esc-u：光标到单词尾部转换为大写
        Esc-l：光标到单词尾部转换为小写
        Esc-c：光标所在位置到单词尾部这段首字母大写

# 防止变量未赋值

    set -o nounset / set -u

使用这个选项可以使脚本在使用未初始化的变量时直接退出

# 字符串变量中的空格

示例：

    x=" dokjd    "


## 1.保留全部空格

        echo "$x"

## 2. 去除头尾空格:

        echo $x

# shell string总结

1. 空串判断 if [ -z "$line" ]
2. 在awk使用时，全部是数字的外部string变量需要前后加双引号，不然会当作数值，打印时会出bug
3. for循环遍历文件时，使用 for line in `cat $filename` 缺点: 当行内有空格时，一行会被划分成两行
4. 上一条的替代方法 while read line do done &lt; filename 缺点：过程中需要 命令行交互时， 无法输入命令。

# 字符串格式化输出

和C相似

    printf "%-12s" "$x"

awk 和 c 的几乎一样

    awk ' { printf "%s-%s", $1, $2 } '


# 二次赋值

## 数组中二次赋值

    i=1;
    x[1]=2;
    echo ${x[$i]}

## eval 变量二次赋值

见证奇迹的时刻:

    first_item="PROJECT_NAME"
    eval $first_item="LB03"
    echo $PROJECT_NAME

结果是

    LB03

引申到数组的利用上

    set -A array_name "PROJECT_NAME" "BRANCH"
    set -A array_value "LB03" "DEV"
    eval ${array_name[1]}=${array_value[1]}
    echo "BRANCH =" $BRANCH

结果应该是

    BRANCH = DEV

# 参数太长

如 rm -f * 删除当前路径下所有文件时，可能文件太多，报错Argument list too long

解决方法:

    ls | xargs rm -f

写个循环也行，但是肯定没有上面一句就搞定简单。

# 带空格文件删除

find ./ -name '*.bak' -print0 | xargs -0 rm -rf

# 判断操作系统

    uname

# 历史命令记录

!的使用

- !!重复前一个命令
- !字符 重复前一个以“字符”开头的命令
- !num 按照history命令输出中的序号来重复对应命令
- !?abc 重复前一个包含abc的命令 *这个最好用*
- !-n 重复n个命令之前的那个命令
- !$ 上一个命令的最后一个参数

按键组合:

⑴使用up和down键来上下浏览之前执行的命令
⑵键入ctr+r来在命令历史中搜索命令

# shell脚本中判断上一个命令是否执行成功

    if [[ $? -ne 0 ]]; then
        echo "failed"
    fi