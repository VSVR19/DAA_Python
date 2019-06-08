class Deque:

    # Initializing a empty list to be used as a Queue.
    def __init__(self):
        self.items = []

    # Printing the Deque to check its contents.
    def print_deque(self):
        return self.items

    # Checking whether the Deque is empty.
    def is_empty(self):
        return self.items == []

    # ADD_FRONT- A Stack Operation- items get appended.
    def add_front(self, item):
        self.items.append(item)
        return self.items

    # ADD_REAR- A Queue Operation- items get inserted at the beginning.
    def add_rear(self, item):
        self.items.insert(0, item)
        return self.items


    # REMOVE_FRONT- A Operation common to both Stack and Queue.
    # Removes the latest element in Stack.
    # Removes the VERY FIRST added element in Queue.
    def remove_front(self):
        return self.items.pop()

    # A operation UNIQUE to DEQUES.
    # Removes the FIRST ELEMENT in the Deque.
    def remove_rear(self):
        return self.items.pop(0)

    # Return the size of the Deque.
    def size(self):
        return len(self.items)


ObjectDeque = Deque()

ObjectDeque.add_front(19)
ObjectDeque.add_rear("VSVR")
ObjectDeque.add_rear(33)
ObjectDeque.add_rear("SR")

print("The Deque is: {0}".format(ObjectDeque.print_deque()))

print("Is the Deque empty ? {0}".format(ObjectDeque.is_empty()))

print("Size of the Deque: {0}".format(ObjectDeque.size()))

print("Adding to front of the Deque: {0}".format(ObjectDeque.add_front(44)))
print("Adding to rear of the Deque: {0}".format(ObjectDeque.add_rear("JP")))

print("Removing from front of the Deque: {0}".format(ObjectDeque.remove_front()))
print("The Deque is: {0}".format(ObjectDeque.print_deque()))

print("Removing from rear of the Deque: {0}".format(ObjectDeque.remove_rear()))
print("The Deque is: {0}".format(ObjectDeque.print_deque()))

print("Dequeues size: {0}".format(ObjectDeque.size()))
