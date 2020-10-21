# Time Complexity: O(N) --> loop1 + 1/2 loop
# Space Complexity: Constant  --> creating variables

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    size = 0
    current = head
    # find the length of the linked list
    while current:
        size += 1
        current = current.next
    middle = int(size/2)
    counter = 0
    curr = head
    # find the middle node
    while counter < middle:
        curr = curr.next
        counter += 1
    return curr


# 2nd approach with runner
# if fast reaches the end, that means we are in the middle
# Time Complexity: O(N)
# Space Complexity: Constant
def middleNode(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow