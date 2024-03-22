def uscln(a,b) :
    if b == 0 :
        return a
    return uscln(b,a%b)

a,n = (int(i) for i in input().split())
cnt = 0
for i in range(10**(n-1),10**n) :
    if uscln(a,i) == 1 :
        print(i,end=' ')
        cnt = cnt + 1
        if cnt % 10 == 0 and cnt != 0 :
            print()