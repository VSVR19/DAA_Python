"""
RUN THIS CODE IN JUPYTER NOTEBOOK; NOT IN PYCHARM.
"""


class Node:

    def __init__(self, value):
        # Provide a value for the current node.
        self.value = value
        # Temporarily assign the next node as None.
        self.nextnode = None

# This method checks for cycle  in the linked list.


def cycle_check(a):
    # SLOW MARKER- Assigned the value of start node- a.
    marker1 = a
    # FAST MARKER- Assigned the value of start node- a.
    marker2 = a

    # Perform checks with fast marker- both the fast marker and its next node musnt' be None.
    while marker1 is not None and marker2.nextnode is not None:
        # Marker 1 is assigned the nextnodes' value
        marker1 = marker1.nextnode
        # Marker 2 is assigned the nextnodes nextnodes' value.
        marker2 = marker2.nextnode.nextnode

        # If both markers' value are same, we can be sure of a cycle.
        if marker1 == marker2:
            print("Cycle Found!")
            # Return True and end.
            return True

    # The While Loop ends and marker1 was never equal to marker2- so no cycle found.
    print("No Cycles!!")
    # Return False and end.
    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""
from nose.tools import assert_equal

# CREATE CYCLE LINKED LIST.
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
# Cycle Here!
c.nextnode = a

# CREATE NON CYCLE LINKED LIST.
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


# The class containing calls to the Test Method.
class TestCycleCheck:

    def test(self, cycle_check):
        # A True check.
        assert_equal(cycle_check(a), True)
        # A False check.
        assert_equal(cycle_check(x), False)

        print("ALL TEST CASES PASSED.")


# Run Tests

# Object creation for the class.
t = TestCycleCheck()
# Call the test method using this object.
t.test(cycle_check)