x=int(input("enter the value:"))
y=int(input("enter the value:"))
z=int(input("enter the value:"))
if x<0 or y<0 or z<0:
    print("invalid input")
elif x+y>z and x+z>y and y+z>x:
    print("it will form the triangle")
else:
    print("does not forms the triamgle")

                    