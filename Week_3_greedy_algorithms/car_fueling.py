# Car Gas Refill Minimization Problem

# Goal: Design an algorithm that given inputs of distance needed to travel, miles per full tank, and a list of stops
#       returns the least number of stops needed to get to the destination.
#       Note: if it is not possible to reach the destination (too few/spaced out stops), returns -1

from sys import stdin


def min_refills(distance, tank, stops):
    # My way
    refills = 0
    location = 0
    # Add destination to stops, helps to check about the last stop
    stops.append(distance)
    for i in range(len(stops)):
        # Checks for any impossible situations where distance is too large.
        # First iteration of stops[0] - stops[-1] isn't problematic as it will be a negative number and thus < tank
        if stops[i] - stops[i-1] > tank:
            return -1
        if (location + tank) < stops[i]:
            location = stops[i-1]
            refills += 1
    return refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    # d, m, _, *stops = map(int, input().split())
    print(min_refills(d, m, stops))
