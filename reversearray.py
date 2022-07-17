# Reverse an array using recursion

arr = [1, 4, 6, 8, 9, 2, 3, 5]

def doReverse(arr, l, r):
    if l >= r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return doReverse(arr, l+1, r-1)

print(doReverse(arr, 0, len(arr)-1))