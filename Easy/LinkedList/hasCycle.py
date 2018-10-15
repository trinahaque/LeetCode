class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Space Complexity: Constant since it's only storing two pointers
# Time Complexity
# No Cycle: O(n) whenever the fast pointer reaches the end (n/2)
# Cycle: O(N+K) which is O(n)
# Readup LeetCode Time Complexity
class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        
        # Slow has to be the first value. Otherwise fast will catch up to slow even though 
        # there is no cycle
        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True