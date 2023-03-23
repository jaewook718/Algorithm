def comb(arr, n) :
    result = []
    if n> len(arr) :
        return result

    if n == 1:
        for i in arr :
            result.append([i])

    elif n > 1:
        for i in range(len(arr)- n + 1):
            for j in comb(arr[i+1:], n - 1):
                result.append([arr[i]]+j)

    return result
def calc_dist(home, chi_list):
    min_dist = 1e9
    for chi in chi_list:
        dist = abs(chi[0] - home[0]) +abs(chi[1]-home[1])
        min_dist = min(min_dist,dist)

    return min_dist

def main():

    n , m = map(int, input().split())

    a =[list(map(int, input().split())) for _ in range(n)]

    chicken = [[i,j] for i in range(n) for j in range(n) if a[i][j] == 2]
    home = [[i,j] for i in range(n) for j in range(n) if a[i][j] ==1]

    chi_list = list(comb(chicken, m))

    ans = []
    for chi in chi_list:
        total = 0
        for h in home:
            total += calc_dist(h, chi)
        ans.append(total)
    print(min(ans))


main()