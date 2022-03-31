"""k = 1
X, Y = map(int, input().split(" "))
for i in range(1, Y + 1, X):
    for j in range(i, X + k):
        print(j, end=" ")
    k += X
    print()"""

"""j = 0
X, Y = map(int, input().split(" "))
for i in range(1, Y + 1):
    j += 1
    print(i, end=" ")
    if j == X or i == Y:
        print("\n")
        j = 0"""

X, Y = map(int, input().split(" "))
nums = list(range(0, Y))
for i in nums[::X]:
    print(" ".join([str(num + 1) for num in nums[i : i + X]]))
