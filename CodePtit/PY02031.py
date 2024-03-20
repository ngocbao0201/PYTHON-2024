import math

def nguyen_to(n):
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
n,m = [int(i) for i in input().split()]
for i in range(0,n) :
    l = list(map(int,input().split()))
    for j in l :
        if nguyen_to(j):
            print(1,end = ' ')
        else :
            print(0,end=' ')
    print()
            