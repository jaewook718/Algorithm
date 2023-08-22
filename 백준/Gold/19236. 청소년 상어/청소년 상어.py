dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
from copy import deepcopy
def dfs(shark_x, shark_y, shark_d, cur_score, graph):
    global max_ans
    if shark_d == 0:
        shark_x, shark_y, shark_d, score = eat(-1, -1, 0, 0, graph)
        for i in range(1, 17):
            move(graph, i)

        dfs(shark_x, shark_y, shark_d, score, graph)
    else:
        cnt = 1
        while True:
            nx = dx[shark_d]*cnt + shark_x
            ny = dy[shark_d]*cnt + shark_y
            if 0<= nx < 4 and 0<=ny<4 and graph[nx][ny][0] != 0:
                copy_graph = deepcopy(graph)
                x, y, d, score = eat(shark_x, shark_y, nx, ny, copy_graph)
                for i in range(1, 17):
                    move(copy_graph, i)
                dfs(x, y, d, cur_score+score, copy_graph)
            elif 0<=nx<4 and 0<=ny<4 and graph[nx][ny][0] == 0:
                pass
            else:
                max_ans = max(max_ans, cur_score)
                return
            cnt += 1

def eat(x, y, nx, ny, graph):
    score = graph[nx][ny][0]
    d = graph[nx][ny][1]
    graph[nx][ny] = [-1, -1]
    if x!=-1 and y!=-1:
        graph[x][y] = [0, 0]

    return nx, ny, d, score


def move(graph, k):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == k:
                d = graph[i][j][1]
                while True:
                    nx, ny = i + dx[d], j + dy[d]
                    if 0<=nx<4 and 0<=ny<4 and graph[nx][ny][0] != -1:
                        graph[i][j][1] = d
                        graph[i][j], graph[nx][ny] = graph[nx][ny], graph[i][j]
                        return
                    else:
                        d = d+1
                        if d == 9:
                            d = 1

max_ans = 0
arr = []
for _ in range(4):
    a, b, c, d, e, f, g, h = map(int, input().split())
    arr.append([[a, b], [c, d], [e, f], [g ,h]])
dfs(-1, -1, 0, 0, arr)
print(max_ans)