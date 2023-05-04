label start:
    # 自动全屏
    $ fullscreen()
    # 输入玩家名
    $ player_name = renpy.input('请输入你的玩家名：')

    # 序章
    show overlay dark
    show text '{color=#FFFFFF}{size=+50}序章{/size}{/color}'
    with dissolve
    pause 1.0
    hide text
    hide overlay
    with dissolve
    call prologue

    # 正文
    show overlay dark
    show text '{color=#FFFFFF}{size=+50}向聚类进发{/size}{/color}'
    window hide
    with dissolve
    pause 1.0
    hide text
    hide overlay
    window show
    with dissolve

    # 间章1
    player '聚类听着就像把一堆数据分成几类，这里面有什么奥妙呢？'
    hitomi happy '没错，聚类是针对给定的样本，依据它们特征的相似度或距离，将其归并到若干个“类”或“簇”的数据分析问题。'
    hitomi '其结果满足类内部相似，但类之间不相似。'
    hitomi angry '注意它和分类有一定区别，聚类的对象仅仅是一堆数据，这些数据本身是不带标签的，所以聚类可以算作一种无监督学习。'
    hitomi '就好像我们现在所面临的情况，各种组成物体的数据开始混杂在一起，各种物体的界限不再分明。'
    hitomi '我们要做的就是将这些逐渐混乱的数据重新分成一个个簇，让物体不再混乱。'
    player '嗯~听你讲的好像也不难的呀，那我该怎么用聚类呢？'
    player '总不能我把这些数据一个个用袋子装到一起吧？'
    hitomi happy '这就要涉及到我们的算法了，为了实现聚类的目的，我们可以使用三种算法：'
    hitomi '模型聚类算法K-means；'
    extend '\n密度聚类算法DBSCAN；'
    extend '\n层次聚类算法Agnes。'
    hitomi normal '它们各有各的特点，虽然都能完成聚类的目的，但是聚类出的结果其实各自有所不同。'
    hitomi happy '当然，实现聚类可以用的算法远远不止这三个，只不过这三个算法已经可以满足我们的需求，并且也足够现在的你领悟了。'
    player '好，那我速速学习一下吧，来吧！'

    # 三个聚类
    show bg classroom
    show overlay dark
    show text '{color=#FFFFFF}{size=+50}K-Means{/size}{/color}'
    window hide
    with dissolve
    pause 1.0
    hide text
    hide overlay
    window show
    with dissolve
    call kmeans

    show overlay dark
    show text '{color=#FFFFFF}{size=+50}DBSCAN{/size}{/color}'
    window hide
    with dissolve
    pause 1.0
    hide text
    hide overlay
    window show
    with dissolve
    call dbscan

    show overlay dark
    show text '{color=#FFFFFF}{size=+50}层次聚类{/size}{/color}'
    window hide
    with dissolve
    pause 1.0
    hide text
    hide overlay
    window show
    with dissolve
    call agnes

    show bg prologue1 with dissolve
    show hitomi happy at right, chr_display with dissolve
    hitomi @happy '呼~终于讲完这些聚类啦~赶紧开始吧！！'
    player '停停停，我是差不多知道它们的工作原理了啦，'
    player '但是它们在各种情况下孰优孰劣我还没实践过啊！至少，把它们的优缺点也和我一叙呗。'
    hitomi sneer '呵呵，高级研究员在大学的时候原来这么{cps=*0.1}{b}差劲{/b}啊{/cps}。'
    hitomi  '好，你听着吧：'
    hitomi angry '对于Kmeans来说，如果有一个村民他住在山沟沟里，牧师也要为他一个人搬到山沟沟里。'
    hitomi happy '所以Kmeans算法不适合太离散的分类、样本类别不平衡的分类、非凸形状的分类。'
    hitomi '而DBSCAN因为可以不管离群的点，它的抗噪音性自然强了很多。'
    hitomi '而且它可以聚出很有形状的类来，不像Kmeans，总是只给出一片片的聚类结果。'
    hitomi @angry '不过DBSCAN也有限制的，如果样本集的密度不均匀、聚类间距差相差很大时，聚类质量较差，这时用DBSCAN聚类一般不适合。'
    hitomi normal '最后是层次聚类Agnes，它的优点很明显：'
    hitomi '前两种算法都需要给出很多参数，但我Agnes啥都不用给，也能聚得很有形状，又可以发现簇之间的层次关系，是很省事的方法。'
    hitomi @shy '不过呢，你省事了，我就苦了，这从头到尾的，得算多少个距离啊，更别提这簇与簇之间的距离，算的我都烧了！'
    player '{cps=*0.1}嗯...我{/cps}还是想要一些例子，要不你给我一点数据，我来看看用三种聚类算法分别聚类以后它们的实际效果？'
    hitomi happy '这么积极啊，很好！那就来试试看吧'

    show overlay dark
    show text '{color=#FFFFFF}{size=+50}实战{/size}{/color}'
    window hide
    with dissolve
    pause 1.0
    hide text
    hide overlay
    window show
    with dissolve
    call quiz

    player '啊，初学聚类，感觉还有很多事情要学！'
    hitomi angry '没错，刚才的聚类只是很简单的例子。'
    hitomi '为了修复我们的世界，必然要用到更多聚类方法和评判标准。'
    hitomi happy '不过，对于一个大二学生来说，这些知识足够你消化一阵子了。'
    hitomi '所幸这个世界里的时间比外面流速更慢。以后的知识，就等以后在再来探索吧！'

    show overlay dark
    show text '{color=#FFFFFF}{size=+50}我的旅程才刚刚开始...{/size}{/color}'
    window hide
    with dissolve
    pause
    return
