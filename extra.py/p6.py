#wap to enter two inmteger on keyword and perform all the arithmatic operatin on them
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b if b!=0 else "Undefined")
print("Modulus:", a%b if b!=0 else "Undefined")
print("Floor Division:", a//b if b!=0 else "Undefined")
print("Exponentiation:", a**b)