# 初始化邻接矩阵
'''
默认将num*num的矩阵中的元素定义成INF(无穷大)，为了方便后续的使用min函数求最短路径
然后分别将由x至y路径的权值加入矩阵的matrix[x][y]中，如果是无向图则同时令matrix[x][y]=matrix[y][x]
'''


def Init(arr, num):
    matrix = [[100007 for col in range(num)] for row in range(num)]
    for t in arr:
        # 对于无向图的操作
        matrix[t[0] - 1][t[1] - 1] = matrix[t[1] - 1][t[0] - 1] = t[2]
        # 如果是有向图则：matrix[t[0] - 1][t[1] - 1] = t[2]
    return matrix


'''
传入一个节点，当然，传入的这个节点是随意的。将这个点到其他点的距离存入dis数组，并将传入的这个点标记为已访问。
然后找出从start（传入的那个点）出发的路径中的最短的一个路径；并将它到达的那个点记性并标记。
然后更新dis数组（重点）：如果该结点没有被访问过，且点距离当前点的距离更近，就执行更新；
最后dis数组中就是最小生成树的最短路径的集合；对其求和，即是最小生成树的最短路径；

'''


def prime(start, arr, num):
    INF = 100007
    start -= 1
    dis = []  # 储存由其他点到该点距离的最小值
    vis = [0 for col in range(num)]
    for i in range(num):  # 将与start点相连的路径存到dis数组中
        dis.append(arr[start][i])
    vis[start] = 1

    while True:
        flag = -1
        min = INF
        for i in range(num):  # 在此时从start发出的路径中找到一个最短的路径；即：在当前的生成树中找一条最短路径
            if vis[i] != 1 and dis[i] < min:
                min = dis[i]
                flag = i  # 此时，start到i的路径最短，并将i记下，后面标记为已访问
        if flag == -1:  # 所有结点都已访问；即：已生成最小生成树；跳出死循环
            break
        vis[flag] = 1
        for i in range(num):  # 更新dis数组
            if vis[i] != 1 and dis[i] > arr[flag][i]:  # 该结点没有被访问过，且flag点到该点的距离比另一个点到该点的距离更近，就执行更新
                dis[i] = arr[flag][i]

    sumDis = 0
    for i in range(num):  # n个点一共n-1条路
        if i != start:
            sumDis = sumDis + dis[i]
    return sumDis


#  kruskal算法基本思想：在初始状态时隐去图中的所有边，这样图中每个顶点都自成一个连通块。之后执行下面的步骤：
# （1）对所有的边按边权从小到大进行排序；
# （2）按边权从小到大测试所有边，如果当前测试边所连接的两个顶点不在同一个连通块中，则把这条测试边加入当前最小生成树中；否则，将边舍弃；
# （3）执行步骤（2），知道最小生成树中的边数等于总顶点数减1或者测试完所有的边时结束。
#     当结束时，如果最小生成树的边数小于总顶点数减1，则说明该图不连通

# 注意：这个伪代码里需要注意两个细节：
# （1）如何判断测试边的两个端点是否在不同的连通块中；
# （2）如何将测试边加入到最小生成树中；
#  其实我们可以把每个连通块当做一个集合，判断两个端点是否在同一个连通块中就可以转换为判断两个端点是否在同一个集合中，
#  解决这个问题的方法是使用并查集。并查集可以通过查询两个结点所在集合的根结点是否相同来判断它们是否在同一个集合中，
#  而合并功能恰好可以解决上面提到的第二个问题，即只要把测试边的两个端点所在集合合并，就能达到将边加入最小生成树的目的。

def findFather(father, x): # 使用并查集寻找根节点
    if x == father[x]:
        return x
    else:
        return findFather(father, father[x])


def kruskal(arr, num, edge):
    ans = 0
    numEdge = 0
    father = []
    for i in range(num):  # 将每一个点设置成一个集合，即该顶点的根是自己
        father.append(i)
    arr.sort(key=lambda x: x[2])  # 按照边的权重进行排序
    for i in range(edge):
        fau = findFather(father, arr[i][0])  # 找到一个顶点的根
        fav = findFather(father, arr[i][1])  # 找到另一个顶点的根
        if fav != fau:  # 如果两个顶点的根不同，即表示这两个顶点相连不是同一个集合内，不会构成圈，可以相连
            father[fau] = fav   # 将其中一个顶点的并查集的集合设置成另外一个
            ans = ans + arr[i][2]
            numEdge += 1
            if numEdge == num - 1:  # 判断是否已经连接了所有顶点
                break
    if numEdge != num - 1:  # 如果遍历完所有边后，仍然没有得到n-1个顶点，则无法构造生成树
        return "Error"
    else:
        return ans


while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break
    listRoad = []
    for i in range(m):
        strInt = []
        str = input().split()
        for j in str:
            strInt.append(int(j))
        listRoad.append(strInt)
    ansKruskal = kruskal(listRoad, n, m)
    initList = Init(listRoad, n)
    ansPrime = prime(1, initList, n)
    print(ansKruskal)
    print(ansPrime)
'''
6 10
0 1 4
1 2 1
2 3 6
3 4 5
0 4 1
0 5 2
1 5 3
2 5 5
3 5 4
4 5 3
'''
