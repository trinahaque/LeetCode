# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self, root):
        self.root = root
        
    def insert(self, root, val, side):
        node = TreeNode(val)
        root.side = node
        return self
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if self.root == None:
            self.root = TreeNode(val)
            return self.root
        if val > root.val and root.right == None:
            self.insert(root, val, right)
        elif val > root.val:
            self.insertIntoBST(root.right, val)
        elif val < root.val and root.left == None:
            self.insert(root, val, left)
        else:
            self.insertBST(root.left, val)
        return self.root