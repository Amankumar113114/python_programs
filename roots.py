# Write a Python program to solve quadratic equation.
import math
print("please enter all the values with sign")
a=float(input("enter coefficient of x square : "))
b=float(input("enter coefficient of x  : "))
c=float(input("enter constant term : "))

D=((b**2) - (4*a*c))
if D>=0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-D**(1/2))/(2*a)
    print(f"the roots are {root1} and {root2}")
else:
    print("real roots does not exist")
    real_part=-b/(2*a)
    imag_part=math.sqrt(abs(D))/(2*a)
    print(f"the  imaginary roots are {real_part} + {(imag_part)}i and {real_part} - {(imag_part)}i")
