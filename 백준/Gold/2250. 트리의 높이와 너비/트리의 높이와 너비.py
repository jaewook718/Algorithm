def inorder(i,level):
    global l
    if l < level:
        l = level
    if i!=-1:
        L = graph[i][0]
        R = graph[i][1]
        M = i
        inorder(L,level+1)
        ans.append((level,M))
        inorder(R,level+1)


N = int(input())
graph = [[] for _ in range(N+1)]
isRoot = [0]*(N+1)
for _ in range(N):
    parent, left, right = map(int, input().split())
    graph[parent].append(left)
    graph[parent].append(right)
    isRoot[parent] += 1
    if left != -1:
        isRoot[left] += 1
    if right != -1:
        isRoot[right] += 1
for i in range(1, N + 1):  # 루트를 제외한 모든 점들은 2의 값을 가지기 때문에
    if isRoot[i] == 1:
        root = i

ans = []
l = 0
inorder(root,1)
_max = 0
idx = 0
for i in range(1,l):
    L = 0
    R = N-1
    while ans[L][0] != i: L += 1
    while ans[R][0] != i: R -= 1
    if _max < R-L+1:
        _max = R-L+1
        idx = i
print(idx, _max)

