label dbscan:
    player '那密度聚类DBSCAN算法呢？'
    show dbscan draw1 with dissolve
    hitomi normal '顾名思义，这是根据密度进行聚类的算法，还是以二维样本举例：'
    hitomi '坐标系中有很多的点，每个点以自己为圆心，r为半径作圆，这个点和在圆里的点就形成一个“朋友圈”。'
    hitomi '如图所示，每个点都画上了一个“朋友圈”。'
    hitomi '统计一下在这个圆内的点的数量，计它为“好朋友数”。'
    hitomi '由你给出一个数n，如果一个点的好朋友数大于等于n，就说这个点是一个“交际花”（核心点）。'
    hitomi '在这个例子里，我们规定n是4，那么红点就是“交际花”。'
    hitomi '我们知道，交际花总是会相互吸引的，那么一个交际花的好朋友里有另一个交际花也是很正常的。'
    hitomi '因此我们规定，如果一个交际花A的朋友圈里有另一个交际花B，那我就让他们的朋友圈合并，形成一个更大的朋友圈（簇）。'
    hitomi '但是黄点虽然没有那么多好朋友，不是交际花，但也被包括在交际花的“朋友圈”里，那么他也是更大的朋友圈中的一员（簇的一部分）。'
    hitomi happy '依此规则，这个朋友圈不断扩大，最后直到所有能被包含的交际花都被包含进去了，这个簇就算完事了。'
    hitomi angry '最后我们可以得到一个由密度主导的聚类结果。这个算法中，如果一些点的朋友圈太小，就会被淘汰出去，可见它和Kmeans有大不同的。'
    hitomi '结果就是图中形成了一个簇，由所有红点和黄点组成；而图里的蓝点就被淘汰出去了。'
    player '不合群就会被淘汰？？太吓人了！！那我设置参数的时候，可要把n调的小一点了！'
    hitomi normal '确实是可以这样做的。但是既然我们要聚类，就需要放弃一些离群太远的点，它们对结果造成的误差可是很大的！我们也因此称它们为噪声，蓝点就是“噪声”的一员。'
    hide dbscan
    return
