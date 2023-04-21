﻿label prologue:
    show bg black

    player '啊啊，头好疼...'
    '感觉自己好像躺在地上'
    extend '\n为了确认周围的情况，我缓缓地睁开了双眼'
    hide bg black
    scene bg prologue1 with dissolve
    '却发现自己来到了一片奇诡的“荒野”，正躺在废墟之中'
    '地面四分五裂，楼宇、家具、各类杂物都混合在一起，难舍难分'
    '???' '[player_name]，欢迎来到由往生实践设施创建的实验世界-8号，我是这个世界的AI-[hitomi.name]'
    '一个缥缈却明丽的声音传来'
    show hitomi_catear normal at right, chr_display with dissolve
    '循声而去，是一个猫耳少女在向我说话'
    '嗯，是我喜欢的类型'
    '但是现在不是想这种事的时候啊！'
    '她刚刚在说什么？还是问问当下什么情况更好'
    player '什么AI？什么设施？我记得我刚才还在教室里啊，还在跟ChatGPT畅聊呢'
    player '难道...我转生来到了赛博空间？你就是刚刚的ChatGPT？'
    # love live superstar
    extend '你的声音太好听了吧，你说话真的好好听啊，简直就是天籁！是预先录制的还是用VITS生成的？'
    hitomi @angry '什么ChatGPT，那不是最初代的对话型AI吗？我可是{b}高性能{/b}的AI，你在说什么啊？'
    hitomi '（居然还记得这么古早的技术吗...）'
    hitomi @surprised '等一下...我知道了'
    hitomi @embarrassed '看来这次传输还是有点瑕疵'
    hitomi '这个传输技术还在研发中，本来不应该投入正式使用的'
    hitomi '现在是紧急情况，为了拯救这个崩坏的世界，只能启用这技术把你送过来'
    hitomi @sad '但是这项技术并不成熟，在传输过程中，尽管你的意识得以传入，记忆却丢失了太多'
    hitomi -surprised '事到如今也没办法了'
    hitomi angry '接下来的话请你认真听好：'
    # 流浪地球2
    hitomi '你在毕业之后加入了一个研究设施，成为了设施的高级研究员。设施的目的是研究并制造一个虚拟的数字世界，让即将逝去的人成为数字生命，在其中永远活下去。'
    hitomi '然而我们8号试验场因为不明原因发生了数据大崩坏，所有数据混杂在一起无法分类，而自动修复的程序，包括我的计算系统也损坏了，现在是通过备用系统运作的'
    hitomi '又因为实验世界自主条例，只能从里世界修复里世界'
    hitomi '因此你的任务恰如盘古，需要用聚类的知识把天地万物分开，让世界从混沌的状态回归常态！'
    hitomi normal '我知道这听起来有点强人所难，但是这就是现在的情况，你就是拯救这个世界的最后希望了'
    player '唔，可是我的记忆还停留在大学二年级，并不懂什么聚类啊！'
    hitomi @happy '没关系，我会将几种聚类算法的概念给你阅读，但这是我唯一能做的事情了。学习聚类算法，然后则其适者加以应用来拯救这个世界吧！'
    # hitomi '我会在你的左侧给你一些提示，你可以通过点击提示来查看相关的知识，但是我只能给你一次机会，如果你不会的话，我就只能把你传回去了。'
    # hitomi '你可以通过点击左侧的“返回”按钮来返回到上一步，但是这样会导致你的进度丢失，所以请慎重选择。'
    # player '好的，我明白了。'
    # hitomi '那么，祝你好运！'
    # 'hitomi的声音渐渐消失，只剩下一片寂静。'
    # '我不知道这个世界是怎么回事，但是我知道我必须要拯救它。'
    # extend '我必须要拯救它。'
    return
