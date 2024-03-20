import math

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0 :
                return False
        return True
    
n = int(input())
l = list(map(int,input().split()))
l2 =[]
for i in l:
    if nguyen_to(i) :
        l2.append(i)
d = {}
for i in l2 :
    if i not in d.keys() :
        d.setdefault(i,1);
    else :
        d[i] += 1
for i in d.keys():
    print(i, d[i])