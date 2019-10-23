# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Input: TreeNode
# Output: An array of int after inorder traversal
# Time Complexity: O(n) --> have to traverse all the nodes
# Space Complexity: O(n) --> creating stacks if the tree is linear (all left nodes)
# average O(logn)
class Solution:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root):
        if root == None:
            return self.result
        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result

# nums = [5, 3, null, 4, null, null, 7, null, 9, 8, null]
nums2 = [TreeNode(1), TreeNode(None), TreeNode(2), TreeNode(3)]

