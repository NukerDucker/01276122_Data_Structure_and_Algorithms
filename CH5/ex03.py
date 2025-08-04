class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def createList(l=[]):
    head = None
    tail = None
    for item in l:
        new_node = Node(int(item))
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def printList(H):
    current = H
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

def mergeOrderedList(p, q):
    if not p:
        return q
    if not q:
        return p
    
    if p.data < q.data:
        p.next = mergeOrderedList(p.next, q)
        return p
    else:
        q.next = mergeOrderedList(p, q.next)
        return q

usr_input = input("Enter 2 Lists : ")
L1, L2 = usr_input.split()
L1 = L1.split(',')
L2 = L2.split(',')

LL1 = createList(L1)
LL2 = createList(L2)

print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)

m = mergeOrderedList(LL1, LL2)

print('Merge Result : ',end='')
printList(m)