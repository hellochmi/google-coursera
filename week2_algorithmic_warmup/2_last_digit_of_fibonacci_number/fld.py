#python3
import sys

a = [0,1]

def calc_fib(n): 
    if n<0: 
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < len(a):
        return a[n]
    else: 
        temp = calc_fib(n-1) + calc_fib(n-2) 
        a.append(temp) 
        return temp

last_digits = [calc_fib(i)%10 for i in range(0,60)]

def get_fibonacci_last_digit_naive(n):
    return last_digits[n%60]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
