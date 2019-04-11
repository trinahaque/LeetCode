class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# Time Complexity: O(l1) + O(l2)--> O(n)
# Space Complexity: Constant (only head reference/variable is created)
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None and l2 == None:
        return None
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    p = l1
    q = l2
    if p.val <= q.val:
        head = p
        p = p.next
    else:
        head = q
        q = q.next
    current = head
    while p and q:
        if p.val <= q.val:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next
        current = current.next
    if p == None:
        current.next = q
    else:
        current.next = p
    return head
      


                
