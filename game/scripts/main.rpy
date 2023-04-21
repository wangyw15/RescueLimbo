label start:
    call prologue

    player '聚类听着就像把一堆数据分成几类，这里面有什么奥妙呢？'
    hitomi '没错，聚类是针对给定的样本，依据它们特征的相似度或距离，将其归并到若干个“类”或“簇”的数据分析问题，其结果满足，类内部相似，类之间不相似。注意它和分类有一定区别，聚类的对象仅仅是一堆数据，这些数据本身是不带标签的，所以聚类可以算作一种无监督学习。'
    hitomi '就好像我们现在所面临的情况，各种组成物体的数据开始混杂在一起，各种物体的界限不再分明，我们要做的就是将这些逐渐混乱的数据重新分成一个个簇，让物体不再混乱。'
    player '嗯~听你讲的好像也不难的呀，那我该怎么用聚类呢？总不能我把这些数据一个个用袋子封装好吧？'
    hitomi '这就要涉及到我们的算法了，为了实现聚类的目的，我们可以使用三种算法：模型聚类算法K-means、密度聚类算法DBSCAN和层次聚类算法Agnes，它们各有各的特点，虽然都能完成聚类的目的，但是聚类出的结果其实各自有所不同。当然，实现聚类可以用的算法远远不止这三个，只不过这三个算法已经可以满足我们的需求，并且也足够你这个大学生领悟了（笑）。'
    player '（怎么感觉在骂我？？？）好吧，那我速速学习一下吧，来！'

    # 主要剧情
    call kmeans
    call dbscan
    call agnes

    player '我说停停，我是差不多知道它们的工作原理了啦，但是它们在各种情况下孰优孰劣我还没实践过啊！至少，把它们的优缺点也和我一叙呗。'

    hitomi '呃呃，高级研究员在大学的时候这么差劲啊，好，你听着吧：对于Kmeans来说，如果有一个村民他住在山沟沟里，牧师也要为他一个人搬到山沟沟里，所以Kmeans算法不适合太离散的分类、样本类别不平衡的分类、非凸形状的分类。而DBSCAN因为可以不管离群的点，它的抗噪音性自然强了太多了，而且它可以聚出很有形状的类来，不像Kmeans，总是只给出一片片的聚类结果。不过DBSCAN也有限制的，如果样本集的密度不均匀、聚类间距差相差很大时，聚类质量较差，这时用DBSCAN聚类一般不适合。最后是层次聚类Agnes，它的优点很明显，前两种算法都需要给出很多参数，但我Agnes啥都不用给，也能聚地很有形状，又可以发现簇之间的层次关系，是很省事的方法。不过呢，你省事了，我就苦了，这从头到尾的，得算多少个距离啊，更别提这簇与簇之间的距离，算的我都发烧了！'

    player '你说得对，呃，我还是想要一些例子，要不你给我几张图，我来看看用三种聚类算法分别聚类以后它们的实际效果？'

    hitomi '好吧，你操作就是了，快点领悟吧！'

    return