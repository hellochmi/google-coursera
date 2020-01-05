#python3
import sys

def get_change(m):
    #write your code here
    coins = 0
    while m > 9:
        coins += 1
        m = m - 10
    while m > 4:
        coins += 1
        m = m - 5
    return coins + m
        

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
