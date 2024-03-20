for t in range(int(input())) :
    a = input()
    s1=''
    s2=''
    for i in range(0,2) :
        s1 = s1 + a[i]
    for i in range(len(a)-2,len(a)) :
        s2 = s2 + a[i]
    if s1 == s2 :
        print("YES")
    else :
        print("NO") 