from addNode import *

# Time Complexity: 2n
# Space Complexity: Constant (only created variable curr2, reversePoint, head2, prev, next)
def isPalindrome(head):
    # Edge case: if list is empty or has only one value
    if head == None or head.next == None:
        return True
    
    # find size of linked list
    count = 1
    current = head
    # O(n) for the whole list
    while current.next:
        count += 1
        current = current.next
    
    # finding middle point
    if count % 2 != 0:
        middle = int(count/2) + 1
    else:
        middle = int(count/2)
    # print ("middle is ", middle)
    reversePoint = 0
    curr1 = head
    
    # n/2
    while reversePoint < middle:
        curr1 = curr1.next
        reversePoint += 1
    
    # reversing the linked list
    # n/2
    curr2 = curr1
    prev = None
    while curr2:
        next = curr2.next
        curr2.next = prev
        prev = curr2
        curr2 = next
    
    curr2 = prev
    curr1 = head
    
    # n/2
    while curr2:
        # print ("curr2 is ", curr2.val, " curr1 is ", curr1.val)
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True


sll = SinglyLinkedList()
sll.addLast(1)
sll.addLast(0)
sll.addLast(0)
print (isPalindrome(sll.head))
# sll.print()