#python3

import sys
import math

def largest_number(a):
    
    ans = ''
    max_digit = -99999999
    
    #while a:
    #    for number in a:
    #        if greater_than_or_equal_to(number,max_digit,ans):
    #            max_digit = number
    #    ans += str(max_digit)
    #    a.pop(a.index(max_digit))
        
    for number in a:
        if int(ans + number) >= int(number + ans):
            ans += number
        else:
            ans = number + ans
        
    return int(ans)

def greater_than_or_equal_to(n,m,ans):
    if int(ans + str(n)) >= int(ans + str(m)):
        return True
    else:
        return False
        
        
    
    #b = sorted([i for i in a if len(str(i))>1],reverse=True)
    #c = sorted([i for i in a if len(str(i))==1],reverse=True)
    
    #for number in c:
    #    for number_ in b:
    #        if str(number_).startswith(str(number)):
    #            b.insert(b.index(number_),number)
                
        
    #for i in range(9,-1,-1):
    #    for number in b:
    #        if i in a:
    #            n += str(i)
    #        if str(number).startswith(str(i)):
    #            n += str(number)
   
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
