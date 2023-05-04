label quiz:
    hitomi happy '那我们就从简单的数据集着手来修复灵薄域吧！'
    hitomi '首先是花朵，这里我们从鸢尾花(iris)数据集入手，用三种聚类算法对其进行聚类！'
    show iris origin with dissolve
    hitomi normal '这是数据集降维到二维以后的样子。'
    hitomi '在这个数据集里面，每个样本包含了花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征。'
    hitomi '我们需要通过聚类来判断样本属于山鸢尾、变色鸢尾还是维吉尼亚鸢尾。'
    hitomi '下面我们先从KMeans算法开始吧'
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
    if choice == 3:
        hitomi '恭喜你答对了！'
    else:
        hitomi '答错了哦，正确答案是3哦！'
    return