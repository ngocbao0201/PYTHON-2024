p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True :
    s1 = input().split()
    k = int(s1[0])
    if k == 0 :
        break
    else :
        x = ''
        s = str(s1[1])
        for i in s :
            for j in range(0,len(p)) :
                if p[j] == i :
                    x = x + p[(j+k)%28]
    for i in range(0,len(x)) :
        print(x[len(x)-1-i], end='')
    print()

