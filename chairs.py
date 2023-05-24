import sys

n, m = map(int, sys.stdin.readline().split())
chairs = list(map(int, sys.stdin.readline().split()))
customers = list(map(int, sys.stdin.readline().split()))
chairs.sort()
customers.sort(reverse=True)
res = 0
min_len = min(len(chairs), len(customers))
for i in range(min_len):
    cur_dif = customers[i] - chairs[i]
    if cur_dif > 0:
        res += cur_dif
print(res)
