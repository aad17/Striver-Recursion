arr = [1, 2, 1]
n = len(arr)
target = 2 

def countf(index, arr, suma, n, ds, target):
    if index >= n:
        if suma == target:
            return 1
        else:
            return 0

    ds.append(arr[index])
    suma += arr[index]
    l = countf(index+1, arr, suma, n, ds, target)

    ds.pop()
    suma -= arr[index]
    r = countf(index+1, arr, suma, n, ds, target)

    return l + r

print(countf(0, arr, 0, n, [], target))