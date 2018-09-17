def BubbleSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def OptimizedBubbleSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        swap = 0
        for j in range(0,n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],a[j+1] = a[j+1],a[j]
                swap = 1
        if (swap == 0):
            break
    return arr
                

arr = [1,4,6,3,2]
print(BubbleSort(arr))
print(OptimizedBubbleSort(arr))
