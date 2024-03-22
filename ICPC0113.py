import math

def check(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                return False
        return True

for t in range(0,int(input())) :
    a = int(input())
    for i in range(12,int(a)+1):
        j = str(i)[::-1]
        if int(i) != int(j) and int(j) < int(a) and int(i) < int(j) and check(int(i)) and check(int(j)) :
            print(i, j, end = ' ')
    print() 