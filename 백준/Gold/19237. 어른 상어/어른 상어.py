dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

def check():
    for i in range(N):
        for j in range(N):
            if valid[i][j]:
                if valid[i][j][1] == 1:
                    valid[i][j] = 0
                else:
                    valid[i][j][1] -= 1

            if arr[i][j]:
                valid[i][j] = [arr[i][j], K]


def move(x, y, s_num):
    s_dir = shark_dir[s_num - 1]
    next_dir = direction[s_num-1][s_dir - 1]
    for i in range(4):
        nx = x + dx[next_dir[i]]
        ny = y + dy[next_dir[i]]
        if 0 <= nx < N and 0 <= ny < N:
            if not valid[nx][ny]:
                shark_dir[s_num-1] = next_dir[i]
                arr[x][y] = 0
                if arr[nx][ny]:
                    arr[nx][ny] = min(arr[nx][ny], s_num)
                else:
                    arr[nx][ny] = s_num
                return

    for i in range(4):
        nx = x +dx[next_dir[i]]
        ny = y +dy[next_dir[i]]
        if 0<=nx<N and 0<=ny<N:
            if valid[nx][ny][0] == s_num:
                shark_dir[s_num-1] = next_dir[i]
                arr[x][y]=0
                arr[nx][ny] = s_num
                return

def end():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                cnt +=1
    if cnt == 1:
        return True
    return False


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
valid = [[0]*N for _ in range(N)]
shark_dir = list(map(int,input().split()))
direction = []
ans = 0
check()
for _ in range(M):
    tmp = [list(map(int,input().split())) for _ in range(4)]
    direction.append(tmp)

while True:
    flag = end()
    if flag:
        print(ans)
        break
    if ans >= 1000:
        print(-1)
        break
    tmp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and arr[i][j] not in tmp:
                tmp.append(arr[i][j])
                move(i, j, arr[i][j])
    check()
    ans += 1