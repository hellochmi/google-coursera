# Uses python3
import sys

def get_change(money):
    if money == 0:
        return 0
    min_num_coins = [0]
    coins = [4,3,1]
    for m in range(0,money+1):
        min_num_coins.insert(m,m)
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m-coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    #print("minnumcoins",min_num_coins)
    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
