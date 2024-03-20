for t in range(0,int(input())) :
    n = input()
    if int(n) % 7 == 0 :
        print(n)
    else : 
        i = int(0)
        while i <= 1000 :
            m = str(n)[::-1]
            n = int(n) + int(m)
            if n % 7 == 0 :
                break
        if i > 1000 :
            print("-1")
        else :
            print(n)
        