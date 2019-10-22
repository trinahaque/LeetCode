# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode):
        if root == None:
            return self.result
        if root.left:
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.result

s = Solution()
nums = [1, None, 2, 3]
s.inorderTraversal(nums)