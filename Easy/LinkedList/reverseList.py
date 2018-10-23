Class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

Class Solution:
    # Reverse a singly linked list iteratively
    # Time Complexity: O(n) where n is the number of nodes
    # Space Complexity: O(1)
    # Handles edge cases such as head is none or only one node in the list
    def reverseListRefactored(self, head):
        prev = None
        current = head
        # this solution handles edge cases where head is none or a single value
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
        