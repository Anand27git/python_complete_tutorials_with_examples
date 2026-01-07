# Basic concepts of python

# Author : ANAND KUMAR V
# Purpose : learning python concept for AI

# Basic print statement in python
print("Hello world😊")
print("*" * 10)

# Basic declaration in python

x = 1
y = 2
unit_price = 3

# variables in python

student_count = 1000  # int declaration
rating = 4.99  # float declaration
is_published = True  # boolean declaration
course_name = "python"  # string declaration
print(student_count)

# Strings

course = "python programming"

# --------Functions-------#

len(course)  # len function is used to count charters in python
print(len(course))
print(course[0])  # first character of the index will get print
print(course[-1])  # last character of the index will get print
print(course[0:3])  # it will print starting string to 3rd string
print(course[0:])  # by default, it will assume and print all string
print(course[:3])  # by default, it will add starting index as 0 and print rest 3 characters
print(course[:])  # it will print all characters

# escape sequences in python

# \"
# \'
# \\
# \n

course = "python \n programming"
print(course)

# Formatted String

first = "Anand"
last = "kumar"
full = f"{first} {last}"
print(full)

# string methods

print(course.upper())
print(course.lower())
print(course.title())
print(course.rstrip())  # whitespace will be removed in the string
print(course.find("ro"))  # this method will find the string which mentioned
print(course.replace("p", "j"))  # this will replace old string to new string
print("pro" in course)  # this method will check true or false in string

# numbers

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # used to divide and get float output
print(10 // 3)  # used to divide and get integer output
print(10 % 3)
print(10 ** 3)  # 10 power of 3

x = x + 3
x += 3  # line no 77 expression and 78 both are same
print(x)

# Working with numbers
import math

print(round(2.9))
print(abs(-2.9))

math.ceil(2.2)
print(math.ceil(2.2))

# Type conversions
x = input("x: ")
print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str( x) -- this are the built-in type conversation in python


# bool considered as Falsy and true

# "", 0 ,None -- these are considered as  Falsy

# primitive types

fruit = "Apple"
print(fruit[1:-1])

# comparission Operators

# "bag" > "apple" -->True
# "bag" == "BAG"  -->False

ord("b")
ord("B")  # shows asci code of char

# Conditional statement

temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink Water") # white space need to be there to execute both the statements
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
