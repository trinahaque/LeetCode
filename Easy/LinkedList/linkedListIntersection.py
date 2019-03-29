# Time Compexity: O(m+n)
# Space Complexity: O(1)/constant

def getIntersectionNode(headA, headB):
    # if either list is empty, there is no intersection
    if headA == None or headB == None:
        return None
    
    currA = headA
    currB = headB
    countA = 0
    countB = 0
    
    # O(n)
    while currA:
        countA += 1
        currA = currA.next
    
    # O(m)
    while currB:
        countB += 1
        currB = currB.next
    
    # O(n)
    if countA > countB:
        diff = countA - countB
        num = 0
        while num < diff:
            headA = headA.next
            num += 1
    else:
        diff = countB - countA
        num = 0
        while num < diff:
            headB = headB.next
            num += 1
    # O(n)
    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None