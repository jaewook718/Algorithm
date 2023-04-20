di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def add(q):
    _min = min(q)[0]
    for i in range(N):
        if q[i][0] == _min:
            q[i][0] += 1

def pop_left(q):
    tmp = q.pop(0)
    q[0].extend(tmp)

def turn_90(x, y):
    tmp_rotate = [[0]*x for _ in range(y)]
    for i in range(x):
        for j in range(y):
            tmp_rotate[j][x-i-1] = cur_arr[i][j]
    return tmp_rotate


def control():
    tmp_bowls = [[0]*len(bowls[0]) for _ in range(len(bowls))]
    visited = [[0]*len(bowls[0]) for _ in range(len(bowls))]
    for i in range(len(bowls)):
        for j in range(len(bowls[i])):
            visited[i][j] = 1
            tmp_bowls[i][j] += bowls[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < len(bowls) and 0 <= nj < len(bowls[ni]) and not visited[ni][nj]:
                    if bowls[i][j] > bowls[ni][nj]:
                        tmp_bowls[ni][nj] += (bowls[i][j] - bowls[ni][nj])//5
                        tmp_bowls[i][j] -= (bowls[i][j] - bowls[ni][nj])//5
                    else:
                        tmp_bowls[i][j] += (bowls[ni][nj] - bowls[i][j]) // 5
                        tmp_bowls[ni][nj] -= (bowls[ni][nj] - bowls[i][j]) // 5

    for i in range(len(bowls)):
        for j in range(len(bowls[i])):
            bowls[i][j] = tmp_bowls[i][j]


def flatten():
    tmp_arr = []
    for i in range(len(bowls)):
        for j in range(len(bowls[i])):
            tmp_arr.append([bowls[i][j]])
    return tmp_arr


N, K = map(int, input().split())
tmp = list(map(int,input().split()))
bowls = [[t] for t in tmp]
ans = 1


while True:
    add(bowls)
    pop_left(bowls)
    while True:
        cnt = 0
        for i in range(len(bowls)):
            if len(bowls[i])>=2:
                cnt += 1
        if len(bowls[0]) > len(bowls) - cnt:
            break
        cur_arr = []
        for _ in range(cnt):
            cur_arr.append(bowls.pop(0))
        rotate_arr = turn_90(cnt, len(cur_arr[0]))
        for i in range(len(rotate_arr)):
            bowls[i].extend(rotate_arr[i])
    control()
    bowls = flatten()
    cur_arr = []
    for _ in range(N//2):
        cur_arr.append(bowls.pop(0))
    cur_arr = turn_90(N//2, 1)
    rotate_arr = turn_90(1, N//2)
    for i in range(len(rotate_arr)):
        bowls[i].extend(rotate_arr[i])
    cur_arr = []
    for _ in range(N//4):
        cur_arr.append(bowls.pop(0))
    cur_arr = turn_90(N//4, 2)
    rotate_arr = turn_90(2, N//4)
    for i in range(len(rotate_arr)):
        bowls[i].extend(rotate_arr[i])
    control()
    bowls = flatten()
    if max(bowls)[0] - min(bowls)[0] <= K:
        print(ans)
        break
    ans+=1

