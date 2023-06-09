label kmeans:
    hitomi normal '那么先来看Kmeans算法，这个算法是最常被使用的算法，它认为两个目标的距离越近，相似度越大。'
    hitomi 'Kmeans聚类的目标是将n个样本点划分到k个集合中，使得组内平方和最小。'
    hitomi '换句话说，就是要找到满足这个数学公式的聚类，其中μ是所有点的均值：'
    window hide
    show kmeans math at center
    with dissolve
    pause
    window show
    with dissolve
    player '不行，我得了看到数学公式就头晕的病。'
    player '你能不能用通俗的例子来解释一下这个公式？'
    hitomi @angry '{cps=*0.07}...行{/cps}吧。'
    show kmeans draw1 with dissolve
    hitomi '把每个样本点比作一个村庄的村民，而你是天主教堂的教皇，要选派几个牧师去传授福音，必须把每个村民覆盖在内。'
    show kmeans draw2 with dissolve
    hitomi '但是牧师们并不知道这个村庄的村民分布情况，'
    show kmeans draw3 with dissolve
    '于是他们各自随意选择了地点驻扎下来，并告诉村民。'
    show kmeans draw4 with dissolve
    hitomi '聪明的村民当然会选择最近的牧师去登记，于是每个牧师手里都有了一份名单（簇）。'
    show kmeans draw5 with dissolve
    hitomi '他一想：为了天父，我要让我的信众们享受更近的距离，于是他搬到了名单上所有地址的中心地带。'
    hitomi '所有牧师这样做以后，有的村民发现：离自己最近的牧师换了，于是名单再次更新了。'
    show kmeans draw6 with dissolve
    hitomi happy '牧师为了信众考虑又搬了家，循环往复不知多少次，终于牧师发现自己可以不用搬家了，于是他们把名单交给了你，对这个村庄的传教也就此完成了。'
    show kmeans draw7 with dissolve
    hitomi 'Kmeans的过程也就结束了。'
    player '噢噢噢噢！amen！这样就可以把距离近的数据聚成一类了！！看来我只要设置牧师数量（簇的数量）和迭代次数就可以完成聚类了！'
    hitomi @angry '顺带一提，实际上这就是Lloyd算法，通过不断迭代得到某一局部最优解。'
    hide kmeans
    return
