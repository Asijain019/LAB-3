num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
if num1>0 and num2>0 and num3>0:
    if num1>num2:
        f1=num1
    else:
        f1=num2    
    if f1>num3:
        print("largest number is",f1)
    else:
        print("the largest number is",num3)        
else:
    print("invalid input")
            