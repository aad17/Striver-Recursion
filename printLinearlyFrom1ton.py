# Print Linearly from 1 to n

n = int(input())
def printNum(n):
    if n == 0:
        return
    printNum(n-1)
    print(n)

printNum(n)