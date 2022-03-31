A, B, C = map(float, input().split(" "))

for _ in range(2):
    if A < B:
        A, B = B, A
    if B < C:
        B, C = C, B
print(A, B, C)
