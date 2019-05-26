class ContinuousSum:

    # Just 'pass' as args. are passed to the method and not to the class.
    def __init__(self):
        pass

    # Making this method 'static' as it doesnt use any self. parameters.
    @staticmethod
    def find_continuous_sum(continuous_list):
        # Initializing the required variables.
        answer = 0
        old_sum = 0
        continuous_sum = 0

        # A loop through the length of the array.
        for i in range(len(continuous_list)):
            # Adding up variables one by one- not in pairs.
            answer = answer + continuous_list[i]

            # If new sum is less than old sum.
            if answer < old_sum:
                # The previous sum is the largest sum.
                continuous_sum = old_sum
                # Don't use the sum reduced by negative numbers.
                old_sum = continuous_sum
            else:
                # Positive number case
                old_sum = answer

        return continuous_sum


print("A redundant print for May 15 branch.")
print("Oops!")
print("Lets see")
print("Lets see again!")

objectContinuousSum = ContinuousSum
print(objectContinuousSum.find_continuous_sum([1, 2, -1,3, 4, -1]))  # Output 9.
print(objectContinuousSum.find_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))  # Output 29.
print(objectContinuousSum.find_continuous_sum([-1, 1]))  # Sum is to add two things; so, Out- 1.
