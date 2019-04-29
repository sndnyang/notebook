Title: TensorFlow和PyTorch如何结果一致   
Date: 2019-3-18 22:18:30
slug: TensorFlow-PyTorch-get-same-outputs
category: 深度学习   
tags: 深度学习, 机器学习, 人工智能  
Modified: 2019-3-18 22:18:30

[TOC]

# github

[repo](https://github.com/sndnyang/DeepLearningCMP)

[nbviewer tf eager](https://nbviewer.jupyter.org/github/sndnyang/DeepLearningCMP/blob/master/tf_eager.ipynb)

[nbviewer pytorch](https://nbviewer.jupyter.org/github/sndnyang/DeepLearningCMP/blob/master/pytorch.ipynb)

# 求导, gradient

    torch.autograd.grad(f_x[:, 0], logits, grad_outputs=torch.ones_like(f_x[:, 0]))

    tp.gradient(f_x[:, 0], logits)

# 优化器, optimizer

    torch_optimizer = optim.SGD(list(model.parameters()), lr, momentum=0.9, nesterov=True)

    optimizer = tf.train.MomentumOptimizer(lr, momentum=0.9, use_nesterov=True)
    
# BatchNorm

Converting a batch normalization layer from TF to Pytorch


    bn_layer = nn.BatchNorm2d(num_filters, eps=EPS, momentum=MOMENTUM, affine=False).to(device)
    p = bn_layer(images)
    
    bn_layer = tf.layers.BatchNormalization(axis=-1, momentum=MOMENTUM, epsilon=EPS)
    p = bn_layer(m, training=True)
    print("output\n", p.numpy())
    print("sum of output**2\n", (p.numpy()**2).sum())
    p = tf.layers.batch_normalization(m, training=True, momentum=MOMENTUM, epsilon=EPS)
    print("output\n", p.numpy())
    print("sum of output**2\n", (p.numpy()**2).sum())
    
## 代码示例

    tf.set_random_seed(1)
    m = tf.random_uniform((2, 3, 3, 1), 0, 1)
    print("random input\n", m.numpy())
    print("sum of random input\n", m.numpy().sum())
    images = torch.FloatTensor(m.numpy()).to(device)
    images = images.permute(0, 3, 1, 2)
    bn_layer = nn.BatchNorm2d(1, eps=EPS, momentum=MOMENTUM, affine=False).to(device)
    p = bn_layer(images)

    print("output\n", p.cpu().numpy())
    print("sum of output**2\n", (p.cpu().numpy() ** 2).sum())

    
    tf.set_random_seed(1)
    m = tf.random_uniform((2, 3, 3, 1), 0, 1)
    print(m)
    print(m.numpy().sum())
    bn_layer = tf.layers.BatchNormalization(axis=-1, momentum=MOMENTUM, epsilon=EPS)
    p = bn_layer(m, training=True)
    print("output\n", p.numpy())
    print("sum of output**2\n", (p.numpy()**2).sum())

    p = tf.layers.batch_normalization(m, training=True, momentum=MOMENTUM, epsilon=EPS)
    print("output\n", p.numpy())
    print("sum of output**2\n", (p.numpy()**2).sum())


# Dropout

# deterministic 

    PyTorch
    torch.backends.cudnn.deterministic = True
    
    
    TensorFlow
    没找到, didn't find

    