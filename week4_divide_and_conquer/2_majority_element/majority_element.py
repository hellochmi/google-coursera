# Uses python3
import sys
import math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def get_majority(a,n):
    #return any((a.count(i)>math.floor(n/2)) for i in a)
    #a = []
    #for i in range(0,len(n)):
    for i in a:
        if a.count(i) > math.floor(n/2):
            return True
    return False
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority(a, n):
        print(1)
    else:
        print(0)
