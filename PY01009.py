chu_thuong = 0
chu_hoa = 0
s = input()
for i in s :
    if i >= 'a' and i <= 'z' :
        chu_thuong = chu_thuong + 1
    else :
        chu_hoa = chu_hoa + 1
if chu_hoa > chu_thuong :
    print(s.upper())
else :
    print(s.lower())