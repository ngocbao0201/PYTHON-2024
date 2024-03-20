for t in range(0,int(input())) :
    s = str(input())
    cnt = 1
    s1 = ''
    for i in range(0,len(s)-1) :
        if str(s[i]) == str(s[i+1]) :
            cnt = cnt + 1
        else :
            s1 = s1 + str(cnt) + s[i]
            cnt = 1
    if cnt == len(s) :
        print(str(cnt) + s[0])
    elif s[len(s)-1] != s[len(s)-2] :
        s1 = s1 + '1' + str(s[len(s)-1])
        print(s1)
    else :
        s1 = s1 + str(cnt) + s[len(s)-1]
        print(s1)
        
        
    