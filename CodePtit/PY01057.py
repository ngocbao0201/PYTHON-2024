import math

l = [2,3,5,7]

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 : 
                return False
        return True
    
def check(n) :
    for i in range(0,len(n)):
        if int(n[i]) in l :
            if nguyen_to(i) == False :
                return False
        else :
            if nguyen_to(i) :
                return False
    return True
    
for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")