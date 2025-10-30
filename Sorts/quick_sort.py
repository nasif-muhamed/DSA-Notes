# simple - not efficient - takes n space complexity.
def simple_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = len(arr) // 2

    left = [x for x in arr if x < arr[pivot]]
    middle = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return simple_quick_sort(left) + middle + simple_quick_sort(right)


if __name__ == "__main__":
    unsorted_list = [5, 4, 3, 6, 4, 15, 15, 7]
    sorted_list = simple_quick_sort(unsorted_list)
    print("Sorted List:", sorted_list)


# more efficient - in place - takes log n space complexity for the stack only.
def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Example usage:
nums = [10, 7, 8, 9, 1, 5]
quick_sort_in_place(nums, 0, len(nums) - 1)
print("Sorted array:", nums)
