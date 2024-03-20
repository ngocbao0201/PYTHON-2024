l = ['0','1','2']

def check(n) :
    for i in n :
        if i not in l :
            return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")