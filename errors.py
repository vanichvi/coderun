n = int(input())
posib_errors = 0
errors = []

for i in range(n):
    a, b = map(int, input().split())
    cur = a * b
    errors.append(cur)
    posib_errors += cur
for i in errors:
    print(i / posib_errors)
