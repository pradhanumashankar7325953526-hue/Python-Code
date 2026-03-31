num=int(input("Enter a number:"))
rev=0
temp=num
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if(num==rev):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")