import math

def check(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                return False
        return True
    
for t in range(int(input())) :
    n = int(input())
    if check(n%10000) :
        print("YES")
    else :
        print("NO")