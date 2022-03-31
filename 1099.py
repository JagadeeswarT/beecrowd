odd_count = []

N = int(input())
for _ in range(N):
    count = 0
    x, y = map(int, input().split(" "))
    if x > y:
        x, y = y, x
    if x < y:
        for i in range(x + 1, y):
            if i % 2 != 0:
                count += i
    odd_count.append(count)
for x in odd_count:
    print(x)
