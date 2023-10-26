N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

sensors_diff = [sensors[i]-sensors[i-1] for i in range(1, N)]
sensors_diff.sort()

print(sum(sensors_diff[:N-K]))