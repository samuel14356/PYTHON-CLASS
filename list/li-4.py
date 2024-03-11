n=int(input("Enter the limit:"))
l1=[]
l2=[]
for i in range (n) :
    j=int(input("Enter the element:"))
    l1.insert(i,j)
for i in range (n):
    if l1[i]%2 == 0:
        l2.insert(i,l1[i])
l2.sort()
print(l2)