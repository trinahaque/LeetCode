class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeTwoLists(self, l1, l2):
    # l1 and l2 are list nodes
    if l1 == None and l2 == None:
        return None
    elif l1 == None and l2 != None:
        return l2
    elif l2 == None and l1 != None:
        return l1
    else:
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        current = head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1 == None:
            current.next = l2
        else:
            current.next = l1
        return head
def mergeSortedList(l1, l2):
    if l1 == None and l2 == None:
        return None
    if l1 == None and l2 != None:
        return l2
    if l1 != None and l2 == None:
        return l1
    
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    
    current = head
    p = l1
    q = l2
    while p != None and q != None:
        if p.val <= q.val:
            current = p
            p = p.next
        else:
            current = q
            q = q.next
        current = current.next
    if q is None:
        current = p
    else:
        current = q
    return head


                
