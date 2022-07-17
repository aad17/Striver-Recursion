# Reverse an array using recursion

arr = [0, 1, 4, 2, 4, 1, 5, 7, 8]

def reverseArr(arr, i, j):
    if i >= j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    reverseArr(arr, i+1, j-1)

reverseArr(arr, 0, len(arr)-1)
print(arr)