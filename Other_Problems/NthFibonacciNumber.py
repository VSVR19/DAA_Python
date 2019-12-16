class NthFibonaccciNumber:

    def __init__(self):
        pass

    @staticmethod
    def display_nth_fibonacci_number(target):
        number_one = 0
        number_two = 1

        for number in range(target):
            # print("Number one is: {0}.".format(number_one))
            # print("Number two is: {0}.".format(number_two))

            result = number_one + number_two
            number_two = number_one
            number_one = result

        print("Result is: {0}.".format(result))


ObjectNthFibonaccciNumber = NthFibonaccciNumber
ObjectNthFibonaccciNumber.display_nth_fibonacci_number(10)