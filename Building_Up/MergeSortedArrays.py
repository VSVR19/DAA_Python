class MergeSortedArrays:

    def __init__(self):
        pass

    # @staticmethod
    # def merge_sorted_arrays(array_one, m, array_two, n):
    #     # array_one = array_one + array_two
    #     # print(array_one)
    #
    #     # indexer = 0
    #     # array_one_length = len(array_one)
    #     # print("Array one length: {0}.".format(array_one_length))
    #     # array_two_length = len(array_two)
    #     # print("Array two length: {0}.".format(array_two_length))
    #     #
    #     # while indexer < n:
    #     #     array_one[array_one_length - 1] = array_two[array_two_length - 1]
    #     #
    #     #     array_one_length -= 1
    #     #     array_two_length -= 1
    #     #     indexer += 1
    #     #
    #     # print("Array one is: {0}.".format(sorted(array_one)))
    #     # array_one_length = len(array_one)
    #     # array_one_mid = array_one_length // 2
    #     # print("Array one mid is: {0}.".format(array_one_mid))
    #     #
    #     # counter = 0
    #     # while counter < array_one_mid:
    #     #     temp_variable = array_one[counter]
    #     #     array_one[counter] = array_one[array_one_length - 1 - counter]
    #     #     array_one[array_one_length - 1 - counter] = temp_variable
    #     #
    #     #     counter += 1
    #     #
    #     # print("Array one is: {0}.".format(array_one))
    #     #
    #     # counter = 0
    #     # while counter < array_one_mid:
    #     #     temp_variable = array_one[counter]
    #     #     array_one[counter] = array_one[array_one_length - 1 - counter]
    #     #     array_one[array_one_length - 1 - counter] = temp_variable
    #     #
    #     #     counter += 1
    #     #
    #     # print("Array one is: {0}.".format(array_one))
    #     while m > 0 and n > 0:
    #         print("M is: {0}.".format(m))
    #         print("N is: {0}.".format(n))
    #
    #         if array_one[m - 1] >= array_two[n - 1]:
    #             print("In If.")
    #             array_one[m + n - 1] = array_one[m - 1]
    #             m -= 1
    #         else:
    #             print("In Else.")
    #             array_one[m + n - 1] = array_two[n - 1]
    #             n -= 1
    #
    #         print("Array one is: {0}.".format(array_one))
    #     if n > 0:
    #         array_one[:n] = array_two[:n]
    #
    #     print(array_one)

    @staticmethod
    def merge_sorted_arrays(array_one, m, array_two, n):
        array_one_length = len(array_one)
        array_two_length = len(array_two)

        while (array_one_length - 1) and (array_two_length - 1) >= 0:
            print(array_one_length)
            print(array_two[array_two_length - 1])
            array_two_length -= 1



ObjectMergeSortedArrays = MergeSortedArrays
ObjectMergeSortedArrays.merge_sorted_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# ObjectMergeSortedArrays.merge_sorted_arrays([2, 5, 6], 3, [1, 2, 3, 0, 0, 0], 3)
# ObjectMergeSortedArrays.merge_sorted_arrays([4, 5, 6], 3, [1, 2, 3, 0, 0, 0], 3)
# ObjectMergeSortedArrays.merge_sorted_arrays([1, 2, 3, 0], 3, [2], 1)
