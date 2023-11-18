num=int(input("enter the 5 digit number:"))
a=num//10000
num1=num%10000
b=num1//1000
num2=num1%1000
c=num2//100
num3=num2%100
d=num3//10
e=num3%10
#reversing the number using string method:
reversed_num= str(e)+str(d)+str(c)+str(b)+str(a)
print("the reversed number is\n",reversed_num)
reversed_num=int(reversed_num)

if num<=9999:
    print("invalid input")

elif num==reversed_num:
    print("number is palindrome")
else:
    print("number is not palindrome")
        