def check(n) :
    if len(n) % 2 == 0 :
        return False
    if int(n[0]) == int(n[1]) :
        return False
    m = int(n[0])
    for i in range(2,len(n),2) :
        if int(n[i]) != m :
            return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")