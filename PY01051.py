def check(n) :
    sum = int(0)
    for i in n :
        sum += int(i)
    if len(str(sum)) < 2 :
        return False
    if str(sum) == str(sum)[::-1] :
        return True
    else :
        return False
    
for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")