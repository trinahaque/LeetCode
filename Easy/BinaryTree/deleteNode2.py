# Given a root node reference of a BST and a key, delete the node with the given key 
# in the BST. Return the root node with the updated BST

# Two stages:
# 1) Search for a node to remove
# 2) If the node is found, delete the node

# Time Complexity: O(height of tree)

# Cases:
# a) Zero Child
# b) One Child
# c) Two Children

class Solution:
    # Given root of a tree, return the node with minimum value
    def minValueTree(self, root):
        if root == None:
            return None
        current = root
        while current.left != None:
            current = current.left
        return current