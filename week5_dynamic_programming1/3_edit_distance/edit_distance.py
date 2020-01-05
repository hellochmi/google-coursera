# Uses python3
"""
def d(i,j,A,B):
    if d(i,j-1,s,t)+1
"""

# A Dynamic Programming based Python program for edit 
# distance problem 
def edit_distance(s, t): 
    m = len(s)
    n = len(t)
    # Create a table to store results of subproblems 
    a = [[0 for x in range(n+1)] for x in range(m+1)] 

    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                a[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                a[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif s[i-1] == t[j-1]: 
                a[i][j] = a[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                a[i][j] = 1 + min(a[i][j-1],        # Insert 
                                  a[i-1][j],        # Remove 
                                  a[i-1][j-1])    # Replace 
  
    return a[m][n] 

"""
def edit_distances(s, t):
    #write your code here
    
    #A = list(s)
    #B = list(t)
    
    #A = [d(i,0,A,B) for i in range(0,len(s))]
    #B = [d(0,j,A,B) for j in range(0,len(t))]
    s = ' ' + s
    t = ' ' + t
    
    m = 999999
    d = 0
    
    for j in range(1,len(s)):
        for i in range(1,len(t)):
            if s[i] == t[j-1]:
                insertion = abs(i - j - 1) + 1
            insertion = d(i,j-1,s,t)+1
            deletion = d(i-1,j,s,t)+1
            match = d(i-1,j-1,s,t)
            mismatch = d(i-1,j-1,s,t)+1
            if s[i] == t[j]:
                d = min(insertion,deletion,match)
            else:
                d = min(insertion,deletion,mismatch)
            if d < m:
                m = d
    return m
"""



if __name__ == "__main__":
    print(edit_distance(input(), input()))
