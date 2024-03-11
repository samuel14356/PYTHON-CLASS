s=input("Enter a string:")
d={}
k=0
l=0
s1=""
for i in range(len(s)):
    if s[i]!=" ":
        s1=s1+s[i]
    else:
        d[k]=s1
        s1=""
        k=k+1
d[k]=s1
k=k+1
for key in d:
    for i in range(k):
        if d[key]==d[i] and d[key]!=" ":
            l=l+1
            if l>1:
                d[i]=" "
    if l>0:
        print(d[key],l)
        l=0

