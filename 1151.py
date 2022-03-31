list1 = [0, 1, 1]

list1 = [0, 1, 1]
N = int(input())
if N <= 3:
    print(" ".join([str(list1[i]) for i in range(N)]))
else:
    for i in range(3, N):
        list1.append(list1[i - 1] + list1[i - 2])
    print(" ".join([str(list1[i]) for i in range(N)]))
