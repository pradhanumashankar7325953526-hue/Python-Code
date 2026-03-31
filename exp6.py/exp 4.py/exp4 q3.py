n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
gcd=1
while(gcd<=n1 and gcd<=n2 and gcd<=n3):
    if(n1%gcd==0 and n2%gcd==0 and n3%gcd==0):
        gcd+=1
    else:
        gcd+=1
print("GCD is:",gcd-1)