n=int(input("Enter the limit for first list:"))
l1=[]
l2=[]
l3=[]
for i in range (n):
    j=int(input("Enter the element:"))
    l1.insert(i,j)
n1=int(input("Enter the limit for second list:"))
for i in range (n1):
    j=int(input("Enter the element:"))
    l2.insert(i,j)
k=0
for i in range(n):
    for j in range(n1):
        if l1[i]==l2[j]:
            l3.insert(k,l1[i])
            k=k+1
            break
print(l3)