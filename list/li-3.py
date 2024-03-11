n=int(input("Enter the limit:"))
l1=[]
l2=[]
for i in range (n) :
    j=int(input("Enter the element:"))
    l1.insert(i,j)
k=int(input("\nEnter the number:"))
for i in range (n) :
    if l1[i]<k:
        l2.insert(i,l1[i])
print(l2)