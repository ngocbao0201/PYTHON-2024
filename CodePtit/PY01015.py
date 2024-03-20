def check(n) :
    for i in range(len(n)-1) :
        if int(n[i+1]) < int(n[i]) : 
            return False
    return True

for t in range(int(input())) :
    a = input()
    if check(a) :
        print("YES")
    else :
        print("NO")