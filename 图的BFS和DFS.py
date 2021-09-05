# 初始化邻接矩阵
"""
默认将num*num的矩阵中的元素定义成0(表示不存在这条路径)，因为不需要使用min函数进行比较
"""
def Init(n, m):
    listRoad = []
    for i in range(m):
        strInt = []
        str = input().split()
        for j in str:
            strInt.append(int(j))
        listRoad.append(strInt)
    matrix = [[0 for col in range(n)] for row in range(n)]
    for t in listRoad:
        # 对于无向图的操作
        # matrix[t[0] - 1][t[1] - 1] = matrix[t[1] - 1][t[0] - 1] = 1
        # 如果是有向图则：
        matrix[t[0] - 1][t[1] - 1] = 1
    return matrix


'''
深度优先搜索在搜索过程中访问某个顶点后，需要递归地访问此顶点的所有未访问过的相邻顶点。
初始条件下所有节点为白色，选择一个作为起始顶点，按照如下步骤遍历：
a. 选择起始顶点涂成灰色，表示还未访问
b. 从该顶点的邻接顶点中选择一个，继续这个过程（即再寻找邻接结点的邻接结点），一直深入下去，直到一个顶点没有邻接结点了，涂黑它，表示访问过了
c. 回溯到这个涂黑顶点的上一层顶点，再找这个上一层顶点的其余邻接结点，继续如上操作，如果所有邻接结点往下都访问过了，就把自己涂黑，再回溯到更上一层。
d. 上一层继续做如上操作，知道所有顶点都访问过。
'''
def DFS(arr, s, visited):
    visited[s] = 1
    print(s + 1)
    for i in range(len(arr)):
        if arr[s][i] == 1 and visited[i] == 0:
            DFS(arr, i, visited)


'''
广度优先搜索在进一步遍历图中顶点之前，先访问当前顶点的所有邻接结点。
a .首先选择一个顶点作为起始结点，并将其染成灰色，其余结点为白色。
b. 将起始结点放入队列中。
c. 从队列首部选出一个顶点，并找出所有与之邻接的结点，将找到的邻接结点放入队列尾部，将已访问过结点涂成黑色，没访问过的结点是白色。
   如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现
d. 按照同样的方法处理队列中的下一个结点。
'''
def BFS(arr, start, vis):
    queue = []
    queue.append(start)
    vis[start] = 1
    while queue:
        front = queue.pop(0)
        print(front + 1)
        for i in range(len(arr)):
            if vis[i] == 0 and arr[front][i] == 1:
                vis[i] = 1
                queue.append(i)


while True:
    print("Input:BFS")
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break
    BFSList = Init(n, m)
    visBFS = [0 for col in range(n)]
    for i in range(n):
        if visBFS[i] == 1:
            continue
        BFS(BFSList, i, visBFS)

    print("Input:DFS")
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    DFSList = Init(a, b)
    visDFS = [0 for col in range(a)]
    for i in range(a):
        if visDFS[i] == 1:
            continue
        DFS(DFSList, i, visDFS)

'''
BFS
5 10
1 2
1 3
2 3
2 4
3 2
3 3
3 4
4 1
5 3
5 4

DFS
5 9
1 2
1 3
2 3
2 5
3 3
4 1
4 2
4 5
5 3
'''
