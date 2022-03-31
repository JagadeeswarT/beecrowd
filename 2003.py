while True:
    try:
        hours = input().split(":")
        n = int(int(hours[0]) * 60) + int(hours[1]) - 420
        if n < 0:
            n = 0
        print("Atraso maximo: %d" % n)
    except EOFError:
        break
