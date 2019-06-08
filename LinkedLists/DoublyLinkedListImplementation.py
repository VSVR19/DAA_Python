class Node:

    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None


a = Node("DEN")
b = Node("CLT")
c = Node("PHL")
d = Node("LGA")

print(a.value)
a.next_node = b
print(a.next_node.value)

print(b.value)
b.previous_node = a
b.next_node = c
print(b.previous_node.value)
print(b.next_node.value)

d.next_node = a
print(d.next_node.value)





