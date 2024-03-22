import math

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0 :
                return False
    return True

def hamming(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0 :
            if i > 5 : 
                return False
            else :
                while n % i == 0 :
                    n = int(n) / i
    return True

for t in range(int(input())) :
    n = int(input())
    if hamming(n) :
        print("yes")
    else :
        print("no")
                