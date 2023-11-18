basic_salary=float(input("enter the salary:"))
HRA=0.2*basic_salary
TA=0.5*basic_salary
DA=0.1*basic_salary
gross_salary=basic_salary+HRA+TA+DA
print("gross salary of the employee:\n",gross_salary)
if gross_salary<300000:
    print("income tax 0%")
elif 300000<=gross_salary<1000000:
    print("income tax rate is 10% 0f gross salary")
elif 1000000<=gross_salary<=2500000:
    print(" income tax rate is 20% of the gross salay")
else:
    print("income tax rate is 30% of the gross salary")
