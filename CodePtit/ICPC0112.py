import math

def check(n):
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                return False
        return True

for t in range(0,int(input())) :
    n = int(input())
    cnt = int(0)
    for i in range(2,int(n-6)) :
        if check(int(i))  and check(int(i+6)) :
            if check(int(i+2)) or check(int(i+4)) :
                cnt = cnt + 1 
    print(cnt)
            