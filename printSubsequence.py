arr = [3, 1, 2]
n = len(arr)

def printSubsequence(ind, ds, arr, n):
    if ind >= n:
        print(ds)
        return
    # Take Condition
    ds.append(arr[ind])
    printSubsequence(ind+1, ds, arr, n)
    # Remove Condition
    ds.pop()
    printSubsequence(ind+1, ds, arr, n)

printSubsequence(0, [], arr, n)