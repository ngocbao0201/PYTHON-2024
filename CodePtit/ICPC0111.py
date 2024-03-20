for t in range(0,int(input())) :
    n,d = (int(i) for i in input().split())
    list = []
    for j in input().split() :
        list.append(j)
    for i in range(d,n) :
        print(list[i], end = ' ')
    for i in range(0,d) :
        print(list[i], end = ' ')
    print()