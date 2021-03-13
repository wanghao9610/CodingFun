def binary_search(arr, x):
    if len(arr) > 0:
        mid = len(arr) // 2
        if arr[mid] == x:
            return True
        if arr[mid] < x:
            return binary_search(arr[mid + 1:], x)
        if arr[mid] > x:
            return binary_search(arr[0:mid], x)
    else:
        return False


# print(binary_search([0, 1, 1, 1, 2, 3, 4, 5, 7, 34, 50], 1))


def binary_search_v2(arr, start, end, x):
    if arr is None or start < 0 or start > end:
        raise Exception("Invalid input parameters.")
    assert (end - start - 1) <= len(arr), 'Search range is out range of the length of array.'

    if end >= start:
        mid = (start + end - 1) // 2
        if arr[mid] == x:
            return True
        if arr[mid] < x:
            return binary_search_v2(arr, start, mid - 1, x)
        if arr[mid] > x:
            return binary_search_v2(arr, mid + 1, end, x)
    else:
        return False


# print(binary_search_v2([0, 1, 1, 1, 2, 3, 4, 5, 7, 34, 50], 0, 10, 50))

def binary_search_non_recursive(arr, start, end, x):
    if arr is None or start < 0 or start > end:
        raise Exception("Invalid input parameters.")
    assert (end - start - 1) <= len(arr), 'Search range is out range of the length of array.'

    while start <= end:
        mid = start + (end - start) >> 1
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return True
    return False


print(binary_search_non_recursive([0, 1, 1, 1, 2, 3, 4, 5, 7, 34, 50], 0, 10, 0))
