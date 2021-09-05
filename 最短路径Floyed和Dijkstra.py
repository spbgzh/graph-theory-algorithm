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


# Floyed算法(多源最短路,基于动态规划算法)
# 本质是对边进行操作
'''
状态转移方程: arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
为了得到状态转移方程，定义f[k][i][j]为经过前k的节点,从i到j所能得到的最短路径，
f[k][i][j]可以从f[k-1][i][j]转移过来，即不经过第k个节点，也可以从f[k-1][i][k]+f[k-1][k][j]转移过来，即经过第k个节点。
'''
def Floyd(cur, end, arr, num):
    for k in range(num):
        for i in range(num):
            for j in range(num):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    print(arr)
    return arr[cur-1][end-1]


# Dijkstra算法(单源最短路,基于贪心算法)
# 本质是对顶点进行操作
'''
维护一个列表dist用来储存初始顶到到各个顶点之间的最短距离，对该列表一直进行一下操作：
1.找出未访问的点中dist最小的点，将他作为候选点
2.对所有未访问的点的dist进行更新，dist[未访问] = min(dist[未访问],dist[候选点] + map[候选点][未访问])
最后可以得到一个dist里面包含初始顶点到各个顶点之间的最短路径
'''
def Dijkstra(cur, end, arr, num):
    cur = cur - 1  # 序列从0开始
    vis = [0 for col in range(num)]  # vis中0表示没有访问到1表示已经访问
    vis[cur] = 1

    dist = []  # dist序列表示由cur顶点到各各顶点之间的距离
    for i in range(num):
        dist.append(arr[cur][i])  # 将由cur顶点到各个顶点的距离赋初值给dist
    dist[cur] = 0
    # 开始求最短路
    for i in range(1, num):  # 遍历除初始顶点以外的每个顶点
        k = cur  # 定义k为初始顶点
        minval = 100007  # 设置一个变量用来临时储存最小的路径长度
        for j in range(num):  # 找到未访问点中，dist最小的点
            if vis[j] == 0 and dist[j] < minval:
                minval = dist[j]
                k = j  # 如果当前的j可以使当前路径长度最小则k=j
        vis[k] = 1  # 已找到dist最小的点k，设置顶点k已被访问

        # 找到的该点将被候选成为我们最终最短路中的点，接下来我们将进行判断是否使它加入
        # 接下来通过点k对未访问的点进行松弛操作
        # 即选择当前由cur点到j点的距离与由cur点到k点的距离加上k到j的距离的最小值
        for j in range(num):
            if vis[j] == 0:
                dist[j] = min(dist[j], dist[k] + arr[k][j])

        # 其方程与Floyd类似但是本质却不同，
        # Floyd的动态规划思想是：想要解决大问题，先解决局部问题
        # 而Dijkstra的贪心的思想是：每一步操作满足当前最优解
    return dist[end-1]


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
    # ans= Floyd(1, n, initList, n)
    ans = Dijkstra(1, n, initList, n)

    print(ans)
