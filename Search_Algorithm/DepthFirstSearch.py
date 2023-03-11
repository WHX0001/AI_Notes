sample = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

def dfs(grap, start):  # 传入两个参数，第一个grap，第二个是开始的节点
    frontier = [start]  # 此处用列表来表示每次传入的节点，方便删除与增加元素
    flag = set(start)  # 查看已经访问的节点
    while len(frontier) > 0:  # 当队列的长度大于零
        expect = frontier.pop(-1)  # 将最后一个节点拿出来 LIFO
        around = grap[expect]  # 得到上一个节点的邻接点
        for newFrontierElement in around:  # 遍历对应的节点
            if newFrontierElement not in flag:  # 判断邻接点不在队列中
                frontier.append(newFrontierElement)  # 将未见过的点传入
                flag.add(newFrontierElement)  # i已经见过
        print(expect)


dfs(sample, 'A')
