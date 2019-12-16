import sys

# This program has a TC of O(n) and SC of O(1).
class MaximumProfit:

    def __init__(self):
        pass

    # @staticmethod
    # def calculate_max_profit(stock_prices):
    #     stock_profit = 0
    #
    #     if len(stock_prices) > 0:
    #         lowest_price = min(stock_prices)
    #
    #         prices_after_lowest = stock_prices[(stock_prices.index(lowest_price) + 1):]
    #         # print("Prices after lowest List is: {0}.".format(prices_after_lowest))
    #
    #         if len(prices_after_lowest) > 0:
    #             stock_profit = max(prices_after_lowest) - lowest_price
    #
    #     print("Stock profit is: {0}.".format(stock_profit))
        # print(lowest_price, max(prices_after_lowest))

    # @staticmethod
    # def calculate_max_profit(stock_prices):
    #     profits_list = []
    #     while len(stock_prices) > 0:
    #         lowest_price = min(stock_prices)
    #         print("Lowest price is: {0}.".format(lowest_price))
    #
    #         prices_after_lowest = stock_prices[(stock_prices.index(lowest_price)+ 1):]
    #         print("Prices after lowest: {0}.".format(prices_after_lowest))
    #
    #         if len(prices_after_lowest) > 0:
    #             stock_profit = max(prices_after_lowest) - lowest_price
    #             print("Stock profit is: {0}.".format(stock_profit))
    #
    #             profits_list.append(stock_profit)
    #             print("Profit list is: {0}.".format(profits_list))
    #
    #         stock_prices.remove(lowest_price)
    #         print("Input Array is: {0}.".format(stock_prices))
    #
    #     if len(profits_list) > 0:
    #         maximum_profit = max(profits_list)
    #     else:
    #         maximum_profit = 0
    #
    #     print("Maximum profit is: {0}.".format(maximum_profit))
        # return maximum_profit

    @staticmethod
    def calculate_max_profit(stock_prices):
        # Set the minimum price to a very very big variable like 123456789.
        # By doing so, all the the very first variable will get assigned to this minimum variable.
        # Just a way to detect the smallest variable in a array.

        # Both these assignments have a TC of O(1).
        # SC is O(1) as well as the above two variables always require one unit of space.

        min_price = sys.maxsize
        # Set the maximum profit to zero.
        # Since profits always start at one, this will also get overridden at the very first calculation of profit.
        max_profit = 0

        # Loop through the input array.

        # We loop through 'n' elements; therefore, TC is O(n).
        for number in range(len(stock_prices)):
            # Check if the current array element is less than minimum price.

            # This equality check is always O(1).
            if stock_prices[number] < min_price:
                # If yes, set the current array element as the minimum variable.

                # This assignment always requires a constant space, therefore, its SC is O(1).
                min_price = stock_prices[number]

            # If the current array element is greater than minimum price,
            # Calculate profit.
            # Profit = Current array element - Minimum price.

            # This equality check is always O(1).
            elif stock_prices[number] - min_price > max_profit:
                # If the above calculated profit is higher than the previously calculated profit,
                # Set this newly calculated profit as the max_profit.

                # This assignment always requires a constant space, therefore, its SC is O(1).
                max_profit = stock_prices[number] - min_price

        # Print the maximum profit at the end.
        print("Max profit is: {0}.".format(max_profit))
        # return max_profit


ObjectMaximumProfit = MaximumProfit()
ObjectMaximumProfit.calculate_max_profit([12,11,15,20,10])
# ObjectMaximumProfit.calculate_max_profit([12,11,15,3,10])
# ObjectMaximumProfit.calculate_max_profit([7,1,5,3,6,4])
# ObjectMaximumProfit.calculate_max_profit([7,6,4,3,1])
# ObjectMaximumProfit.calculate_max_profit([2, 4, 1])
# ObjectMaximumProfit.calculate_max_profit([7, 6, 4, 3, 1])
# ObjectMaximumProfit.calculate_max_profit([0, 6, -3, 7])
