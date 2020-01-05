#python3
import sys

def optimal_summands(n):
    summands = [1,n-1]
    i = 1
    while summands[-1] > summands[-2]:
        summands[i] = i + 1
        summands[-1] = n - (i + 1)
        i += 1
        
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    print(input)
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
