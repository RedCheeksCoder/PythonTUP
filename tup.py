#print("Hello World")

#grades = 5
#print(grades)

#String concatenation
""" first_name = "Bryan"
last_name = "Odina"
age = 22
full_name_age = first_name + " " + last_name + " " + age
print(full_name_age) """

#Integers Augmentation Assignmen operator
""" age = 21
age += 1
age = age +1
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

#AREA OF TRIANGLE
""" base = float(input("Enter the base: "))
height = float(input("Enter height"))
area = 0.5*base*height
print(f"The base is {base} units and the height is {height} units. And the area is {area} square units") """

#MATH FUNCTIONS

import math
#Squaring
""" number = input("Enter number of input: ")
number = number **2
print(number) """

""" number = int(input("Enter number of input: "))
number **=3
print(number) """

""" #Modulus - REMAINDER
number = int(input("Enter number of input: "))
remainder = number % 2
print(remainder) """

#Min-max
""" x = 1.25
y = 2.75
z = 5.00

results = min(x,y,z)
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
""" temperature = 31
if temperature > 0 and temperature < 30:
    print("Temperature is in good range")
elif temperature == 32 or temperature == 40:
    print("Temperature is in medyo bad range")
else:
    print("Temp is bad") """

#STRING METHODS
password = "mathenatics"

#print(password.capitalize())
#print(password.upper())
#print(password.lower())
#print(password.isdigit())
#print(password.isalpha())
#print(password.count("m"))
#print(password.replace("n", "m"))

#USERNAME VALIDATION
#Length is more than 12
#No spaces
#Alphabets

#User input Conditional statement string methods

""" print(password.find("t")) """

""" if len(password) >= 8:
    print("Proceed!")
else:
    print("Passwords must be more than 8 characters in length.") """


#INDEXING
#credit_card = "5417-2351-6678-1124"
#credit_card [first:last:step]
#print(credit_card[::4])

#Last four digit of the creditcard number
""" credit_card = input("Enter your credit card number: ")
last_four = credit_card[-4:]
print(f"****-****-****-{last_four}") """

#LOOPS
#While loop
#-------------EXAMPLE 1 -------------
""" name = input("Enter your name: ")
while name == "":
    print("Please enter your name!")
    name = input("Enter your name: ")

print(f"Hello {name}!") """

#-------------EXAMPLE 2 -------------

""" age = int(input("Enter your age: "))

while age < 0:
    print("You are either not born yet or still a baby.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old") """

#-------------EXAMPLE 3 -------------
""" food = input("Enter a food you like (q to quit)") 

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit)") 

print("BYEEEE!!!") """

######## FOR LOOP #########
#-------------EXAMPLE 1 -------------
""" for x in range (1, 11):
    print(x) """
#-------------EXAMPLE 2 -------------
""" for x in reversed(range (1, 11)):
    print(x) 

print("HAPPY BIRTHDAYYYYY!!!")"""
#-------------EXAMPLE 3 -------------
""" for x in range (1, 11, 2):
    print(x) """
#-------------EXAMPLE 4 -------------
""" credit_card = "5417-2351-6678-1124"

for x in credit_card:
    print(x) """

#-------------CONTINUE -------------
""" for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x) """
#-------------BREAK -------------
""" for x in range(1,21):
    if x == 13:
        break
    else:
        print(x) """

#DELAY
""" import time
for x in range(1,11):
    time.sleep(1) #1sec delay
    print(x) """

######### DATA STRUCTURES #########
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#fruits = ["apple", "orange", "banana", "coconut"]
#List  = [] ordered and changeable. Duplicates OK
#print(len(fruits))
#print("pineapple" in fruits)
#print(help(fruits)) #AskForHelp

#fruits[0] = "pineapple"

#ADDING in LIST
""" 
print(fruits)
print("pineapple" in fruits) """

#-------METHODS---------------
#Add an element at the end of the list
#fruits.append("Strawberry")
#print(fruits)

#remove an element
#fruits.remove("pineapple")
#print(fruits)

#insert an an index
#fruits.insert(2, "Almond")
#print(fruits)

#sorting alphabetically
#fruits.sort()
#print(fruits)

#reverse order
#fruits.reverse()
#print(fruits)

#print(fruits.count("coconut"))


#---------SETS----------
#Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#fruits = {"apple", "orange", "banana", "mango"}
#Error: fruits[0] #Note: Unordered - cannot have 

#adding an element 
#fruits.add("strawberry")
#print(fruits)

#removing an element 
#fruits.add("apple")
#fruits.remove("mango")
#print(fruits)

#removing random element
#fruits.pop()
#print(fruits)
#fruits.pop()
#print(fruits)
#clear all elements
#clear()

#NO DUPLICATES
#Add same element to check

#---------Tuple----------
#Tuple = () ordered and unchangeable. Duplicates OK. FASTER
#fruits = ("apple", "orange", "banana", "mango", "banana")

#Only two common methods
#get the index
#print(fruits.index("banana"))
#number of occurence in tuple
#print(fruits.count("banana"))

#####SHOPPING CART#####
""" foods = []
prices = []
total = 0
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price

print()
print(f"Your total is: ${total}") """

#---------DICTIONARY-----------------
#dictionary =  a collection of {key:value} pairs
#ordered and changeable. No duplicates

""" #capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"} """

#print(capitals.get("USA"))


""" if capitals.get("India"):
    print("That capital exists")
else:
    print("That capital doesn't exist") """



""" capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})

capitals.pop("China")
capitals.popitem()
capitals.clear()
print(capitals) """


#keys = capitals.keys()
""" for key in capitals.keys():
    print(key)
values = capitals.values()
for value in capitals.values():
    print(value) """


""" items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}") """

""" student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eva": 85,
    "Frank": 78,
    "Grace": 92,
    "Hank": 88,
    "Ivy": 90,
    "Jack": 95
}
list_of_students = []

items = student_grades.items()
for key, value in items:
    if value == 85:
        list_of_students.append(key)

print(list_of_students) """

menu = {"pizza": 3.00,
               "nachos": 4.50,
               "popcorn": 6.00,
               "fries": 2.50,
               "chips": 1.00,
               "pretzel": 3.50,
               "soda": 3.00,
               "lemonade": 4.25}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")

