def toStr_base_b(n,b):
    res = ""
    while n:
        res+=str(n%b)
        n/=b
    return res[::-1]

def solution(n,b):
    # Your code here
    a = str(n)
    k = len(a)
    generated_number = [a]    
    while True:
        y = ''.join(sorted(a))
        x = y[::-1]            
        z = toStr_base_b(int(x,b) - int(y,b),b)
        z = "0"*(k-len(z)) + z    
        if z in generated_number:            
            break
        generated_number.append(z)
        a = z
    
    return len(generated_number) - generated_number.index(z)

# print solution(210022,3)
# print solution(1211, 10)