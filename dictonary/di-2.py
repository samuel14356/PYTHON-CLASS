x={'k1':'v1','k2':'v2','k3':'v3'}
d={}
for i in reversed(x):
    d[i]=x[i]
print(d)