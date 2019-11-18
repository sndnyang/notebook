Title: conda给虚拟环境配置环境变量
Slug: conda-config-environment-variable  
Date: 2019-10-10 09:05:05   
Author: sndnyang (sndnyangd@gmail.com)  
Tags: tool   
Category: 开发工具    
Summary: conda在所创建的环境里配置环境变量
  
[TOC]

# 配置

网上找到的中文介绍都是给整个conda配置环境变量， 但如何给 conda创建的虚拟环境设置单独的环境变量， 基本没找到中文的（virtualenv 那个直接在activate文件里添加环境变量 export var_name="abcde")

英文官网关于管理虚拟环境的 [manage environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment)

在激活了某个conda的虚拟环境之后, 进行如下管理：

1. 找到并进入该conda环境的主文件夹（目录） echo $CONDA_PREFIX ; cd $CONDA_PREFIX
2. 创建如下子文件夹和文件：  
```
mkdir -p ./etc/conda/activate.d  
mkdir -p ./etc/conda/deactivate.d  
touch ./etc/conda/activate.d/env_vars.sh  
touch ./etc/conda/deactivate.d/env_vars.sh  
```
3. 在activate.d/env_vars.sh文件里添加、修改环境变量， 在deactivate.d/env_vars.sh恢复原环境变量或注销你新加的变量  
