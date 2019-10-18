# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Convert sorted array to BST
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return
        mid = int(len(nums) / 2)
        leftRoot = TreeNode(nums[mid])
        rightRoot = TreeNode(nums[mid])
        
        for i in range(mid):
            leftRoot = self.leftTree(leftRoot, nums, mid - i - 1)
            rightRoot = self.rightTree(rightRoot, nums, mid - i - 1)
            
    def leftTree(self, root, nums, index):
        root.left = TreeNode(nums[index])
        return root.left
    
    def rightTree(self, root, nums, index):
        root.right = TreeNode(nums[index])
        return root.right
        