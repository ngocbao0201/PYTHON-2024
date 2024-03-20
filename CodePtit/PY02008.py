import math

def nguyen_to(n) :
    if n < 2 :
        return False
    else :
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                return False
    return True

l = []
i = int(2)
while len(l) < 1000 :
    if nguyen_to(i) :
        l.append(i)
    i = i + 1

n,x = (int(j) for j in input().split())
print(x,end = ' ')
for j in range(0,n):
    y = int(x) + int(l[j])
    print(y, end = ' ')
    x = y

