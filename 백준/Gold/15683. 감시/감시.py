from sys import stdin
from collections import deque
from itertools import product
input = stdin.readline

# 사무실 세로, 가로
N, M = map(int,input().split())
office = [list(map(int,input().split())) for _ in range(N)]

# 카메라 위치(r,c)와 종류 체크(num), 이 카메라로 감시 가능한 구역 리스트([])
camera = []
# CCTV 감시 할 구역
check_area_num = 0
for r in range(N):
    for c in range(M):
        if 1<= office[r][c] <= 5:
            camera.append([r,c,office[r][c],[]])
        elif office[r][c] == 0:
            check_area_num +=  1

# 감시
def watch(cam_num, cam):
    for direction in cam_num:
        # 지금 방향으로 감시한 구역
        area = []
        for dr,dc in direction:
            # CCTV는 감시할 수 있는 방향에 있는 구역 전체를 감시
            q = deque()
            q.append((cam[0],cam[1]))
            while q:
                cr,cc = q.popleft()
                # 이동
                nr = cr + dr
                nc = cc + dc
                # 사무실 내인가
                if 0 <= nr < N and 0 <= nc < M:
                    # 벽이면 패스
                    if office[nr][nc] == 6:
                        break
                    else:
                        q.append([nr,nc])
                        # 감시할 구역이면
                        if office[nr][nc] == 0:
                            area.append([nr,nc])
        # 지금 방향으로 감시한 구역들을 이 카메라로 감시 가능한 구역리스트에 넣기
        cam[3].append(area)


# 각 감시카메라의 관찰 방향
c1_d = [[[-1,0]],[[1,0]],[[0,-1]],[[0,1]]]
c2_d = [[[-1,0],[1,0]],[[0,-1],[0,1]]]
c3_d = [[[-1,0],[0,-1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[1,0],[0,1]]]
c4_d = [[[-1,0],[1,0],[0,-1]], [[-1,0],[1,0],[0,1]], [[-1,0],[0,-1],[0,1]],[[1,0],[0,-1],[0,1]]]
c5_d = [[[-1,0],[1,0],[0,-1],[0,1]]]

# 감시해보자...
for cam in camera:
    r,c,num = cam[:3]
    if num == 1:
        watch(c1_d,cam)
    elif num == 2:
        watch(c2_d,cam)
    elif num == 3:
        watch(c3_d,cam)
    elif num == 4:
        watch(c4_d,cam)
    elif num == 5:
        watch(c5_d,cam)

# 감시한 구역들 모으기
areas = []
for cam in camera:
    areas.append(cam[3])
# print(areas)
# -> [[[i번 카메라 j번째 감시 구역 list],[i번째 카메라 j+1번째 감시구역 list]...],[...]]

# 감시할 구역은 최대 64 (가로 세로 최대가 8)
blind_spot = 64
# 각 카메라에 감시구역 경우의 수 1개씩 뽑아서 사각지대 갯수 세기
# cartesian product
for a in product(*areas):
    # print(a)
    # -> ([i번째 카메라 감시 구역 list],[...])
    
    # 현재 감시 구역(중복 제외)
    watch = set()
    for i in a:
        # print(i)
        # -> [[r1,c1],[r2,c2]...]
        for r,c in i:
            watch.add((r,c))
    # 사각지대 구역 수가 최소인가?
    if blind_spot > check_area_num - len(watch):
        blind_spot = check_area_num - len(watch)

# 결과
print(blind_spot)