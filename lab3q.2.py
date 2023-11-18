h=float(input("enter the value of height in meters:"))
w=float(input("enter the value in kg:"))
BMI=w/h**2
print("the BMI CALCULATED IS:\n","{:.2F}".format(BMI))


#weight in pounds and heght in inches
h=float(input("enter the value of height in inches:"))
w=float(input("enter the value in pounds:"))
#conversion from inch to meter:
converted_h=h*0.0254
#conversion from pounds to meter:
converted_w= w*0.453
calulated_BMI=converted_w/converted_h**2
print("the calculated BMI in metric value:\n",calulated_BMI)


