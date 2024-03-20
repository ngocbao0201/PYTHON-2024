while True :
    l = list(map(int,input().split()))
    if l.count(0) == 4 :
        break
    else :
        cnt = int(0)
        while len(set(l)) > 1 :
            x = l[0]
            l[0] = abs(l[0]-l[1])
            l[1] = abs(l[1]-l[2])
            l[2] = abs(l[2]-l[3])
            l[3] = abs(l[3]-x)
            cnt += 1
        print(cnt)