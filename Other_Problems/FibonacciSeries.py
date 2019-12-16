class FibonacciSeries:

    def __init__(self, term, count, result):
        self.term = term
        self.count = count
        self.result = result
        self.counter = 0
        self.cache = [None] * (self.term + 1)

    def calculate_iterative_fibonacci_number(self, number_one, number_two):
        count = 1
        while count <= self.term:
            self.result = number_one + number_two
            number_one = number_two
            number_two = self.result
            count += 1
            print(self.result)

        print("The {0}th Fibonacci number is: {1}.".format(self.term, self.result))

    def calculate_recursive_fibonacci_number(self, term_one, term_two):
        if self.counter == self.term:
            return self.result
        else:
            self.result = term_one + term_two
            self.counter += 1
            return FibonacciSeries.calculate_recursive_fibonacci_number(self, term_two, self.result)

    @staticmethod
    def jose_recursion(n):
        if n == 0 or n == 1:
            return n
        else:
            print(ObjectFibonacciSeries.jose_recursion(n - 1) + ObjectFibonacciSeries.jose_recursion(n - 2))
            return ObjectFibonacciSeries.jose_recursion(n - 1) + ObjectFibonacciSeries.jose_recursion(n - 2)

    # def calculate_fibonacci_number_dynamically(self, n):
    #     # Base case:
    #     if n == 0 or n == 1:
    #         return n
    #     # Check cache.
    #     if self.cache[n] is not None:
    #         return self.cache[n]
    #     else:
    #         self.cache[n] = ObjectFibonacciSeries.calculate_fibonacci_number_dynamically(n - 1) + ObjectFibonacciSeries.calculate_fibonacci_number_dynamically(n - 2)
    #         return self.cache[n]


ObjectFibonacciSeries = FibonacciSeries(10, 0, 0)
# print("The required Fibonacci number is: {0}.".format(ObjectFibonacciSeries.calculate_recursive_fibonacci_number(0, 1)))
ObjectFibonacciSeries.calculate_iterative_fibonacci_number(0, 1)
# print("Result is: {0}.".format(ObjectFibonacciSeries.jose_recursion(5)))
# print("Result is: {0}.".format(ObjectFibonacciSeries.calculate_fibonacci_number_dynamically(10)))
