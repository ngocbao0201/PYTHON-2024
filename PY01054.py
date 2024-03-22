for t in range(int(input())) :
    n = input()
    mul = int(1)
    for i in n:
        if int(i) != 0 :
            mul = mul * int(i)
    print(mul)