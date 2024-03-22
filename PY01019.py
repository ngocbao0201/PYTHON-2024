import math

for t in range(int(input())) :
    s = input()
    check = 1
    for i in range(1,len(s)) :
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[len(s)-1-i]) - ord(s[len(s)-i])) :
            check = 0
    if check == 1 : 
        print("YES")
    else :
        print("NO")