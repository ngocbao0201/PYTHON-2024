def thap_ha_noi(n,a,c,b) :
    if n == 1 :
        print(a, "->", c)
        return
    else :
        thap_ha_noi(n-1,a,b,c)
        print(a, "->", c)
        thap_ha_noi(n-1,b,c,a)
n = int(input())
thap_ha_noi(n,'A','C','B') 