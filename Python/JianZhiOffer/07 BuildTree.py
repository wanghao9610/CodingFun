"""输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This is a recursive practice. May be difficult. Need rewite. 0228
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildMyTree(root, left, right):  # input the boundary indexes of root in preorder, left, right in Inorder
            if left > right:
                return

            node = TreeNode(preorder[root])
            inorder_index = inorder_indexes[preorder[root]]  # search the root on the hash table of inorder
            node.left = buildMyTree(root + 1, left, inorder_index - 1)  # recur the left tree
            node.right = buildMyTree(inorder_index - left + root + 1, inorder_index + 1, right)  # recur the right tree
            # (inorder - left) means the length of left tree,
            # and then plus (root + 1) means the right boundary of right tree
            return node

        inorder_indexes = {elem: i for i, elem in enumerate(inorder)}  # build a hash table with key: elem, value: index
        return buildMyTree(0, 0, len(inorder) - 1)