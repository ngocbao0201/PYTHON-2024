def cnt(s) :
    c = int(0)
    for i in s :
        if i != ' ' :
            c += 1
    return c

def check(s1,s2) :
    if s1 in s2 :
        return True
    