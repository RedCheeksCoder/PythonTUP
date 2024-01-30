#print("Hello World")

#grades = 5.00
#print(grades)

#String concatenation
""" first_name = "Bryan"
last_name = "Odina"
age = 22
full_name_age = first_name + " " + last_name + " " + age
print(full_name_age) """

#Integers
""" age = 21
age += 1
print(age)
print(type(age)) """

""" age = 21
print("You are " + str(age)) """

#FLOAT
""" height = 272.5

print(height)
print(type(height))
print("Your height is " + str(height) + "cm") """

#BOOLEAN
""" isStudent = True;

print(isStudent)
print(type(isStudent)) """


""" name = "Bryan"
school = "TUP-Taguig"
age = 20
height = 167.2
weight = 70
grades = 2.25
from_taguig = True """

""" #USER-INPUT and F string
user_name = input("Enter your Username: ")
age = input("Enter your age: ")
print(f"Your username is {user_name}. Your age is {age}") """

""" #MAD LIBS
name = "Usain Bolt"
km = 200
time = 10
water = 0.1

print(f"{name} is currently running to Market2x! He/she is already at {km}km having only the time of {time}minutes and took {water} liters") """

""" #AREA OF TRIANGLE
base = float(input("Enter the base: "))
height = float(input("Enter height"))
area = 0.5*base*height
print(f"The base is {base} units and the height is {height} units. And the area is {area} square units") """

#MATH FUNCTIONS

import math
""" #Squaring
number = input("Enter number of input: ")
number = number **2
print(number) """

""" number = int(input("Enter number of input: "))
number **=3
print(number) """

""" #Modulus - REMAINDER
number = int(input("Enter number of input: "))
remainder = number % 2
print(remainder) """

""" #Min-max
x = 1.25
y = 2.75
z = 5.00

results = round(y)
print(results) """

""" import math
print(math.pi)
print(math.e) """

""" import math
number = 9.25
print(math.sqrt(number))
print(math.ceil(number))
print(math.floor(number)) """

""" import math
#Circumference of circle 2pir
radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius
print(f"Circumference: {circumference:.2f}") """

""" #AREA OF A CIRCLE pir2 """

#Conditional statements
""" age = int(input("Enter your age: "))

if age >= 18:
    print("You are now in legal age.")
else:
    print("You are NOT in legal age.") """

#Raw grades
""" grades = float(input("Enter your age: "))

if grades >= 49.5:
    print("You are PASADO.")
elif grades <= 30:
    print("You are SUPER BAGSAK.")
else:
    print("You are NOT PASADO.") """

#BOOLEAN + Conditional statements
""" isStudent = False

if isStudent:
    print("You are STUDENT.")
else:
    print("You are NOT STUDENT.") """

""" answer = input("Do you wnat to continue? (Y/N)")

if answer == 'Y':
    print("Continue sa pag-aaral")
else:
    print("Welcome to my youtube channel!") """

#LOGICAL OPERATORS AND | OR | NOT
temperature = 32
if temperature > 0 and temperature < 30:
    print("Temperature is in good range")
elif temperature == 32 or temperature == 40:
    print("Temperature is in medyo bad range")
else:
    print("Temp is bad")