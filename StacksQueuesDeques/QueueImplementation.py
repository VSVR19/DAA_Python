class Queue:

    # Initializing a empty list to be used as a Queue.
    def __init__(self):
        self.items = []

    # Printing the Queue to check its contents.
    def print_queue(self):
        return self.items

    # Checking the Queue for any contents.
    def check_length(self):
        return self.items == []

    # ENQUEUING- Adding items to the Queue at the rear-end.
    def add_item(self, item):
        self.items.insert(0, item)

    # DEQUEUING- Removing the top-most item from the queue.
    def remove_item(self):
        return self.items.pop()

    # Returning the length of the Queue.
    def return_size(self):
        return len(self.items)


ObjectQueue = Queue()

print("Is the Queue Empty? {0}".format(ObjectQueue.check_length()))

ObjectQueue.add_item(22)
ObjectQueue.add_item(88)
ObjectQueue.add_item(44)

print("The Queue is: {0}".format(ObjectQueue.print_queue()))

print("Removed/ Popped item: {0}".format(ObjectQueue.remove_item()))

print("Size of the Queue is: {0}".format(ObjectQueue.return_size()))
