import math

n = int(input())
l = list(map(int,input().split()))
l.sort()
for i in range(0,n-1):
    for j in range(i+1,n) :
        if math.gcd(l[i],l[j]) == 1 :
            print(l[i],end=' ')
            print(l[j])