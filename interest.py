a=float(input("Enter the investment amount:"))
n=int(input("Enter the number of years:"))
r=int(input("Enter the rate:"))
print("year\t\tstarting balance\tinterest\t\tending balance\n")
e=0
ci=0
inter=0
for i in range(1,n+1) :
    ci=(a*r)/100
    e=a+ci
    print(i,"\t\t",'%8.2f'%a,"\t\t",'%5.2f'%ci,"\t\t",'%8.2f'%e,"\n")
    a=e
    inter=inter+ci
print("Ending balance=$",'%8.2f'%e)
print("Total interest earned=$",'%8.2f'%inter)