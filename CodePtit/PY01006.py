
def check(n) :
    for i in n :
        if i != '4' and i != '7' :
            return False
    return True

for t in range( int(input()) ) :
    n = input()
    if check(n) == True :
        print("YES")
    else :
        print("NO")