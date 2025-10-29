def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found target
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found


def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)
    

arr = [2, 4, 7, 10, 15, 20, 25, 30]
target = 15

result = binary_search(arr, target)
print(result)  # Output: 4

