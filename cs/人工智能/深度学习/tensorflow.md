Title: TensorFlow技巧  
Date: 2018-4-25 22:18:30
slug: TensorFlow-tricks
category: 深度学习   
tags: 深度学习 机器学习, 人工智能  
Modified: 2018-4-25 22:18:30

[TOC]

# 显卡使用问题

python设置系统变量的方法

	os.environ["CUDA_VISIBLE_DEVICES"] = "8,9,10,11,12,13,14,15"

注意，在代码中指定设备时，重新从0开始计，而不是从8开始。

# 显存使用问题

显卡内存默认占用几乎全部, 可以通过重设backend的GPU占用情况来进行调节

	import tensorflow as tf
	config = tf.ConfigProto()

	config.gpu_options.allow_growth = True

	config.gpu_options.per_process_gpu_memory_fraction = 0.3
	tf.Session(config=config)

[引用CSDN](https://blog.csdn.net/sinat_26917383/article/details/75633754)


# tensorflow cudnn 版本问题

Loaded runtime CuDNN library: 7.0.5 but source was compiled with: 7.2.1

cudnn 7.0.4 对应 tensorflow-gpu==1.10.1 , 1.11, 1.12 默认的 cudnn 版本更新。。。

[cudnn报错解决](https://blog.csdn.net/jy1023408440/article/details/82887479)

# 解决Tensorflow 使用时cpu编译不支持警告

tensorflow 大量信息

	import os  
	os.environ["TF_CPP_MIN_LOG_LEVEL"]='1' # 这是默认的显示等级，显示所有信息  
	os.environ["TF_CPP_MIN_LOG_LEVEL"]='2' # 只显示 warning 和 Error   
	os.environ["TF_CPP_MIN_LOG_LEVEL"]='3' # 只显示 Error

