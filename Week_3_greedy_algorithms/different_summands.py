# Maximum Number of Prizes (Different Summands) Problem

# Goal: Design an algorithm that given an input of a number 'n', returns a list of the smallest possible (in size and
#       number) summands (i.e. numbers that make a sum). Note that summands cannot repeat.
#       Ex: 7 --> 1, 2, 4     12 --> 1, 2, 3, 6


def optimal_summands(n):
    summands = []
    total = 0
    counter = 1
    while total != n:
        if total + counter <= n:
            total += counter
            summands.append(counter)
            counter += 1
        else:
            summands[-1] += n - total
            break
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
