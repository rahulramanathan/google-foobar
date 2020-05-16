dp = [[-1 for i in range(202)] for j in range(202)]

def dp_helper(h, rem):
    x = dp[h][rem]
    if x != -1:
        return x

    if rem == 0:
        return 1
    if rem < h:
        return 0
    
    x = dp_helper(h+1, rem-h) + dp_helper(h+1, rem)
    dp[h][rem] = x
    return x

def solution(n):
    return dp_helper(1,n)-1

print solution(200)