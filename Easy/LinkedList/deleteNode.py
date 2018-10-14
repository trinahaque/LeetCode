Class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# Assumption that the Node value exist in the Linked List
# No need to check for edge cases when the Node value doesn't exist
# Node will never equal to tail node
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
    