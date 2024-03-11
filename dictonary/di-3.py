d1={'a1':'z1','a2':'z2','a3':'z3'}
d2={'b1':'z2','a3':'z3','b2':'z1'}
c=0
for key in d2:
    for i in d1:
        if d2[key]==d1[i] and d1[i]!=" ":
            c=c+1
            if c>1:
                d1[i]=" "
    if c>0:
        print(d2[key])
        c=0