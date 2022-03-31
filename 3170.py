B = int(input())
G = int(input())

result = G // 2 - B
if result <= 0:
    print("Amelia tem todas bolinhas!")
else:
    print("Faltam {} bolinha(s)".format(result))
