for t in range(0,int(input())) :
    a = input()
    sum = 0
    for i in a :
        sum = sum + int(i)
    if sum % 3 == 0 :
        print("YES")
    else :
        print("NO")