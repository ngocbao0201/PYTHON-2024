import math

list = [2,3,5,7]

def check(n) :
    if int(n) < 2:
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if int(n) % i == 0 :
                return False
        return True

for t in range(0,int(input())) :
    n = input()
    m = n[::-1]
    sum = int(0)
    ok = 1
    for i in n :
        sum = sum + int(i)
        if int(i) not in list :
            ok = 0
    #print(n, m, sum, ok)
    if ok == 0 :
        print("No")
    else :
        if check(int(n)) and check(int(m)) and check(sum) :
            print("Yes")
        else :
            print("No")