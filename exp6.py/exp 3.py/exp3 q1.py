s=input("enter a string:")
rev = s[::-1]
if s == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")