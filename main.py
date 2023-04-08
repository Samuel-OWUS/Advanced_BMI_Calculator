#Advanced BMI Calculator

name=input("Enter your name:")
age=int(input("Enter your age:"))
Height=float(input("Enter your height in centimeters:"))
weight=float(input("Enter your weight in Kg:"))
Height=Height/100
BMI=weight/(Height*Height)
print("your Body Mass Index is:",BMI)
if (BMI>0):
    if(BMI<=16):
        print("You are severely underweight")
    elif(BMI<=20.5):
        print("You are underweight")
    elif(BMI<=30):
        print("You are healthy")
    elif(BMI<=70):
        print("You are overweight")
    else: print("You are severely overweight")
else:("Enter valid details")