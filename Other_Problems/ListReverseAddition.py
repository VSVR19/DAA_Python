# This program does many things.
# 1. Takes in 2 strings as input.
# 2. Converts them to integers.
# 3. Adds the two lists from reverse.
# 4. Appends these results to a new list.

# We have a TC and SC of O(n).
class ListReverseAddition:

    # Parameters are directly passed to the method itself.
    def __init__(self):
        pass

    # This is a static method as its uses no '.self' parameters.
    @staticmethod
    def display_reverse_added_lists(number_one, number_two):
        # Two empty lists to hold number_one and number_two once theyre' converted to numeric lists.
        array_one = []
        array_two = []

        # Convert both the input strings to int to their extract digits.
        # We read all the digits and convert it to a int.
        # There, a TC of O(n).
        # Also, as we just replicate the input, this has a SC of O(n) as well.
        number_one = int(number_one)
        number_two = int(number_two)

        # Work till the number is greater than zero.
        # This is greater than zero to include the very first digit as well.
        # If it was greater than 1, 12 / 10 equals 1 and this first digit will get ignored.

        # Looping through the entire number- TC of O(n).
        while number_one > 0:
            # print("Number One is: {0}".format(number_one))
            # Extract the last digit of the number using modulo by 10 operation.
            remainder = number_one % 10
            # print("**********Remainder is: {0}**********".format(remainder))
            # Append the remainder to the numeric list.
            array_one.append(remainder)
            # Continue the loop; each time, this division will cut of the last number.
            number_one = int(number_one / 10)

        # A new array is constructed equal to the size of the input string.
        # Therefore, a SC of O(n).
        print("Array One is: {0}.".format(array_one))

        # The above While loop is replicated with the second input string.
        while number_two > 0:
            remainder = number_two % 10
            array_two.append(remainder)
            number_two = int(number_two / 10)

        # A new array is constructed equal to the size of the input string.
        # Therefore, a SC of O(n).
        print("Array Two is: {0}.".format(array_two))

        # Get the length of both the input arrays.
        # The smaller array will be inserted with zeros till its length is equal to the larger array.
        array_one_length = len(array_one)
        array_two_length = len(array_two)

        # print("Array 1 length is: {0}.".format(array_one_length))
        # print("Array 2 length is: {0}.".format(array_two_length))

        # The smaller array will be inserted with zeros till its length is equal to the larger array.
        # This, if the array one is smaller.
        if array_one_length < array_two_length:
            length_difference = abs(array_one_length - array_two_length)
            # print("Length difference is: {0}.".format(length_difference))

            for number in range(length_difference):
                array_one.insert(0, 0)
            # print("Array 1 after modification: {0}.".format(array_one))

        # This, if the array two is smaller.
        elif array_two_length < array_one_length:
            length_difference = abs(array_one_length - array_two_length)
            # print("Length difference is: {0}.".format(length_difference))

            for number in range(length_difference):
                array_two.insert(0, 0)
            # print("Array 2 after modification: {0}.".format(array_two))

        # Number is reduced by one as there is a difference of 1 between length and actual indexing.
        number = len(array_one) - 1
        result_list = []
        # Reverse add both the lists.
        while number > -1:
            answer = array_one[number] + array_two[number]
            # Since output must be a string, convert the sum to a string and append it to the result list.
            result_list.append(str(answer))
            # This decrement is to control the loop.
            number -= 1

        # This list has a SC of O(n) + O(n) = O(2n).
        # Ignoring the 2, we have a SC of O(n).
        print("The result list is: {0}.".format("".join(result_list)))
        # Convert the result list to a string and print it.


ObjectListReverseAddition = ListReverseAddition()
ObjectListReverseAddition.display_reverse_added_lists(12345, 678910)
# ObjectListReverseAddition.display_reverse_added_lists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
# ObjectListReverseAddition.display_reverse_added_lists([1, 2, 3], [6, 7, 8, 9, 10])
# ObjectListReverseAddition.display_reverse_added_lists([1, 2, 3, 4, 5], [6, 7, 8])
# ObjectListReverseAddition.display_reverse_added_lists([1, 2, 3, 4, 5], [6])
