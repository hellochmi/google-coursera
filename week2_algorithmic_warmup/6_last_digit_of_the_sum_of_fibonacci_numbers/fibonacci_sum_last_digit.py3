# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    sums = [0,1]
        if n<0: 
        return -1
    elif n<=len(a): 
        return a[n-1] 
    else: 
        temp = calc_fib(n-1) + calc_fib(n-2) 
        a.append(temp) 
        return temp

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sums(n))
