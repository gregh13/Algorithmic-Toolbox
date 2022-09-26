def change(money):
    # Problem stated coin denominations are 1, 3, and 4 cent coins
    coin_denoms = [1, 3, 4]

    # Initialize num_coins to positive infinity
    num_coins = float("inf")

    # Initialize dict for storing coin numbers
    min_num_coins = {0: 0}

    for m in range(1, money + 1):
        # Set number of coins for current money value to positive infinity
        min_num_coins[m] = float("inf")

        # Iterate through all possible coin denominations
        for coin_i in coin_denoms:

            # Check if able to add a coin without going over the money value
            if m >= coin_i:
                num_coins = min_num_coins[m - coin_i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
