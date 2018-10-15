Class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

Class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            prev = None
            current = head
            next = head.next
            
            while next:
                current.next = prev
                prev = current
                current = next
                next = next.next

            current.next = prev
            return current
    
    # Reverse a singly linked list iteratively
    # Time Complexity: O(n) where n is the number of nodes
    # Space Complexity: O(1)
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
        