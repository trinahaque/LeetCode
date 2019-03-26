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

# Time Complexity: O(n) --> categorically
# Space Complexity: O(1) --> constant
def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # empty list
        if head == None:
            return False
        slow = head
        fast = head.next
        
        # it has cycle if both fast and slow point to the same node
        while slow != fast:
            # handles cyclibility with one node cycle/pointing to itself
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True