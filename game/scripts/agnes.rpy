label agnes:
    player '好吧，那层次聚类Agnes呢？'

    hitomi happy '这个你就非常熟悉了！数据结构学过吧？二叉树里的哈夫曼树学过吧？'
    hitomi normal '对于这么多个点，我先把它们相互之间的距离全部算出来，'
    hitomi '我每次都取两个最近的点，把他们变成一个簇。'
    hitomi '对于这个簇，我们仍然把它看成一个点，就像哈夫曼树的构造那样子。'
    hitomi '于是我们重复这个过程，直到簇的数量聚成一个。'
    hitomi '至于簇怎么看成一个点来计算距离，我这里给你三种方法：'
    hitomi '最小值：就是取两个类中距离最近的两个样本的距离作为这两个集合的距离；'
    hitomi '最大值：取两个集合中距离最远的两个点的距离作为两个集合的距离；'
    hitomi '平均值：把两个集合中的点两两的距离全部放在一起求一个平均值，相对也能得到合适一点的结果。'

    hitomi @happy '你看，这样我就介绍完了这些聚类方法了~赶紧干活吧！！'
    return
