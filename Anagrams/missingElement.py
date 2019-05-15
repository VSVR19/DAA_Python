# N.B- This code is for only for 'one' missing element.
class MissingElement:

    # Just 'pass' as args. are passed to the method and not to the class.
    def __init__(self):
        pass

    def find_element(array_one, array_two):
        # Finding the sum of two arrays.
        sum_array_one = sum(array_one)
        sum_array_two = sum(array_two)

        # The absolute difference between the sums is the missing number.
        missing_element = abs(sum_array_one - sum_array_two)
        return missing_element


objectMissingElement = MissingElement
#print("******************TC01******************")  # Output 5- Passes
print(objectMissingElement.find_element([5, 5, 7, 7],[5, 7, 7]))
#print("******************TC02******************")  # Output 5- Passes
print(objectMissingElement.find_element([1, 2, 3, 4, 5, 6, 7],[3, 7, 2, 1, 4, 6]))
#print("******************TC03******************")  # Output 6- Passes
print(objectMissingElement.find_element([9,8,7,6,5,4,3,2,1],[9, 8, 7, 5, 4, 3, 2, 1]))
