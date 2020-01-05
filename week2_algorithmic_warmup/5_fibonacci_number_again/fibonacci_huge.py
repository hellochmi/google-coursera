#python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n<0: 
        return -1
    elif n<=len(a): 
        return a[n-1] 
    else: 
        temp = get_remainder(n,m)
        a.append(temp) 
        return temp

def get_fibonacci_huge(n,m): 
    # initialize series array
    series = [0,1]
    # initialize pisano period to 0
    pisano_period = 0
    # find length of pisano period
    while True:
        # get last digit of current number sum and add to series
        series.append((series[-1] + series[-2]) % 10)
        # repeating [0,1] indicates the beginning of the next pisano period
        if series[-2:] == [0,1]:
            # return the length of the series - the repeating [0,1]
            pisano_period = len(series) - 2
            break
    # find remainder of n % pisano period
    return (n % pisano_period) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    a = [0,1]
    print(get_fibonacci_huge(n, m))
