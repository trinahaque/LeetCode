# Time Complexity: O(n) --> traverses every node to compare depth
# Space Complexity: O(n) --> if tree is linear

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if leftDepth >= rightDepth:
            return 1 + leftDepth
        else:
            return 1 + rightDepth