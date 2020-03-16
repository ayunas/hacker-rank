class LinkedNode:
    def __init__(self,val=None):
        self.value = val
        self.next = None
    
    def __repr__(self):
        return str({'value' : self.value, 'next' : self.next})


def deleteKey(ll,key):

    removed = 0
    node = ll
    prev = None

    if not ll.value:
        return 0

    while node:
        prev = node
        node = node.next
        print('prev', prev)
        print('node', node)
        if not node:
            break
        if node.value == key:
            prev.next = node.next
            removed += 1
        
        
    
    print('updated ll', ll)
    return (1,removed)


ll = LinkedNode(10)
ll.next = LinkedNode(11)
ll.next.next = LinkedNode(12)
ll.next.next.next = LinkedNode(13)

x = deleteKey(ll,13)
print(x)




#if l.value doesnt exist, return 0 for length of linked list
#start at beginning of list
#traverse the list, and compare the value to k
#if the value = k, set the next of the previous to the current.next
#keep track of previous???
#increment a count of elements removed.  return 1 with the count of all values removed