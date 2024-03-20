def check(n) :
    m = n[::-1]
    for i in range(1,len(n)) :
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(m[i]) - ord(m[i-1])) :
            return False
    return True

for t in range(int(input())) :
    n = input()
    if check(n) :
        print("YES")
    else :
        print("NO")