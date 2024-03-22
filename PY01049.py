import math

l = ['2','3','5','7']

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n)) + 1) :
            if n % i == 0 :
                return False
        return True
    
def check(n) :
    if nguyen_to(len(n)) == False :
        return False
    cnt = int(0)
    for i in n :
        if i in l :
            cnt += 1
    if cnt <= len(n) - cnt :
        return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")
    