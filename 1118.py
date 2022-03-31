s = p = 0
while True:
    N = float(input())
    if N < 0 or N > 10:
        print("nota invalida")
    else:
        s += N
        p += 1
        if p == 2:
            print("media = {:.2f}".format(s / 2))
            print("novo calculo (1-sim 2-nao)")
            while True:
                N = int(input())
                if N == 1:
                    s = p = 0
                    break
                elif N == 2:
                    quit()
                else:
                    print("novo calculo (1-sim 2-nao)")
