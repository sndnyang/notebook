Title:  Unsupervised Learning of Probably Symmetric Deformable 3D Objects From Images 
Slug:  Unsupervised_Learning_Deformable_3D_Objects  
Date: 2014/5/20 13:14:20  
Authors: sndnyang sndnyang.github.io  
Category:  论文导论  
Tags: 论文, 人工智能   
Summary:   天天读论文导论和摘要  

[TOC]

# 论文名

Unsupervised Learning of Probably Symmetric Deformable 3D Objects From Images in the wild

# 会议

CVPR-2020

# 关键字

unsupervised learning, 3D reconstruction

# 个人总结

无监督、单视角图片训练， 之后就可以三维重建，  帅！

用AUTOENCODER把图片因子化， 分解出 深度、反照率albedo, 视角, 和 光照

利用物品的对称结构， 对光照效果进行推理 能利用上物体的对称性， 之后对（多半对称的）物体建模， 通过先端到端学习模型其他部件后预测出对称概率图。 we model objects that are probably symmetric by predicting a symmetry probability map, learned end-to-end with the other components of the model.

stereo reconstruction

explicitly model illumination

o reason about potential lack of symmetry in the objects.

To do this, the model predicts, along with the other factors, a dense map containing the probability that a given pixel has a symmetric counterpart in the image.



不过没有基础概念， 不会~~~



# 赞踩

5分赞