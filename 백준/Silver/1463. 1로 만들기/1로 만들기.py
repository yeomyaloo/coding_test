import sys
sys.setrecursionlimit(10**6)
def dp(n):
    if n == 2 or n == 3:
        memo[n] = 1
        return memo[n]
    elif n == 1:
        memo[n] = 0
        return memo[n]
    if n not in memo:
        if n % 6 == 0:
            memo[n] = 1+min(dp(n//3),dp(n//2))
            
        elif n%3 == 0:
            memo[n] = 1+min(dp(n//3), dp(n-1))
            
        elif n%2 == 0:
            memo[n] = 1+min(dp(n//2), dp(n-1))
        else:
            memo[n] = dp(n-1)+1
    return memo[n]
        

    
memo = {}
n = int(input())
print(dp(n))

