def secondLargetElement(arr):
    n = len(arr)

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                arr[i],arr[j] = arr[j],arr[i]

    return arr[1]

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(secondLargetElement(arr))