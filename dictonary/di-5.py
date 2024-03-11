l={}
f=True
l1=[]
l2=[]
l3=[]
while (f==True):
    s=input("Enter team name or stop :")
    if s=='stop':
        f==False
        break 
    n=int(input("Enter no. of games won:"))
    n2=int(input("Enter no. of games lost:"))
    l1.append(n)      
    l2.append(n2)
    l3.append(s)
    l[s]=[n,n2]  
print("The name of the teams are:")  
for key in l:
    print(key)
print('Team with greatest wins:',l3[l1.index(max(l1))])
print('Team with greatest loss:',l3[l2.index(max(l2))])
s=input("Enter team to find win percentage:")
l4=l[s]
print('win percentage:',float((l4[0])/(l4[0]+l4[1]))*100)