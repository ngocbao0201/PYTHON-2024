import array as arr

a,k,n = [int(i) for i in input().split()]
check = 0
b = k - a % k
for i in range(a+b,n+1,k) :
    print(i-a,end=' ')
    check = 1
if check == 0 :
    print("-1")
