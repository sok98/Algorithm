def factorial(N):
    if N<=1:
        return 1
    return N * factorial(N-1)

print(factorial(4))