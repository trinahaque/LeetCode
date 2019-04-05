class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Time Complexity: O(n) --> iterate through all nodes
    # Space Complexity: Constant --> only variable current created
    def addLast(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            return

    def print(self):
        current = self.head
        while current:
            print (current.val)
            current = current.next

# sll = SinglyLinkedList()
# sll.addLast(1)
# sll.addLast(5)
# sll.print()