def bubble_sort(mylist, ascend=False, descend=False):
    """
    :param mylist:to be sorted list
    :return: sorted list
    :param normal:from small to big
    """
    assert ascend ^ descend is True
    for i in range(len(mylist)):
        for j in range(len(mylist) - 1):
            if ascend:
                if mylist[j + 1] < mylist[j]:
                    # from small to big
                    mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            if descend:
                if mylist[j + 1] > mylist[j]:
                    # from big to small
                    mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
                    # tmp = mylist[j+1]
                    # mylist[j+1] = mylist[j]
                    # mylist[j] = tmp
    return mylist


# print(bubble_sort([4, 1, 7, 34, 2, 0, 5, 3, 7], descend=True))


def selection_sort(mylist):
    """
    Time complexity: best case: n*n ,if inner loop if condition is always wrong
    worst case : n*n
    Space Complexity :o(1)
    :param mylist:
    :return:
    """
    for i in range(len(mylist)):
        index = i
        for j in range(i + 1, len(mylist)):
            if mylist[index] > mylist[j]:
                index = j
        mylist[i], mylist[index] = mylist[index], mylist[i]

    return mylist


# print(selection_sort([4,1,7,34,2,0,5,3,7]))

def insert_sort(mylist):
    """
    Time complexity: best case: O(n),
    worse case: O(n*n)
    :param mylist:
    :return:
    """
    for i in range(1, len(mylist)):
        if mylist[i - 1] > mylist[i]:
            for j in range(0, i):
                if mylist[j] > mylist[i]:
                    mylist[j], mylist[i] = mylist[i], mylist[j]

    return mylist


# print(insert_sort([4,1,7,34,2,0,5,3,7]))

# def merge_sort(mylist):
#     """
#     Time complexity: O(n*log n)
#     :param mylist:
#     :return:
#     """
#     if len(mylist) <= 1:
#         return mylist
#     mid = int(len(mylist) / 2)
#     left = merge_sort(mylist[0:mid])
#     right = merge_sort(mylist[mid:len(mylist)])
#     merged = left + right
#
#     for i in range(len(merged)):
#         if merged[i - 1] > merged[i]:
#             for j in range(0, i):
#                 if merged[j] > merged[i]:
#                     merged[j], merged[i] = merged[i], merged[j]
#
#     return merged


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    if arr is None:
        raise Exception("Invalid array input.")

    def merge(_left, _right):
        result = []
        while _left and _right:
            if _left[0] < _right[0]:
                result.append(_left.pop(0))
            else:
                result.append(_right.pop(0))
        while _left:
            result.append(_left.pop(0))
        while _right:
            result.append(_right.pop(0))
        return result

    mid = int(len(arr) / 2)
    left, right = arr[0:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([50, 1, 4, 1, 7, 34, 2, 0, 5, 3, 1]))


# def quick_sort(mylist):
#     """
#     Time Complexity:O(N*log N)
#     Space Complexity: O(N)
#     :param mylist:
#     :return:
#     """
#     less = []
#     equal = []
#     grater = []
#     if len(mylist) <= 1:
#         return mylist
#     # base = mylist[0]
#     import random
#     index = random.randint(0, len(mylist) - 1)
#     base = mylist[index]
#     for num in mylist:
#         if num > base:
#             grater.append(num)
#         elif num < base:
#             less.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(less) + equal + quick_sort(grater)

def partition(_arr, _start, _end):
    if _arr is None or _start < 0 or _end > len(_arr):
        raise Exception("Invalid Parameters")

    import random
    index = random.randint(_start, _end - 1)  # random select a number to reduce the complexity
    _arr[index], _arr[_end] = _arr[_end], _arr[index]  # swap the last element with the selected element
    small = _start - 1  # pointer that point to the small index, function: travel along with _arr
    for i in range(_start, _end):
        if _arr[i] < _arr[_end]:
            small += 1
            _arr[small], _arr[i] = _arr[i], _arr[small]
    small += 1
    _arr[small], _arr[_end] = _arr[_end], _arr[small]  # swap the middle position number with the last
    # number(be compared)
    return small


def quick_sort(arr, start, end):
    if start == end:
        return arr

    index = partition(arr, start, end)
    if index > start:
        arr = quick_sort(arr, start, index - 1)     # here is (index - 1)
    if index < end:
        arr = quick_sort(arr, index + 1, end)
    return arr

print(quick_sort([0,0,0,2,0,5], 0, 5))
