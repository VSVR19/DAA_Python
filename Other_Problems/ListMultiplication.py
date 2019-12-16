# This class multiplies all elements in a python expect the 'self' number; i.e, the number at that particular iteration.
# This program has a TC of O(n) and SC of O(n).
# https://leetcode.com/problems/product-of-array-except-self/


class ListMultiplication:

    # Parameters are directly passed to the method itself.
    def __init__(self):
        # self.result_array = result_array
        # self.array = array
        pass

    # @staticmethod
    # def print_multiplication(array):
    #
    #     h = 0
    #     # print(array[1:])
    #     print(array[:h] + array[(h + 1):])
    #
    #     i = 1
    #     print(array[:i] + array[(i + 1):])
    #
    #     j = 2
    #     print(array[:j] + array[(j + 1):])
    #
    #     k = 3
    #     print(array[:k] + array[(k + 1):])

    # This is a static method as its uses no '.self' parameters.
    @staticmethod
    def productExceptSelf(input_list):
        # Get the length of the input list.
        number_list_length = len(input_list)

        # Construct left and right arrays having the same size as that of the input list with all the elements being '1'.
        left_array = [1] * number_list_length
        right_array = [1] * number_list_length

        # Construct the left array.
        # Its length - 1 as we ignore the last element in the input list.

        # Loop through 'n' elements of the left array.
        # Therefore, we have a TC of O(n) here.
        # Also, by creating a new array, the SC in O(n) as well.
        for number in range(len(input_list) - 1):
            # left_array[number + 1] as we intend the first element in the left_array to be '1'.
            left_array[number + 1] = input_list[number] * left_array[number]
        print("Left array is: {0}.".format(left_array))

        # Construct the right array.
        number = len(input_list)
        # The limit is greater than 2 as we 'reverse' fill the right array by always being 2 steps ahead of the input list.
        # Therefore, if not stopped at 2, we might end up re-populating the array list.

        # Loop through 'n' elements of the right array.
        # Therefore, we have a TC of O(n) here.
        # Also, by creating a new array, the SC in O(n) as well.
        while number >= 2:
            # print("Number is: {0}.".format(number))
            right_array[number - 2] = input_list[number - 1] * right_array[number - 1]
            # print("Multiplying: {0} and {1}. Answer: {2}.".format(input_list[number - 1], right_array[number - 1],
            #                                                       right_array[number - 2]))
            # print("*************Right array is: {0}.*************".format(right_array))
            number -= 1
        print("Right array is: {0}.".format(right_array))

        # Multiply left and right arrays to get the resultant array.

        # Once again, we creatin    g a new array of the same size of the input array.
        # This loop has a TC and SC of O(n).
        result_array = []
        for number in range(len(left_array)):
            result_array.append(left_array[number] * right_array[number])
        print("Result array is: {0}.".format(result_array))


ObjectListMultiplication = ListMultiplication()
# ObjectListMultiplication.print_multiplication_result()
# print(ObjectListMultiplication.jose_print_multiplication_result())
# ObjectListMultiplication.multiply_everything_but_self([4, 5, 1, 8, 2])
ObjectListMultiplication.productExceptSelf([5, 5, 0, 5])
