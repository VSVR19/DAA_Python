"""
RUN THIS CODE IN JUPYTER NOTEBOOKS, NOT IN PYCHARM
"""


# This class assigns values to linked list nodes and temporarily assigns the nextnodes to be none.
class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# The method which will reverse the linked list.
def reverse(head):
    # Variable initializations; we start with the head of the linked list.
    current = head
    previous = None
    nextnode = None

    # We traverse the length of the linked list; so the time complexity is O(n).
    while current:
        # Lines 20 and 21 are for the current iteration.
        # We make a copy of the nextnode before its overwritten.
        nextnode = current.nextnode
        # Acxtual reversal- the nextnode is set as the previous node of this current node.
        current.nextnode = previous
        # Lines 23 and 24 are for the next iteration.
        # The next iterations' previous node is this iterations' current node.
        previous = current
        # The copy of the current node made in line 21, is made as the current node to be used in the next iteration.
        current = nextnode

    # Finally, the head is set to the last node in the actual un-reversed list.
    head = previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)

# This line will produce a error as the list is not yet reversed
# and d.nextnode has a value of 'None'.
d.nextnode.value

# Actual reversing occurs here.
reverse(a)

print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

# Now, a will have its nextnode value as 'None' and hence this line will generate an error.
print(a.nextnode.value)