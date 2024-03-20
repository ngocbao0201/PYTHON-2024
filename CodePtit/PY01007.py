
for t in range( int(input())) :
    a,x,b = [float(i) for i in input().split()]
    cnt = int(0)
    while a < b :
        cnt = cnt + 1
        a =  a + a * float((x/100)) 
    print(cnt)        