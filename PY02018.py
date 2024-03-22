n = int(input())
l = list(map(int,input().split()))
l.sort()
for i in l :
    if (i+1) not in l :
        print(i+1)
        break