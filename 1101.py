while True:
    x, y = map(int, input().split(" "))
    sum = 0
    if x <= 0 or y <= 0:
        break
    if x > y:
        x, y = y, x
    for i in range(x, y + 1):
        print(i, end=" ")
        sum += i
    print("Sum={}".format(sum))
