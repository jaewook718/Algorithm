H, W, N, M = map(int,input().split())
ans = ((H-1)//(N+1)+1)*((W-1)//(M+1)+1)
print(ans)