class CoinChange:

    def __init__(self):
        pass

    @staticmethod
    def calculate_coin_change(amount, coins_list):
        result = 0
        coins_list_length = len(coins_list)
        counter = 1
        while result <= amount:

            if counter <= coins_list_length:
                result = result + coins_list[counter]

        print(result)


ObjectCoinChange = CoinChange
ObjectCoinChange.calculate_coin_change(10, [1, 5, 10])