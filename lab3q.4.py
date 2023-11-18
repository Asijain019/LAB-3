n=int(input("enter the 3 digit number:"))
x=n//100
n1=n%100
y=n1//10
z=n1%10
SUM=x+y+z
print("the sum of the digits\n",SUM)
#weather the number is divisible by 3:
if SUM%3==0:
    print("the number is divisible by 3")
else:
    print("the number is not divisilbe by 3")
        