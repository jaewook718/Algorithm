class set:
    def __init__(self,key):
        self.key = key
        self.parent = self
        self.rank = 0

    def find(self):
        v = self
        while v.parent != v:
            v = v.parent

        return v

    def __str__(self):
        return f'{self.key}'


def union(x, y):
    v = x.find()
    w = y.find()
    if v.rank < w.rank:
        v, w = w, v
    w.parent = v
    if v.rank == w.rank:
        v.rank += 1


n, m = map(int, input().split())
arr = [0]*(n+1)
for _ in range(m):
    com, a, b = map(int, input().split())
    if com == 0:
        if arr[a] == 0:
            x = set(a)
            arr[a] = x
        if arr[b] == 0:
            y = set(b)
            arr[b] = y
        union(arr[a], arr[b])
    else:
        if arr[a] == 0:
            x = set(a)
            arr[a] = x
        if arr[b] == 0:
            y = set(b)
            arr[b] = y
        if arr[a].find() == arr[b].find():
            print('YES')
        else:
            print('NO')
