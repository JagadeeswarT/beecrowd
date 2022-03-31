N = int(input())
k = 0
for i in range(1, N + 1):
    for j in range(i * i, i * i + 2):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0) or j == 2:
            print(f"{i} {j} {i*j}")
        else:
            k += 1
            print(f"{i} {j} {i*j-k}")
