#python3

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

n = int(input())

print(calc_fib(n))
