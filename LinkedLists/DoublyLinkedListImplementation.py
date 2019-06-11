# This class implements a Singly Doubly List.
class Node:

    # This constructor assigns values to nodes and
    # temporarily makes the nextnode and previousnode as 'None'.
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.previousnode = None

# Setting up nodes and their values.
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# Linking nodes to set up a doubly linked list.
a.nextnode = b

b.nextnode = c
b.previousnode = a

c.nextnode = d
c.previousnode = b

d.nextnode = e
d.previousnode = c

e.previousnode = d

# Printing the nextnode and previousnode of each node in the singly linked list.
print(a.nextnode.value)  # 2

print(b.nextnode.value)  # 3
print(b.previousnode.value)  # 1

print(c.nextnode.value)  # 4
print(c.previousnode.value)  # 2

print(d.nextnode.value)  # 5
print(d.previousnode.value) # 3

print(e.previousnode.value)  # 4
