class Node:

    def __init__(self, value):
        self.value = value


a = Node("DFW")
b = Node("ATL")
c = Node("EWR")

a.next_node = b
b.next_node = c

print(a.value)
print(a.next_node.value)
