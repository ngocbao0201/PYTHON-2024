import math

def uscln(a,b) :
    if b==0 :
        return a
    return uscln(b,a%b)

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                return False
        return True
    
for t in range( int(input()) ) :
    a,b = [int(i) for i in input().split()]
    x = int(uscln(a,b))
    #print(x)
    y = int(0)
    for i in str(x) :
        y = y + int(i)
    #print(y)
    if nguyen_to(y) == True :
        print("YES")
    else :
        print("NO")