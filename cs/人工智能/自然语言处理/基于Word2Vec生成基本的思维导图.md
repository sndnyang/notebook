Title: 基于Word2Vec生成基本的思维导图   
Date: 2016-4-28
slug: word2vec-2-mindmap
category: 自然语言处理   
tags: CS, 自然语言处理, 人工智能  

[TOC]

译自：

[原文链接](https://codesachin.wordpress.com/2015/10/15/generating-rudimentary-mind-maps-from-word2vec-models/)(没有找过作者， 随手就翻译了)

思维导图这一工具因其长于组织大量任务、材料信息，在头脑风暴、 计划和问题解决等领域得到广泛使用、一致好评。

对思路的可视整理有助于整个思考的过程， 并且模拟了我们人类思考时获取脑中知识的方式。

现今有很多工具可以帮助我们画出思维导图， 但还没有一个能自行生成的， “生成”是指从文本（语音）内容中提成。

为了做到这一点， 我花了最长的时间（至今快8个月了）， 研究如何结合文本挖掘和图论做成一个框架来生成思维导图（给定一段文本）。

当然， 第一个问题就是， 任意一段文字都不会只有那么一种可行的思维导图。

只是， 如果你要构建自己的思维导图， 有这么一个自动工具， 可能会给你更多的思路和洞见， 特别是头脑风暴时， 或帮你查缺补漏。

那我们先来看看一个思维导图的样式——

![mindmap](https://codesachin.wordpress.com/2015/10/15/generating-rudimentary-mind-maps-from-word2vec-models/)

两个关键点：

* 思维导图并不简单地是一棵树， 不只是递归地将主题划分成子主题。 它本质上更像图， 连接项在语义上是相关的。
* 正如‘夜晚’可能会让你想到‘白天’， 思维导图中， 意义相反的两个概念之间也很可能存在连接。

还有诸如使用图片强化概念等其他点。但这些并不是本文的主旨（我的设计师风格创造力糟透了）。

有备无患 ， [Heres](http://lifehacker.com/how-to-use-mind-maps-to-unleash-your-brains-creativity-1348869811) 这篇文章能帮助你熟悉构建和使用思维导图的过程。

在我上一篇博文 [链接](https://codesachin.wordpress.com/2015/10/09/generating-a-word2vec-model-from-a-block-of-text-using-gensim-python/) 中， 我描述了一种从文本生成Word2Vec模型的方法（使用维基的文章作为示例）。

在这里， 我将描述我使用的从 Word2Vec模型生成基本思维导图的方法。

# 第一步： 从文章中找出前n项
（就像我上一篇博文所说， 我只使用stemmed unigrams（一个词干的n-gram), 你可以自行采用更高阶的ngrams, 想来会更棘手（准确来说， 是当你生成n-gram的算法有效时）

这里的 n 是指思维导图中的节点数， 在我多次尝试之后， 50是个比较好的数字， 太小则信息少， 太大则噪音多。 欢迎尝试其他数字。

我使用了本文 链接 中写的 co-occurrence 方法， 列出文本的前 n 项词。 代码如下：

    def _get_param_matrices(vocabulary, sentence_terms):
        """
        Returns
        =======
        1. Top 300(or lesser, if vocab is short) most frequent terms(list)
        2. co-occurence matrix wrt the most frequent terms(dict)
        3. Dict containing Pg of most-frequent terms(dict)
        4. nw(no of terms affected) of each term(dict)
        """

        #Figure out top n terms with respect to mere occurences
        n = min(300, len(vocabulary))
        topterms = list(vocabulary.keys())
        topterms.sort(key = lambda x: vocabulary[x], reverse = True)
        topterms = topterms[:n]

        #nw maps term to the number of terms it 'affects'
        #(sum of number of terms in all sentences it
        #appears in)
        nw = {}
        #Co-occurence values are wrt top terms only
        co_occur = {}
        #Initially, co-occurence matrix is empty
        for x in vocabulary:
            co_occur[x] = [0 for i in range(len(topterms))]

        #Iterate over list of all sentences' vocabulary dictionaries
        #Build the co-occurence matrix
        for sentence in sentence_terms:
            total_terms = sum(list(sentence.values()))
            #This list contains the indices of all terms from topterms,
            #that are present in this sentence
            top_indices = []
            #Populate top_indices
            top_indices = [topterms.index(x) for x in sentence
                           if x in topterms]
            #Update nw dict, and co-occurence matrix
            for term in sentence:
                nw[term] = nw.get(term, 0) + total_terms
                for index in top_indices:
                    co_occur[term][index] += (sentence[term] *
                                              sentence[topterms[index]])

        #Pg is just nw[term]/total vocabulary of text
        Pg = {}
        N = sum(list(vocabulary.values()))
        for x in topterms:
            Pg[x] = float(nw[x])/N

        return topterms, co_occur, Pg, nw


    def get_top_n_terms(vocabulary, sentence_terms, n=50):
        """
        Returns the top 'n' terms from a block of text, in the form of a list,
        from most important to least.

        'vocabulary' should be a dict mapping each term to the number
        of its occurences in the entire text.
        'sentence_terms' should be an iterable of dicts, each denoting the
        vocabulary of the corresponding sentence.
        """

        #First compute the matrices
        topterms, co_occur, Pg, nw = _get_param_matrices(vocabulary,
                                                         sentence_terms)

        #This dict will map each term to its weightage with respect to the
        #document
        result = {}

        N = sum(list(vocabulary.values()))
        #Iterates over all terms in vocabulary
        for term in co_occur:
            term = str(term)
            org_term = str(term)
            for x in Pg:
                #expected_cooccur is the expected cooccurence of term with this
                #term, based on nw value of this and Pg value of the other
                expected_cooccur = nw[term] * Pg[x]
                #Result measures the difference(in no of terms) of expected
                #cooccurence and  actual cooccurence
                result[org_term] = ((co_occur[term][topterms.index(x)] -
                                     expected_cooccur)**2/ float(expected_cooccur))

        terms = list(result.keys())
        terms.sort(key=lambda x: result[x],
                   reverse=True)

        return terms[:n]

get_top_n_terms 函数实现了这个功能， 我希望我写的 docstring 和 注释很好地解释了整个过程（结合起那篇论文）。

如果你有时间， 足够耐心， 你可以看到你Word2Vec模型里的整个词库（entire vocabulary）， 并找到你想加入到你的思维导图里的那些项。 这样做大概能得到最好的结果（就是太辛苦）。

第二步： 选定根节点 根结点是最能表达思维导图中心思想的。 相比起整个词库entire vocabulary， 选中的结点个数小上许多， 所以， 也许最好就是 手工选定根结点的项。

或者， 使用出现频率最高的（has the highest occurrence）。这一步也需要很多尝试（但数学科学能起什么作用吗）

第三步： 生成导图 这是至关重要的一步， 也是我花了最多时间的。

首先， 我需要定义一个项（term）的 情境向量（contextual vector）

假设， 本导图的根是‘电脑’， 连到另一个项‘硬件’， ‘硬件’再连‘键盘’， 那么， ‘键盘’的Word2Vec向量以 model[keyboard]的方式在Python/Gensim中获得。 定义这个向量为 $ v_{keyboard} $

现在考虑构建过程。

因为你目前已经有了一些东西， 你再想到'键盘' 时， 其实已经处于'电脑'和 '硬件' 的情境（上下文）中。

所以你很难把 ’键盘‘ 跟 ’音乐‘ 联系起来（最起码不直接相关）。

可见， '键盘' 的contextual vector情境向量（定义为 $ v^{'}_{keyboard} $ ) 一定会将方向偏向到

$ v 和 v_{hardware} $ (be biased in its direction towards). ---- 我们要计算 Word2Vec 模型的 cosine 相似度， 当然只跟方向有关。

从直觉上说， $ v_{hardware} 和 v^{'}_{keyboard} $ 的影响应该大于的影响应该大于 v ， 也就是距离越远， 父节点的影响会越小。

为了考虑这个因素， 我再加入了一个 参数 情境递减因子 αα 。 数学表达如下：

$$
v^{'}_{computer} = v 
$$
$$
v^{'}{hardware} = (1-\alpha)v + \alpha v^{'} 
$$
$$
v^{'} = (1-\alpha)v_{keyboard} + \alpha v^{'}_{hardware}
$$

最后， 可以生成实际的导图了， 以下是我使用的算法（我希望行内注释能帮你理解我的工作）


    from scipy.spatial.distance import cosine
    from networkx import Graph

    def build_mind_map(model, stemmer, root, nodes, alpha=0.2):
        """
        Returns the Mind-Map in the form of a NetworkX Graph instance.

        'model' should be an instance of gensim.models.Word2Vec
        'nodes' should be a list of terms, included in the vocabulary of
        'model'.
        'root' should be the node that is to be used as the root of the Mind
        Map graph.
        'stemmer' should be an instance of StemmingHelper.
        """

        #This will be the Mind-Map
        g = Graph()

        #Ensure that the every node is in the vocabulary of the Word2Vec
        #model, and that the root itself is included in the given nodes
        for node in nodes:
            if node not in model.vocab:
                raise ValueError(node + " not in model's vocabulary")
        if root not in nodes:
            raise ValueError("root not in nodes")

        ##Containers for algorithm run
        #Initially, all nodes are unvisited
        unvisited_nodes = set(nodes)
        #Initially, no nodes are visited
        visited_nodes = set([])
        #The following will map visited node to its contextual vector
        visited_node_vectors = {}
        #Thw following will map unvisited nodes to (closest_distance, parent)
        #parent will obviously be a visited node
        node_distances = {}

        #Initialization with respect to root
        current_node = root
        visited_node_vectors[root] = model[root]
        unvisited_nodes.remove(root)
        visited_nodes.add(root)

        #Build the Mind-Map in n-1 iterations
        for i in range(1, len(nodes)):
            #For every unvisited node 'x'
            for x in unvisited_nodes:
                #Compute contextual distance between current node and x
                dist_from_current = cosine(visited_node_vectors[current_node],
                                           model[x])
                #Get the least contextual distance to x found until now
                distance = node_distances.get(x, (100, ''))
                #If current node provides a shorter path to x, update x's
                #distance and parent information
                if distance[0] > dist_from_current:
                    node_distances[x] = (dist_from_current, current_node)

            #Choose next 'current' as that unvisited node, which has the
            #lowest contextual distance from any of the visited nodes
            next_node = min(unvisited_nodes,
                            key=lambda x: node_distances[x][0])

            ##Update all containers
            parent = node_distances[next_node][1]
            del node_distances[next_node]
            next_node_vect = ((1 - alpha)*model[next_node] +
                              alpha*visited_node_vectors[parent])
            visited_node_vectors[next_node] = next_node_vect
            unvisited_nodes.remove(next_node)
            visited_nodes.add(next_node)

            #Add the link between newly selected node and its parent(from the
            #visited nodes) to the NetworkX Graph instance
            g.add_edge(stemmer.original_form(parent).capitalize(),
                       stemmer.original_form(next_node).capitalize())

            #The new node becomes the current node for the next iteration
            current_node = next_node

        return g


备注： 我使用了 NetworkX 的简易图构建架构来完成了思维导图生成的核心任务（使之更易用于可视化）。

要计算 余弦距离， 我使用了 SciPy.

另外注意74和75行， 我使用了上篇博文所写的 StemmingHelper 类， 所以在思维导图中显示的是词干原始形式， 而不是词干。可以将StemmingHelper类直接当做参数 stemmer 传入。 所以， 如果你不需要词干处理， 那就把第4,74,75三行的代码干掉吧。

如果你仔细看过代码， 你会发现， 这看着很像 迪杰斯特拉的单点最短路径， 只是情境不同。

# 示例输出
[原文链接](https://codesachin.wordpress.com/2015/10/15/generating-rudimentary-mind-maps-from-word2vec-models/)

看着不错， 和我人工画的也挺像的。

# 其他
还有一些可尝试的东西。

* 比如加入 bi-grams 和 trigrams。 我相信能让 Word2Vec 模型更强大， 能对文本做出更好的释义。
* 导图中仍存在多余项， 但它给出了文本的（最？）短长度（相对其他文本挖掘任务来说）， 这种关键词提取算法（我在上文提到过的论文）似乎相当不错。 这段翻译有点不确认（There are some unnecessary terms in the Mind Maps, but given the short length of the texts (compared to most text mining tasks), the Keyword extraction algorithm in the paper I mentioned before, seems really good.）
* 此方法可用于头脑风暴， 从你选择的一点出发， 这代码框架会给出建议的可连项， 你再做出选择， 然后又可以得到新的推荐——就有点像思维导图助手。

无论怎样， 这都是篇长博文了， 谢谢你坚持着读完全文！（翻译也一样感谢您的阅读）。
