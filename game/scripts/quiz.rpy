label quiz:
    hitomi happy '那我们就从简单的数据集着手来修复灵薄域吧！'
    hitomi '首先是花朵，这里我们从鸢尾花数据集入手，用三种聚类算法对其进行聚类！'
    show iris origin behind hitomi with dissolve
    hitomi normal '这是数据集降维到二维以后的样子。'
    hitomi '在这个数据集里面，每个样本包含了花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征。'
    hitomi '我们需要通过聚类来判断样本属于山鸢尾、变色鸢尾还是维吉尼亚鸢尾。'
    hitomi '下面我们先从KMeans算法开始吧'
    show iris origin with dissolve
    menu:
        '问题1：要设置k=？'
        '1':
            $ choice = 1
        '2':
            $ choice = 2
        '3':
            $ choice = 3
        '4':
            $ choice = 4
    show iris origin behind hitomi with dissolve
    if choice == 3:
        hitomi '恭喜你答对了！'
    else:
        hitomi '答错了哦，正确答案是3哦！'
    show iris kmeans zorder 10 with dissolve
    player '噢，三类是这样分的，不知道准确度如何？'
    show iris dbscan with dissolve
    hitomi '效果图，这张是DBSCAN的聚类效果图。'
    player '嗯，有三个点的归属发生了变化，但是其实它们分在…会更好，在这点上…'

    hide iris with dissolve
    hitomi happy '嗯，聚类完成了，花的模型我会算出来的，一会就告诉你'
    hitomi '接下来我们来对酒类进行聚类吧！'
    hitomi normal 'Wine葡萄酒数据集是对意大利同一地区种植的葡萄酒进行化学分析的结果。'
    hitomi '这些葡萄酒来自不同的品种。我们需要分析确定葡萄酒中每种葡萄酒中含有的13种成分的数量，然后对其余葡萄酒进行分析发现该葡萄酒的分类。以下是它们的属性'
    show wine origin behind hitomi with dissolve
    hitomi '这是他们的降维到二维以后的数据形态'
    hitomi angry '这次我们并不知道这些葡萄酒的数据来自哪些品种，也不知道它们原本会被分成几类，但这样的无标签聚类正是修复我们混乱的世界的主要方法！'
    player '那我要如何判断聚成几类是最合适的呢？'
    hitomi happy '一种通过具体数值进行比较的方式是：可以通过轮廓系数Silhouette等等来判断，Silhouette 遵循类紧致性。它的值用来描述一个目标对于目标所在簇与其他簇之间的相似性。其范围是从-1~+1，这个值越大表明目标与自己所在簇之间的匹配关系度越高，与其他簇的匹配关系度越低。如果这个值越高，那么聚类结果越好，如果是很小或是负值，那么可能是分簇太多或是太少造成的。另一种更加直观的方法就是观察。'
    hitomi normal '对于这个wine数据集，我们分别使用kmeans和DBSCAN算法分别来聚类，得出了它们的轮廓系数：'
    window hide
    show wine kmeans zorder 10 with dissolve
    pause
    show wine dbscan with dissolve
    pause
    menu:
        '那么，对于kmeans，分成几类是合适的？'
        '2':
            pass
        '3':
            pass
    player '嗯？分成3类和2类好像都可以？？甚至分2类的轮廓系数更高一点。'
    hitomi happy '是的，在面对纯数据时，聚类效果的标准其实是不唯一的，也许有时候分两类的轮廓系数最大，但是分三类才是需求的，所以聚类并没有一个统一的标准，只能通过一些特征来做到类内相似，类外不相似的守则。'
    player '喔~其实在面对纯数据聚类时，我也有那么一些造物主的味道（把白酒和伏特加聚一块？？）'
    hitomi angry '是的，那么最后，是一个抽象数据集，这是一个笑脸，要让这个笑脸的轮廓连续，我们应该使用哪种聚类方法呢？'
    menu:
        '选择什么算法好呢...'
        'KMeans':
            $ choice = 1
        'DBSCAN':
            $ choice = 2
        'Agnes':
            $ choice = 3
    hide wine with dissolve
    hitomi happy '好啦，模型都已经计算出来了！多亏了你，我们世界的花朵、酒类完成了聚类，变得清晰起来；'
    if choice == 1 or choice == 2:
        extend '大家的脸上又可以呈现出笑容了！'
    else:
        extend '不过大家的表情好像有点奇怪？？'
    return
