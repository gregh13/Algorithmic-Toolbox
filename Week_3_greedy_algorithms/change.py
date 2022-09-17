# Fewest Coins Change Problem

# Goal: Design an algorithm that given an input 'm' returns the fewest number of coins (1, 5, 10) needed to make 'm'


def change(money):
    # Fast way
    coins = (money // 10) + ((money % 10) // 5) + (money % 5)
    return coins

    # Lengthy, naive and slow way
    # coins = 0
    # while money > 0:
    #     if money >= 10:
    #         money -= 10
    #         coins += 1
    #     elif money >= 5:
    #         money -= 5
    #         coins += 1
    #     elif money >= 1:
    #         money -= 1
    #         coins += 1
    # return coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
