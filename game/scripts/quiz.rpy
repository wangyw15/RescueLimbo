label quiz:
    hitomi happy '那我们就从一些基本的东西来着手来修复灵薄域吧！'
    hitomi normal '首先是花朵，这里我们从鸢尾花入手。'
    hitomi @happy '因为当我看着花的时候心里就很平静，花香也是沁人心脾，沉醉在这一片花海中。'
    hitomi @shy '而且鸢尾花的话语是{b}绝望的爱{/b}，在这种情境之下很适合嘛~'
    hitomi '咳咳，回到正题来。'
    hitomi @angry '为了让鸢尾花回归这个世界，就要用三种聚类算法对其进行聚类，如盘古开天地一般将混杂在一起的数据分离开来！'
    show iris origin behind hitomi with dissolve
    hitomi '这是鸢尾花的数据集降维到二维以后的样子。'
    hitomi '在这个数据集中，每个样本都包含了花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征。'
    hitomi '我们需要通过聚类把这些混沌的数据分为两类，先从KMeans算法开始。'
    show iris zorder 10
    menu:
        '嗯~KMeans中的k要定为多少呢~'
        '1':
            $ choice = 1
        '2':
            $ choice = 2
        '3':
            $ choice = 3
        '4':
            $ choice = 4
    show iris zorder 0 behind hitomi with dissolve
    if choice == 2:
        hitomi @happy '两种就足够啦！'
    elif choice == 1:
        hitomi @sad '一种还是有点少了...'
    else:
        hitomi '分得太多了，其实两类就可以了。'
    show iris kmeans zorder 10 with dissolve
    player '噢，KMeans的两类是这样分的，不知道准确度如何？'
    show iris dbscan with dissolve
    hitomi '这张是DBSCAN的聚类效果图。'
    show iris zorder 0 behind hitomi with dissolve
    player '嗯，有三个点的归属发生了变化，但是其实它们分在…会更好，在这点上…'
    hide iris with dissolve
    hitomi happy '嗯，鸢尾花的聚类完成了，花的模型我会算出来的，一会就告诉你~'
    hitomi '这下我就有机会欣赏曾经的花海了。'

    hitomi '接下来我们来对酒类进行聚类吧！'
    hitomi '小酌怡情嘛，偶尔喝一点放松一下。但是喝多了就不好了。'
    hitomi normal '这里还有葡萄酒数据集，是对某地区种植的葡萄酒进行化学分析的结果，但是现在都混在一起分不开了。'
    hitomi '这些葡萄酒来自不同的酒庄。我们需要分析确定每种葡萄酒中含有的13种成分的数量，并进行分析来确定该葡萄酒的分类。属性就如图上这般：'
    show wine origin behind hitomi with dissolve
    hitomi '这是他们的降维到二维以后的数据形态。'
    hitomi @sad '可惜葡萄酒的数据丢失得更彻底，我们并不知道这些葡萄酒来自什么酒庄，也不知道它们原本是几种葡萄酒。'
    hitomi @angry '但是，这样的无标签聚类正是修复我们混乱世界的主要方法！'
    player '那我要如何判断聚成几类是最合适的呢？'
    hitomi '一共有两种方法，一种是直观的方法，你刚刚可能已经用过了，就是观察；'
    hitomi '另一种方法就是通过具体数值进行比较，比如 Silhouette 等方法。'
    hitomi 'Silhouette 遵循类紧致性，它的值用来描述一个目标对于目标所在簇与其他簇之间的相似性。'
    hitomi '其范围是\[-1,+1\]。这个值越大表明目标与自己所在簇之间的匹配关系度越高，与其他簇的匹配关系度越低。'
    hitomi '如果这个值越高，那么聚类结果越好；如果是很小或是负值，那么可能是分簇太多或是太少造成的。'
    hitomi '对于现在这个葡萄酒的数据集来说，我们先用KMeans算法对这些葡萄酒进行聚类：'
    show wine kmeans zorder 10 with dissolve
    hitomi '用KMeans时， Silhouette 系数是0.493；'
    menu:
        '对于KMeans来说，分成几类是合适的？'
        '2':
            pass
        '3':
            pass
    player '嗯？分成两类或者三类好像都可以？？甚至分两类的轮廓系数更高一点。'
    show wine zorder 0 behind hitomi with dissolve
    hitomi happy '是的，在面对纯数据时，聚类效果的标准其实是不唯一的。'
    hitomi '也许有时候分两类的轮廓系数最大，但是分三类才是符合需求的。'
    hitomi @angry '所以聚类并没有一个统一的标准，只能通过一些特征来做到类内相似，类外不相似的守则。'
    hitomi '然后来看看DBSCAN聚类之后的结果：'
    window hide
    show wine dbscan zorder 10 with dissolve
    pause
    player '喔~其实在面对纯数据聚类时，我也有那么一些造物主的味道（把白酒和伏特加聚一块？？）'
    hide wine with dissolve
    hitomi '是的，其实把你找过来，就是需要一个人来承担这个造物主的责任。'
    hitomi normal '那么最后，是一个特殊的数据集。'
    show pic origin at center, pic_display with dissolve
    hitomi '这是一个笑脸，要让这个笑脸的轮廓连续，我们应该使用哪种聚类方法呢？'
    menu:
        '选择什么算法好呢...'
        'KMeans':
            $ choice = 1
        'DBSCAN':
            $ choice = 2
        'Agnes':
            $ choice = 3
    if choice == 1 or choice == 2:
        show pic bin with dissolve
        hitomi @happy '大家的脸上又可以呈现出笑容了！'
    else:
        show pic rgb with dissolve
        hitomi @sad '不过大家的表情好像有点奇怪？？'
    hide pic with dissolve
    hitomi happy '好啦，模型都已经计算出来了！多亏了你，我们世界的花朵、酒类完成了聚类。这个世界已经在渐渐恢复了！'
    return
