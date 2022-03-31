"""def fibonacci(N):
    if N <= 1:
        return N
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)"""


def fibonacci(N):
    if N <= 1:
        return N
    x = 0
    y = 1
    result = 0
    for _ in range(N - 1):
        result = x + y
        x = y
        y = result
    return result


T = int(input())
for _ in range(T):
    X = int(input())
    result = fibonacci(X)
    print(f"Fib({X}) = {result}")
