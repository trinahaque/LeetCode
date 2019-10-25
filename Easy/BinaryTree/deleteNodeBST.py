# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []

    def search(self, root, key):
        if root == None:
            return None
        if key == root.val:
            return root
        if key > root.val:
            if key == root.right.val:
                return (root, root.right, right)
            else:
                self.search(root.right, key)
        else:
            if key == root.left.val:
                return (root, root.left, left)
            else:
                self.search(root.left, key)
        return None

    def deleteNode(self, root: TreeNode, key: int):
        pass