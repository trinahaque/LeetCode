Class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# Assumption that the Node value exist in the Linked List
# No need to check for edge cases when the Node value doesn't exist
# Node will never equal to tail node
# At least two nodes in the linked list
# All values are unique
# Do not return anything

# Head = [4,5,1,9], node = 5
# Output [4, 1, 9]

# Time Complexity: Constant or O(1)
# Space Complexity: Constant/0
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
    