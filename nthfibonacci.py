# Get the nth fibonacci number using recursion

n = int(input())
def getFibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return getFibonacci(n-1) + getFibonacci(n-2)

print(getFibonacci(6))