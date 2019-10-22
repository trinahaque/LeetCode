# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Oct 21st, 2019
class Solution2:
    def sortedArrToBST(self, nums) -> TreeNode:
        # empty list
        if len(nums) < 1:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        print (node.val)
        node.left = self.sortedArrToBST(nums[:mid])
        node.right = self.sortedArrToBST(nums[mid+1:])
        return node
        
s2 = Solution2()
s2.sortedArrToBST([-10, -3, 0, 5, 9])