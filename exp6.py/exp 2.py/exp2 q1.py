p = int(input("Enter principal amount:"))
t = int(input("Enter TIme Period:"))
r = int(input("Enter rate of interest:"))
si = (p*t*r)/100
amp = p*(1+r/100)**t
ci = amp - p
print("Simple Interest:",si)
print("Compound Interest:",ci)