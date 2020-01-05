# Uses python3
import sys
import math

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def mergeSortInv(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = mergeSortInv(a)
        b, bi = mergeSortInv(b)
        c = []
        i = 0
        j = 0
        swaps = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            swaps += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, swaps

#Merge(B,C) returns the resulting sorted array
# and the number of pairs  such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶, and 𝑏 > 𝑐;
def merge(arr, l, m, r):
    count = 0
    
    l = int(l)
    m = int(m)
    r = int(r)
    
    n1 = int(m - l + 1)
    n2 = int(r - m)
  
    # init arrays 
    L = [0] * n1
    R = [0] * n2

    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
        #print("m + 1 + j",m + 1 + j)
  
    # merge the temp arrays back into arr[l..r] 
    i = 0     # initial index of first subarray 
    j = 0     # initial index of second subarray 
    k = l     # initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
            count += (len(a)-i)
        k += 1
  
    # copy the remaining elements of L[], if there are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # copy the remaining elements of R[], if there are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
        
    return count, arr

# MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.
def mergeSort(arr,l,r): 
    count = 0
    if l < r: 
        count += 1
        m = math.floor((l+r)/2) # ==(l+r)/2 but avoids overflow for large l and h
        mergeSort(arr, l, m)[0] # sort left
        mergeSort(arr, m+1, r)[0] # sort right
        cnt, arr = merge(arr, l, m, r)[0] # merge arrays
        count += cnt
    return count, arr


if __name__ == '__main__':
    
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #arr, count = mergeSort(a, 0, len(a)-1)
    arr, count = mergeSortInv(a)
    print(count)
