num=int(input("enter a 3 digit number:"))
x=num//100
num1=num%100
y=num1//10
z=num1%10
armstrong_no=x**3+y**3+z**3
if num<0 or num>=1000:
    print("invalid input")
elif num== armstrong_no:
    print("the no is armstrong")
else:
    print("not an armstrong")    
