"""
RUN THIS CODE IN JUPYTER NOTEBOOKS, NOT IN PYCHARM
"""


# This class assigns values to linked list nodes and temporarily assigns the nextnodes to be none.
class Node:

    # This constructor assigns values to nodes and initialises next node to be none.
    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Method which will return us the nth to last node.
# Takes in head of the link list and the number 'n'.
def nth_to_last_node(n, head):
    # We have two pointers and they are initialized to the head of the link list.
    left_pointer = head
    right_pointer = head

    # Creating a bar of length n-1-- stil not getting this!
    for i in range(n - 1):
        # Move the right_pointer n-1 nodes away from the left pointer.
        right_pointer = right_pointer.nextnode

        # If n is out of the link list, the user has entered a wrong 'n'.
        if right_pointer is None:
            raise LookupError("Not enough number of nodes dude!")

    # Keep moving the right pointer till the reach the last element in the linked list.
    while right_pointer.nextnode:
        # Move the left and right pointers one node at a time.
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # When the right pointer reaches 'null', the left pointer is the requested 'nth' node from the last.
    return left_pointer


# Setting up the nodes of the linked list.
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# Connecting the previously set up nodes so that they form a linked list.
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)

# Printing the target nodes' value.
target_node.value