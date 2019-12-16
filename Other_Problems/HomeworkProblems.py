# This program is my first formal understanding of Recursion. (even if a little bit)
class HomeworkProblems:

    # As usual, a empty constructor is used as parameters are directly passed to the individual methods themselves.
    def __init__(self):
        pass

    # This method calculates the factorial of a given number.
    @staticmethod
    def try_factorial_example(number):
        # Base case.
        if number == 0:
            # As 0! = 1.
            return 1
        else:
            # This is interesting.
            # 'Number' holds the input parameter.
            # And the part after * calls the function until the base case is reached- this is Recursion.
            # A function calling itself.
            # Once the base case is reached, the results of each function call is added to the number,
            # In a reverse waterfall style.
            return number * ObjectHomeworkProblems.try_factorial_example(number - 1)

    # This method calculates the cumulative sum till o of a given number.
    @staticmethod
    def calculate_cumulative_sum(number):
        # Base case.
        if number == 0:
            # As we calculate cumulative sum till we reach zero.
            return 0
        else:
            # As above; store the result of each function call,
            # Once Base Case is reached, add the result of each function call with the number,
            # Repeat this in a reverse waterfall style.
            return number + ObjectHomeworkProblems.calculate_cumulative_sum(number - 1)

    # This method calculates the sum of digits of a number.
    @staticmethod
    def calculate_sum_of_digits(number):
        # This converts the number to int as division converts it to a float.
        number = int(number)
        # Base case.
        if number < 10:
            # Any number which is less than 10, when divided(/) by 10, will return the number itself as the result.
            # Since that is a single digit number, there is no need to break it down any further.
            # It can be added to the existing sum of digits without any further ado.
            return number
        else:
            # Same as above.
            # Extract the individual digits of a number by using modulo.
            # At the same time, to extract the subsequent digits, reduce the number by dividing it by 10.
            # Store the result of each function call,
            # Once base case is reached, add the result of the last function call with the number,
            # And carry it upwards to the previous function call, and add it to the number generated at that time.
            return (number % 10) + ObjectHomeworkProblems.calculate_sum_of_digits(number / 10)


ObjectHomeworkProblems = HomeworkProblems
print(ObjectHomeworkProblems.try_factorial_example(5))
print(ObjectHomeworkProblems.calculate_cumulative_sum(4))
print(ObjectHomeworkProblems.calculate_sum_of_digits(619))
# print(ObjectHomeworkProblems.print_word_splits('themanran'))
