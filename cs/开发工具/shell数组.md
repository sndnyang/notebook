Title: shell数组
Slug: shell-array    
Date: 2017/4/17 19:01:08
Authors: sndnyang sndnyang.github.io    
Modified: 2017/4/17 19:09:40
Tags: shell, bash, ksh 

[TOC]

# 声明数组

    declare -a myarray

在函数中还可以用local 来声明数组
 
    local -a myarray
 
# 数组赋值
 
2.1.对于shell能返回多个值的，可以直接赋值，比如

    myarray=`ls *.bin 2>/dev/null`

这条语句把当前目录下所有的.bin文件赋值给myarray
 
2.2.也可以从让用户输入

    read -a myarray
 
# 用索引值来访问

    ${array[0]}='test'
 
# 数组追加值\新元素

    myarray=(${myarray[*]} test);

或

    hobbies=("${activities[@]}" diving})
 
# 打印数组所有的值
 
    echo ${myarrra[*]};

或

    echo ${myarrra[@]};
 
# 逐一读出数组的值

    for item in ${myarray[*]};
    do
        echo $item;
    done;
 
 
# 清空数组

    uset ${myarray}

或

    myarray=
 
 
