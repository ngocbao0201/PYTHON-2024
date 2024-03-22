for t in range(0,int(input())) :
    a = int(input())
    sum = float(0)
    if a%2==0 :
        for i in range(2,a+1,2) :
            sum = sum + 1/i
    else :
        for i in range(1,a+1,2) :
            sum = sum + 1/i
    print("{:.6f}".format(sum))