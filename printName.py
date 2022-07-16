# Print your name using recursion n times
# T = O(N)
# S = O(N) Using stack space

n = int(input())
def printName(n):
    if n == 0:
        return
    print('Amey')
    printName(n-1)

printName(n)