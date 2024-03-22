def check(n) :
    a = n[0]
    b = n[1]
    for i in range(2,len(n)) :
        if n[i] != a and n[i] != b :
            return False
    for i in range(0,len(n)-2) :
        if n[i] != n[i+2] :
            return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")
        