# Inspiration- https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks
class Queue2Stacks(object):

    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # Add elements to Stack 1 having element as the range.
        for i in range(element):
            self.stack1.append(i)

        print("Stack 1: {0}".format(self.stack1))

        # Check length of stack 2.
        if len(self.stack2) == 0:
            # While we have elements in Stack 1,
            while self.stack1:
                # Pop- append those elements to stack 2.
                # So Stack 2 has the element in reverse order when compared to Stack 1.
                # Eg- Stack 1- 0 1 2 3 4
                # Stack 2 (after popped)- 4 3 2 1 0
                self.stack2.append(self.stack1.pop())

        print("Stack 2: {0}".format(self.stack2))

    # A method to pop- print elements from Stack 2.
    def dequeue(self):
        # While we have elements in Stack 2.
        while self.stack2:
            # Pop- print the elements from Stack 2.
            # Eg- 4 3 2 1 0- pop- printed becomes 0 1 2 3 4.
            # Thus when we pop, we get the original order when we inserted elements
            # In Stack 1.
            print(self.stack2.pop())

        print("Stack 2.0: {0}".format(self.stack2))


ObjectQueue2Stacks = Queue2Stacks()

ObjectQueue2Stacks.enqueue(5)
ObjectQueue2Stacks.dequeue()
