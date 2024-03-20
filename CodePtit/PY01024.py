def check(n) :
    sum = 0
    for i in n :
        sum = sum + int(i)
    if sum % 10 != 0 :
        return False
    for i in range(1,len(n)) :
        if abs(int(n[i]) - int(n[i-1])) != 2 :
            return False
    return True
    
for t in range(int(input())) :
    a = input()
    if check(a) == True :
        print("YES")
    else :
        print("NO")