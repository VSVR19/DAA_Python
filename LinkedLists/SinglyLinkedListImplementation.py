# This class implements a Singly Linked List.
class Node:

    # This constructor assigns values to nodes and temporarily makes the next node as 'None'.
    def __init__(self, value):
        self.value = value
        self.nextnode = None

# Setting up nodes and their values.
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# Linking nodes to set up a singly linked list.
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# Printing the nextnode of each node in the singly linked list.
print(a.nextnode.value)  # 2
print(b.nextnode.value)  # 3
print(c.nextnode.value)  # 4
print(d.nextnode.value)  # 5
# print(e.nextnode.value)  # Error- 'NoneType' object has no attribute 'value'.
