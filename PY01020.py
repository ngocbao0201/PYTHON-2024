for t in range(int(input())) :
    a = input()
    s = ''
    for i in range(len(a)-2, len(a)) :
        s = s + a[i]
    if s == '86' :
        print("YES")
    else :
        print("NO")