import array as arr

t = int(input())
for i in range(t) :
    b = arr.array('i')
    a = input()
    l = len(a)
    for j in range(l) :
        b.append(int(a[j]))
    b.reverse()
    for j in range(len(b)-1) :
        if(b[j] >= 5) :
            b[j+1] += 1
            b[j] = 0
        else :
            b[j] = 0
    b.reverse()
    for j in b :
        print(j, end='')
    print()
    