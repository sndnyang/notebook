Title: shell技巧  
Slug: shell-tricks    
Date: 2017/4/17 18:55:05
Authors: sndnyang sndnyang.github.io
Category: shell  
Modified: 2017/4/24 9:18:56
Tags: shell  

[TOC]

# 有效技巧

## 防止变量未赋值

    set -o nounset / set -u

使用这个选项可以使脚本在使用未初始化的变量时直接退出

## shell 字符串变量中的空格

示例：

    x=" dokjd    "


1. 保留全部空格：  
        echo "$x"
2. 去除头尾空格:  
        echo $x

## shell string总结

1. 空串判断 if [ -z "$line" ]
2. 在awk使用时，全部是数字的外部string变量需要前后加双引号，不然会当作数值，打印时会出bug
3. for循环遍历文件时，使用 for line in `cat $filename` 缺点: 当行内有空格时，一行会被划分成两行
4. 上一条的替代方法 while read line do done &lt; filename 缺点：过程中需要 命令行交互时， 无法输入命令。

## shell 字符串格式化

和C相似

    printf "%-12s" "$x"

awk 和 c 的几乎一样

    awk ' { printf "%s-%s", $1, $2 } '


## 二次赋值

### 数组中二次赋值

    i=1;
    x[1]=2;
    echo ${x[$i]}

### eval 变量二次赋值

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

## 参数太长

如 rm -f * 删除当前路径下所有文件时，可能文件太多，报错Argument list too long

解决方法:

    ls | xargs rm -f

写个循环也行，但是肯定没有上面一句就搞定简单。

## 判断操作系统 uname


## 历史命令记录

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
