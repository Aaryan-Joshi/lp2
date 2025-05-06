def selection(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Pass {i + 1}: {arr}")
    print("Sorted array:", arr)

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Original array:", arr)
selection(arr)
