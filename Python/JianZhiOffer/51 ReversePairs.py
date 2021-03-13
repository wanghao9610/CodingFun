"""在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。"""

# based merge sort, 1) counting the left part reverse paris, 2) counting the right part reverse paris, 3) counting the crossPart reverse paris;
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def recur(arr, left, right, tmp):
            if left == right:  # exit conditon.
                return 0
            mid = left + (right - left) // 2  # partition pivot.
            # mid = (left + right) >> 1
            leftPairs = recur(arr, left, mid, tmp)  # recursively calculate the left part.
            rightPairs = recur(arr, mid + 1, right, tmp)  # recursively calculate the right part.
            if arr[mid] <= arr[
                mid + 1]:  # if the last element of the left part is less than the first element of the right part(the two part is ordered.), directly return the leftPairs plus rihgtPairs.
                return leftPairs + rightPairs
            crossPairs = mergeAndCount(arr, left, mid, right, tmp)
            return leftPairs + rightPairs + crossPairs

        def mergeAndCount(arr, left, mid, right, tmp):
            for i in range(left, right + 1):  # copy all elments between the left and right to tmp array.
                tmp[i] = arr[i]

            i, j, count = left, mid + 1, 0  # init
            for k in range(left, right + 1):  # traverse elements between the range of left and right.
                if i > mid:  # if i index larger than mid, the left part is empty.
                    arr[k] = tmp[j]
                    j += 1
                elif j > right:  # if j index large tha mid, the right part is empty.
                    arr[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:  # compare the left part with the right part. non reversePaired.
                    arr[k] = tmp[i]
                    i += 1
                else:  # compare the left part with the right part. reversePaired.
                    arr[k] = tmp[j]
                    j += 1
                    count += (mid - i + 1)  # reverveParis plus the crossReversePairs (mid - i + 1).
            return count

        if len(nums) < 2:  # if only two or less elements, return 0
            return 0
        tmp = [0] * len(nums)  # create a auxiliary list to copy the given nums.
        return recur(nums, 0, len(nums) - 1, tmp)  # call function and retun the ans.