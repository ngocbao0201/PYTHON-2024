import math

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 : 
                return False
        return True
    
for t in range(int(input())) :
    n = input()
    if nguyen_to(int(n[0:3])) and nguyen_to(int(n[-3:])) :
        print("YES")
    else :
        print("NO")