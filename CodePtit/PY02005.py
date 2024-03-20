n = int(input())
a = list(map(int,input().split()))
cnt = int(0)
for i in range(0,n) :
    x = int(a[i])
    for j in a[i+1:n] :
        if int(j) < x :
            cnt += 1
print(cnt)