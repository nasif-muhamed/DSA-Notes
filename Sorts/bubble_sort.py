def bubble_sort(arr):
    count = 1
    sort = True
    while sort:
        sort = False
        for i in range(len(arr) - count):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort = True
        count += 1
    return arr

array = [2, 8, 1, -10, -3]
print("Sorted array is:", bubble_sort(array))


def bubble_sort_2(arr):
    for i in range(len(arr)):
        sort = False
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sort = True
        if not sort:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", bubble_sort_2(arr))

arr2 = [1, 2, 3, 4, 5]
print("Sorted array is:", bubble_sort_2(arr2))
