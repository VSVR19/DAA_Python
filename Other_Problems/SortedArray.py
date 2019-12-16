# This program has a TC of O(n).
# This program has a SC of O(n).
class SortedArray:

    def __init__(self):
        pass

    @staticmethod
    def check_array_sorted(first_array):
        # Get the length of the input array.
        # Constant time operation.
        first_array_length = len(first_array)

        # Create a second array having the same length of the input array.
        # Constant time operation.
        # This array will occupy 'n' spaces; where n is the number of elements in the input list.
        # So we have a SC of O(n).
        second_array = [0] * first_array_length

        # Define and initialize two counter variables.
        # Constant time operation.
        # Constant space operation.
        odd_counter_one = 1
        odd_counter_two = 1

        # Start looping through the input array.
        # We will loop through 'n' elements of the input array; so the TC is O(n).
        for number in range(len(first_array)):
            # print("Number is: {0}.".format(number))

            # The first element of the input array becomes the first element of the output array
            # Constant time operation.
            if number == 0:
                # Constant time operation.
                second_array[0] = first_array[0]

            # If number is divisible by two,
            # Divide the number by 2. (get its quotient)
            # The number is used to index the output array and quotient, the input array.
            # Constant time operation.
            elif number % 2 == 0:

                # Constant time operation.
                second_array[number] = first_array[int(number / 2)]
            # If number is not divisible by two,
            # Reduce the number by a factor of one for each iteration to access the input array.
            # Increase odd_counter_two by a factor of two for each iteration to access the output array.

            # Constant time operation.
            elif number % 2 != 0:

                # Constant time operation.
                second_array[odd_counter_two] = first_array[first_array_length - odd_counter_one]
                odd_counter_one += 1
                odd_counter_two += 2

            print("Second array is: {0}.".format(second_array))

        # Check if the output array is sorted in ascending order.
        # We will loop through 'n' elements of the output array; so the TC is O(n).
        flag = True
        for number in range(len(second_array) - 1):
            # If the current number is greater than the next number,
            # The output array is not sorted in ascending order.
            # Constant time operation.
            if second_array[number] > second_array[number + 1]:
                flag = False
                break

        if flag:
            print("This array is sorted in ascending order.")
        else:
            print("This array is sorted in descending order.")


ObjectSortedArray = SortedArray
ObjectSortedArray.check_array_sorted([1, 3, 5, 6, 4, 2])
