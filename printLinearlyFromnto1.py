# Print Linearly from n to 1

n = int(input())
def printNum(n):
    if n == 0:
        return
    print(n)
    printNum(n-1)

printNum(n)