def check(n) :
    if len(n) % 2 == 1 :
        return False
    for i in range(len(n)) :
        if n[i] != n[len(n)-1-i] :
            return False
    for i in n :
        if int(i) % 2 == 1 :
            return False
    return True

for t in range(int(input())) :
    n = int(input())
    for i in range(22,n,2) :
        if check(str(i)) == True :
            print(i,end=' ')
    print()
        
        
    