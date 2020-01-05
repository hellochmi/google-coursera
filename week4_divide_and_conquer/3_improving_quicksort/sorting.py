# Uses python3
import sys
import random

#quicksort

"""
def partition3(a, l, r):
    #write your code here
    # all the elements to the right < x, all the elements to the left > x
    
    # x is the pivot
    mid = a[l]
    i = 0
    j = 0
    k = r
    
    while j < k:
        if a[j] < mid:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[i] > mid:
            k -= 1
            a[k], a[j] = a[j], a[k]
        else:
            j += 1
    return j
"""

def partition3(a, l, r):
    x, j, k = a[l], l, r
    i = j
    
    while i <= k:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
        elif a[i] > x:
            a[k], a[i] = a[i], a[k]
            k -= 1
            i -= 1 # remain in the same i in this case
        i += 1   
    return j, k

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
