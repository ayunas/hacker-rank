# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
#Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
from random import randint

class LinkedNode:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next = next_node
    
    def attach(self,val):
        node = self
        prev = None
        while node:
            prev = node
            node = node.next
        prev.next = LinkedNode(val)
        return prev.next
    
    def __repr__(self):
        return str({'value' : self.data, 'next' : self.next})

ll = LinkedNode(randint(1,100))
cyclic = None

for n in range(10):
    num = randint(0,100)
    node = ll.attach(num)
    if n == 3:
        cyclic = node
    if n == 9:
        # print('cyclic', cyclic)
        # print('node', node)
        node.next = cyclic

def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    
    return False

#declare a slow and fast pointer. fast increments by 2.  slow by 1.
#if the fast pointer ever falls behind the slow pointer, we have a cycle
#how to tell if fast pointer falls behind?  if the node has been visited

c = has_cycle(ll)
print(c)

