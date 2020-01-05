# Uses python3
import sys
import math

def binary_search(a, x, low, high):
    # if x not in a:     O(n) runtime
    #    return -1
    if high < low:
        return -1
    mid = math.floor(low + ((high - low)/2))
    try:
        a[mid]
    except:
        return -1
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary_search(a, x, low, mid-1)
    else:
        return binary_search(a, x, mid+1, high)

#def linear_search(a, x):
    #if 
    #if x in a:
    #    return a.index(x)
    #else:
    #    return -1
    #indices = []
    #for number in x:
    #    if number in a:
    #        indices.append(a.index(number),end=' ')
    #    else:
    #        indices.append(-1)
    #return indices

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    a.sort()
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)), end = ' ')
