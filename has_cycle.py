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
    
    def __repr__(self):
        return str({'value' : self.data, 'next' : self.next})


def has_cycle(head):
    pass



ll = LinkedNode(1)

ll.attach(100)
ll.attach(200)
print(ll)


# for n in range(10):
#     num = randint(0,1000)
#     ll.attach(num)



