def recur(level, sign, cur, num,string):
    if level == N:
        cur += sign*num
        if cur == 0:
            print(string)
    else:
        recur(level+1, sign, cur, num*10+level+1, string+' '+str(level+1))
        recur(level+1, 1, cur+sign*num, level+1, string+'+'+str(level+1))
        recur(level+1, -1, cur+sign*num, level+1, string+'-'+str(level+1))


t = int(input())

for _ in range(t):
    N = int(input())
    recur(1,1,0,1,"1")
    print()


