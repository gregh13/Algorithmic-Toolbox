# Knapsack Loot Max Value Problem

# Goal: Design an algorithm that given inputs of bag capacity, item weights, and item values, returns the optimal
#       amount of each item that should be taken to maximize the total value.
#       Note: Value is for total weight of item, however fractional amounts of items can be taken, with fractional value


from sys import stdin


def optimal_value(capacity, weights, values):
    # Optimized recursive method - calculates prices once, then uses second function recursively
    def prices_optimized(cap, w, v, p):
        val = 0.0
        if cap == 0 or not v:
            return val
        max_i = p.index(max(p))
        max_take = min(cap, w[max_i])
        cap -= max_take
        val += p[max_i] * max_take
        v.pop(max_i)
        w.pop(max_i)
        p.pop(max_i)
        return val + prices_optimized(cap, w, v, p)
    value = 0.0
    if capacity == 0 or not values:
        return value
    prices = []
    for i in range(len(weights)):
        prices.append(values[i] / weights[i])
    return value + prices_optimized(capacity, weights, values, prices)

    # # Simple recursive method - accurate, but recalculates 'prices' unnecessarily
    # value = 0.0
    # if capacity == 0 or not values:
    #     return value
    # prices = []
    # for i in range(len(weights)):
    #     prices.append(values[i] / weights[i])
    # max_i = prices.index(max(prices))
    # max_take = min(capacity, weights[max_i])
    # capacity -= max_take
    # value += prices[max_i] * max_take
    # values.pop(max_i)
    # weights.pop(max_i)
    # return value + optimal_value(capacity, weights, values)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print("Capacity: ", capacity)
    # print("Values: ", values)
    # print("Weights: ", weights)
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
