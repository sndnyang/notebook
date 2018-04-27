Title: Keras技巧  
Date: 2018-4-25 22:18:30
slug: keras-tricks
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
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
set_session(tf.Session(config=config))

[引用CSDN](https://blog.csdn.net/sinat_26917383/article/details/75633754)

