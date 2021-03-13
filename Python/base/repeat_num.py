"""
题目一：找出数组中重复的数字。
在一个长度为n 的数组里的所有数字都在O ~n....:1 的范围内。数组中某
些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了
几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7 的数
组{2, 3, 1., 0, 2, 5, 3} ，那么对应的输出是重复的数字2 或者3。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers):
        # write code here
        num_len = len(numbers)
        if numbers == None or num_len <= 0:
            return False
        for num in numbers:
            if num < 0 or num > num_len - 1:
                return False
        for i in range(num_len):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication = numbers[i]
                    return True, duplication
                # numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
                temp = numbers[numbers[i]]
                numbers[numbers[i]] = numbers[i]
                numbers[i] = temp
        return False

print(Solution().duplicate([2,1,3,2,4]))