Title: TensorBoard  
Date: 2019-7-25 22:18:30
slug: TensorBoard-tricks
category: 深度学习   
tags: 深度学习 机器学习, 人工智能  
Modified: 2019-7-25 22:18:30

[TOC]

# Load tfevents file



如何读取tfevents文件， 太多内容似是而非、过时、不准确， 只会把人弄晕。



现总结如下：



TF不同版本的接口变动太大， 为保证准确性， 给出我当前版本: tensorflow-gpu==1.10.1 



如果只是为了读tfevents文件， 有这一个版本就好了， 但以后2.0稳定了，甚至搞3.0了， 可能会觉得这个版本太老。。。以后再说吧， 现在能用就好， 估计 前后几个版本的接口应该是一致的。



读取方式：

## EventAccumulator

```python
from tensorboard.backend.event_processing import event_accumulator
event_acc = event_accumulator.EventAccumulator(p)
event_acc.Reload()
print(event_acc.Tags()["scalars"])
l = event_acc.Scalars('Test/Acc')
print(l[0].step, l[0].value)
```



## summary_iterator

tf.train.summary_iterator， 但不好用， 都不知道遍历了什么样的数据类型， 怎么拿到具体值