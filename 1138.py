def solve(a, b):
    total = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for k in range(a, b):
        while k != 0:
            rem = k % 10
            total[rem] += 1
            k = k // 10
    return total


if __name__ == "__main__":
    while True:
        x, y = [int(i) for i in input().split(" ")]
        if x == 0 and y == 0:
            break
        val = solve(x, y + 1)
        print(" ".join(map(str, val.values())))
