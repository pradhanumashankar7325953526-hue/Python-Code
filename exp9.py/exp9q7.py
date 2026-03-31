import math
x=eval(input("Enter the power list:"))
y=eval(input("Enter the number list:"))
def power(x,y):
    z=int(pow(x,y))
    return z
l=list(map(power,x,y))
print("the resultant list:",1)