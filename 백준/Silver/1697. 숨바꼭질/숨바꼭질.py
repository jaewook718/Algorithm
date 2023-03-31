import sys
import queue

def bfs(n,k):
    q=queue.Queue()
    q.put(n)
    while q:
        x = q.get()
        if x==k:
            print(dist[x])
            break

        for nx in (x-1,x+1,2*x) :
            if 0<=nx<=max and not dist[nx]:
                dist[nx] = dist[x] +1
                q.put(nx)

input = lambda : sys.stdin.readline().rstrip()
n, k = map(int,input().split())

q = queue.Queue()
q.put(n)
max = 100000
dist =[0]*(max+1)

bfs(n,k)