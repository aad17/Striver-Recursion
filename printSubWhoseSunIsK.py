arr = [1, 2, 1]
n = len(arr)
target = 2 

def printf(index, arr, suma, n, ds, target):
    if index >= n:
        if suma == target:
            print(ds)
        return
    
    ds.append(arr[index])
    suma += arr[index]
    printf(index+1, arr, suma, n, ds, target)
    suma -= arr[index]
    ds.pop()
    printf(index+1, arr, suma, n, ds, target)

printf(0, arr, 0, n, [], target)