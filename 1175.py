N = []


def swap(N):
    k = len(N)
    for i in range(0, len(N) // 2):
        N[i], N[k - i - 1] = N[k - i - 1], N[i]


for i in range(20):
    X = int(input())
    N.append(X)
swap(N)
k = len(N)
for i in range(k):
    print(f"N[{i}] = {N[i]}")
