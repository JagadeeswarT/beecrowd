X = int(input())
for _ in range(X):
    total = 0
    N = int(input())
    for i in range(1, N):
        if N % i == 0:
            total += i
    if total == N:
        print("{} eh perfeito".format(N))
    else:
        print("{} nao eh perfeito".format(N))
