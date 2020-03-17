class LinkedNode:
    def __init__(self,val=None):
        self.value = val
        self.next = None
    
    def __repr__(self):
        return str({'value' : self.value, 'next' : self.next})

def deleteKey(ll,key):
    print(ll)
    removed = 0
    remaining = []
    node = ll
    prev = None

    if not ll.value:
        return 0

    while ll.value == key:
    # if node.value == key:
        removed += 1
        ll = ll.next
        if ll is None:
            break
        # prev = node
        # node = node.next #go to next element
        # ll = ll.next
        # prev.next = None
        # prev.next = node.next

    print(ll)

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
    node = ll

    while node:
        remaining.append(node.value)
        node = node.next

    return remaining


ll = LinkedNode(1000)
ll.next = LinkedNode(1000)
ll.next.next = LinkedNode(2)
ll.next.next.next = LinkedNode(4)
ll.next.next.next.next = LinkedNode(5)
ll.next.next.next.next.next = LinkedNode(19)

x = deleteKey(ll,1000)
print(x)




#if l.value doesnt exist, return 0 for length of linked list
#start at beginning of list
#traverse the list, and compare the value to k
#if the value = k, set the next of the previous to the current.next
#keep track of previous???
#increment a count of elements removed.  return 1 with the count of all values removed