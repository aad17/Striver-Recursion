arr = [3, 1, 2]
n = len(arr)

def printSubsequence(ind, ds, arr, n):
    if ind >= n:
        print(ds)
        return
    ds.append(arr[ind])
    printSubsequence(ind+1, ds, arr, n)
    ds.pop()
    printSubsequence(ind+1, ds, arr, n)

printSubsequence(0, [], arr, n)