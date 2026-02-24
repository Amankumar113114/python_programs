# body mass Index
def bmi(height,weight):
    return round(weight/(height**2),2)

h=float(input("enter height in meter"))
w=float(input("enter weight in kg"))
result=bmi(h,w)
print("your BMI is ",result)
if result<18.5:
    print("you are underweight")
elif (result>=18.5) and (result<25.0):
    print("you are healthy or normal")
elif(result>=25.0)and(result<30):
    print("you are overweight")
else:
    print("you are obese")
