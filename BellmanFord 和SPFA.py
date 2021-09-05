# 题目
'''
输入两个整数N,M(N表示有多少个顶点，M表示有多少条边)
输出两个顶点之间最短路径(有的题目规定的是第一个顶点到最后一个顶点，有的题目会给定两个顶点)
当N,M=0时程序结束
'''

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
如果一张图有 n 个节点，那么 Bellman-Ford 算法要做的就是对这张图上的所有的边做 n - 1 次松弛操作。
对于一个图G(v,e)(v代表点集，e代表边集)，执行|v|-1次边集的松弛操作，
所谓松弛操作，就是对于每个边e1(v,w)，将源点到w的距离更新为：
原来源点到w的距离 和 源点到v的距离加上v到w的距离 中较小的那个。
v-1轮松弛操作之后，判断是否有源点能到达的负环，
判断的方法就是，再执行一次边集的松弛操作，
如果这一轮松弛操作，有松弛成功的边，那么就说明图中有负环。算法复杂度为O(ne)
'''
def BellmanFord(cur, end, arr, num):
    cur = cur - 1
    INF = 100007  # 表示无穷大
    dist = []  # dist序列用来存储由cur顶点到各各顶点之间的距离
    for i in range(num):
        dist.append(INF)  # 将由cur顶点到各个顶点的距离初始化为无穷大
    dist[cur] = 0

    for i in range(num - 1):  # 对该图的所有边进行n-1次松弛操作
        # 用两层for遍历图中的所有边
        for j in range(num):
            for k in range(num):
                if arr[j][k] != INF:
                    dist[k] = min(dist[k], dist[j] + arr[j][k])  # 松弛
    return dist[end - 1]


'''
Bellman-Ford算法属于一种暴力的算法，即，每次将所有的边都松弛一遍，
这样肯定能保证顺序，但是仔细分析不难发现，源点s到达其他的点的最短路径中的第一条边，
必定是源点s与s的邻接点相连的边，因此，第一次松弛，我们只需要将这些边松弛一下即可。
第二条边必定是第一次松弛的时候的邻接点与这些邻接点的邻接点相连的边
因此我们可以这样进行优化：设置一个队列，初始的时候将源点s放入，然后s出队，
松弛s与其邻接点相连的边，将松弛成功的点放入队列中，然后再次取出队列中的点，
松弛该点与该点的邻接点相连的边，如果松弛成功，看这个邻接点是否在队列中，
没有则进入，有则不管，这里要说明一下，如果发现某点u的邻接点v已经在队列中，
那么将点v再次放到队列中是没有意义的。因为即时你不放入队列中，
点v的邻接点相连的边也会被松弛，只有松弛成功的边相连的邻接点，
且这个点没有在队列中，这时候稍后对其进行松弛才有意义。因为该点已经更新，需要重新松弛。
SPFA算法同样可以判断负环，如果某个点弹出队列的次数超过n-1次，则存在负环。对于存在负环的图，无法计算单源最短路径。
'''


def SPFA(cur, end, arr, num):
    cur = cur - 1
    INF = 100007
    dist = []  # dist序列表示由cur顶点到各各顶点之间的距离
    flag = []  # 判断是否在队列中的序列！！
    for i in range(num):
        dist.append(INF)  # 将由cur顶点到各个顶点的距离初始化为无穷大
        flag.append(0)
    queue = []
    dist[cur] = 0  # 源点到自身距离为0
    queue.append(cur)  # 源点入队
    flag[cur] = 1
    while queue:
        front = queue.pop(0)  # 取出队首元素弹出
        flag[front] = 0
        for i in range(num):  # 遍历
            if arr[front][i] != INF:
                if arr[front][i] + dist[front] < dist[i]:  # 如果不满足三角形不等式
                    dist[i] = arr[front][i] + dist[front]  # 更新答案
                    if flag[i] == 0:  # 如果终点不在队列
                        flag[i] = 1
                        queue.append(i)  # 入队
    return dist[end - 1]


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
    initList = Init(listRoad, n)
    a, b = input().split()
    a = int(a)
    b = int(b)
    ans = SPFA(a, b, initList, n)
    print(ans)
