def isprime(n):
    if n!=2 and n % 2 == 0:
        return False
    return all(n%j for j in range(3, int(n**0.5) + 1, 2))
    
lambdastring = ""

def solution(i):
    # Your code here
    lambdastring = ""
    
    for k in range(2,21000,1):
        if len(lambdastring) < 10005:
            if isprime(k):
                lambdastring = lambdastring + str(k)
        else:
            break
    
    return lambdastring[i:i+5]

print solution(1)