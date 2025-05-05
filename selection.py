def selection(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
        print(f"Passs {i} {arr}")

    print(arr)

selection([5,3,4,2,1])            
