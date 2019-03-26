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

# 3/25
# Time Complexity: O(n) --> iterate through all nodes
# Space Complexity: O(3) --> constant
def reverseList(self, head):
        if head == None or head.next == None:
            return head
        else:
            prev = None
            current = head
            next = current.next
            while next:
                current.next = prev
                prev = current
                current = next
                next = next.next
            current.next = prev
            head = current
            return head
        