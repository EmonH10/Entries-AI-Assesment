def sumPairs(arr,target):
    result = []
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                result.append([arr[i],arr[j]])

    return result


arr=[1, 2, 3, 4, 5]
target=5

print(sumPairs(arr,target))