def gcd(m,n):
    if m < n:
        (m, n) = (n, m)
    if(m % n) == 0:
        return n
    else:
        return (gcd(n, m % n)) # recursion taking place

def gcdExtended(a, b): 
    # Base Case 
    if a == 0 :  
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y

print(gcd(66528, 52920))
print(gcdExtended(26513, 32321))
