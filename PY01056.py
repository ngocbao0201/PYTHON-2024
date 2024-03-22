import math

c = ['0','2','4','6','8']
l = ['1','3','5','7','9']

def nguyen_to(n) :
    if int(n) < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if int(n) % i == 0 :
                return False
        return True
    
def check(n) :
    for i in range(0,len(n)) :
        if i % 2 == 0 :
            if n[i] not in c : return False
        else :
            if n[i] not in l : return False
    sum = int(0)
    for i in n :
        sum += int(i)
    if nguyen_to(sum) == False :
        return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")
            