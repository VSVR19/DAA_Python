class Stack:

    def __init__(self):
        # Initializing a list here which will act as a Stack.
        self.items = []

    def print_stack(self):
        return self.items

    # Checking the length of the stack.
    def is_empty(self):
        return self.items == []

    # We insert elements in a stack at the last; so- append.
    def inset_new(self, item):
        self.items.append(item)

    # Pop- returns the last item from the stack; removes it as well.
    def pop_item(self):
        return self.items.pop()

    # Peek- this too returns last items from the stack; doesnt remove it though.
    def sneak_peek(self):
        return self.items[len(self.items) - 1]

    # Return the size of the stack.
    def return_size(self):
        return len(self.items)


ObjectStack = Stack()
print("Is Stack Empty ? " + str(ObjectStack.is_empty()))

ObjectStack.inset_new(19)
ObjectStack.inset_new("VSVR")
ObjectStack.inset_new(33)
ObjectStack.inset_new("SRW")

print("The Stack is: {0}".format(ObjectStack.print_stack()))

print("Popped Item: " + str(ObjectStack.pop_item()))

print("Peek Result: " + str(ObjectStack.sneak_peek()))

print("Size of Stack: "+ str(ObjectStack.return_size()))