giai_thua = {
    '0' : 1,
    '1' : 1,
    '2' : 2,
    '3' : 6,
    '4' : 24,
    '5' : 120,
    '6' : 720,
    '7' : 5040,
    '8' : 40320,
    '9' : 362880
}

for t in range(0,int(input())) :
    a = input()
    sum = int(0)
    for i in a :
        sum = sum + int(giai_thua[i])
    if sum == int(a) :
        print("Yes")
    else : print("No")