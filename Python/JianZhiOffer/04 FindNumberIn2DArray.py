"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         if matrix is None or len(matrix) == 0:
#             return False
#         rows = len(matrix)
#         columns = len(matrix[0])
#         i = 0
#         j = columns - 1
#         while j >= 0 and i <= rows - 1: # traverse from the top right.
#             if matrix[i][j] == target:
#                 return True
#             if matrix[i][j] > target:   # the judgement order can't be changed
#                 j -= 1
#             if matrix[i][j] < target:
#                 i += 1
#         return False

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        i = rows - 1
        j = 0
        while i >= 0 and j <= columns - 1: # traverse from the buttom left.
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:   # the judgement order can't be changed
                i -= 1
            if matrix[i][j] < target:
                j += 1
        return False