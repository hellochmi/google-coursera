#Uses python3

import sys

def lcs2(a, b): 
    m = len(a) 
    n = len(b) 
  
    # declaring array for storing the dp values 
    # dp = [[None]*(n + 1) for i in xrange(m + 1)] 
    dp = [[0]*(n + 1) for i in range(0,m + 1)] 
    
    """Build L[m + 1][n + 1] in bottom up fashion 
    L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]"""
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                dp[i][j] = 0
            elif a[i-1] == b[j-1]: 
                dp[i][j] = dp[i-1][j-1]+1
            else: 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
  
    # dp[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return dp[m][n] 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
