while True:
    X = int(input())
    if X == 0:
        break
    print(" ".join([str(x) for x in range(1, X + 1)]))
