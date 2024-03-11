import math
a=int(input("Enter a positive number:"))
x=a
m=a
z=1
for i in range(-1,a):
    z=(z+x/z)/2
    if m>z:
        m=z

print("Program estimate:",m)
print("Python estimate:",math.sqrt(a))