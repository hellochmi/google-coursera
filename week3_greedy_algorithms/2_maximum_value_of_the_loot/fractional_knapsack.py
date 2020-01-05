#python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    weight = 0.
    loot = sorted([[value/weight,weight] for weight,value in zip(weights,values)],reverse=True)
    while weight <= capacity:
        if not loot:
            return value
        if loot[0][1] < capacity - weight:
            value += loot[0][0] * loot[0][1]
            weight += loot[0][1]
            loot.pop(0)
        else:
            remaining = capacity - weight
            value += loot[0][0] * remaining
            weight += loot[0][1]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
