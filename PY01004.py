import math

def check(n) :
    if n<2:
        return False
    else :
        for i in range( 2 , int(math.sqrt(n)+1) ) :
            if n % i == 0 :
                return False
        return True

def uscln(a,b) :
    if b==0 :
        return a
    return uscln(b, a%b)
        
for t in range(int(input())) :
    n = int(input())
    cnt = int(0)
    for i in range(1,n) :
        if uscln(i,n) == 1 :
            cnt = cnt + 1
    #print(cnt)
    if check(cnt)==True : 
        print("YES")
    else :
        print("NO")
    