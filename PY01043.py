l = ['0','2','4','6','8']

def check(n) :
    m = str(n)[::-1]
    if str(n) != m :
        return False
    else :
        if len(str(n)) % 2 == 1 :
            return False
        for i in str(n) :
            if i not in l :
                return False
        return True
    
for t in range(int(input())) :
    n = input()
    for i in range(22,int(n),2) :
        if check(i) :
            print(i,end=' ')
    print()