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
    sum = int(0)
    for i in n :
        sum += int(i)
    if nguyen_to(sum) :
        print("YES")
    else :
        print("NO")