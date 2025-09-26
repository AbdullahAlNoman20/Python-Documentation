# =====================================
# Beginner Level: Python Basics
# =====================================

"""
This file contains comprehensive Python basics with detailed explanations
and practical examples for beginners. Each section includes theory, code examples,
and Bengali translations for better understanding.
"""

# =====================================
# 1. Python Installation & Setup
# =====================================
"""
Theory: Python is a high-level, interpreted programming language.
Installation: Download from python.org and use VS Code, PyCharm, or Jupyter.
🇧🇩 Python একটি উচ্চ-স্তরের প্রোগ্রামিং ভাষা। python.org থেকে ডাউনলোড করে 
VS Code, PyCharm বা Jupyter ব্যবহার করুন।
"""

# Check Python version
import sys
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# =====================================
# 2. Basic Syntax & Structure
# =====================================
"""
Theory: Python uses indentation (4 spaces) instead of curly braces for code blocks.
Comments start with # and docstrings use triple quotes.
🇧🇩 Python এ কোড ব্লক বোঝাতে ইনডেন্টেশন (৪টি স্পেস) ব্যবহার হয়।
"""

# Your first Python program
print("Hello, World!")
print("Welcome to Python Programming!")

# Indentation example
if 5 > 2:
    print("5 is greater than 2")
    print("This line is also indented")
    if 3 > 1:
        print("Nested indentation works!")

# =====================================
# 3. Variables & Data Types
# =====================================
"""
Theory: Python is dynamically typed - you don't need to declare variable types.
Variables are created when you assign values to them.
🇧🇩 Python-এ ভেরিয়েবল ঘোষণা করার সময় টাইপ বলে দিতে হয় না।
"""

# String variables
name = "Noman"
city = "Dhaka"
country = "Bangladesh"
print(f"Name: {name}, City: {city}, Country: {country}")

# Numeric variables
age = 25
height = 5.8
weight = 70.5
print(f"Age: {age}, Height: {height}, Weight: {weight}")

# Boolean variables
is_student = True
is_employed = False
print(f"Is student: {is_student}, Is employed: {is_employed}")

# Check data types
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Type conversion
age_str = str(age)  # Convert to string
height_int = int(height)  # Convert to integer
print(f"Age as string: {age_str}, Height as int: {height_int}")

# =====================================
# 4. Operators
# =====================================
"""
Theory: Operators are symbols that perform operations on variables and values.
Types: Arithmetic, Comparison, Logical, Assignment, Identity, Membership
🇧🇩 অপারেটর ব্যবহার করে গণনা, তুলনা ও যুক্তি প্রয়োগ করা যায়।
"""

# Arithmetic operators
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical operators
x = True
y = False
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Assignment operators
num = 10
num += 5  # num = num + 5
print(f"After += 5: {num}")
num *= 2  # num = num * 2
print(f"After *= 2: {num}")

# =====================================
# 5. Control Flow - Conditional Statements
# =====================================
"""
Theory: Control flow determines the order in which statements are executed.
if, elif, else statements allow conditional execution.
🇧🇩 if-else ব্যবহার করে নির্দিষ্ট শর্ত অনুযায়ী কোড চালানো যায়।
"""

# Basic if statement
num = 5
if num > 0:
    print(f"{num} is positive")

# if-else statement
score = 85
if score >= 60:
    print("Pass!")
else:
    print("Fail!")

# if-elif-else statement
temperature = 25
if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("It's warm!")
elif temperature > 10:
    print("It's cool!")
else:
    print("It's cold!")

# Nested conditions
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive!")
else:
    print("You're too young to drive!")

# =====================================
# 6. Loops
# =====================================
"""
Theory: Loops allow you to repeat a block of code multiple times.
for loop: iterate over a sequence, while loop: repeat while condition is true
🇧🇩 লুপ দিয়ে কোনো কাজ বারবার করানো যায়।
"""

# for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# for loop with list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in the list:")
for fruit in fruits:
    print(f"- {fruit}")

# for loop with enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# while loop
print("\nWhile loop example:")
count = 0
while count < 3:
    print(f"While loop iteration: {count + 1}")
    count += 1

# Loop control statements
print("\nLoop control example:")
for i in range(1, 6):
    if i == 3:
        continue  # Skip this iteration
    if i == 5:
        break  # Exit the loop
    print(f"Number: {i}")

# =====================================
# 7. Functions
# =====================================
"""
Theory: Functions are reusable blocks of code that perform specific tasks.
They help organize code and avoid repetition.
🇧🇩 ফাংশন হলো পুনরায় ব্যবহারযোগ্য কোড ব্লক।
"""

# Basic function
def greet(name):
    """This function greets a person by name."""
    return f"Hello, {name}! Welcome to Python!"

# Function with multiple parameters
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Function with default parameters
def greet_with_title(name, title="Mr."):
    """Greet with optional title."""
    return f"Hello, {title} {name}!"

# Function with multiple return values
def get_name_and_age():
    """Return multiple values."""
    return "Noman", 25

# Using functions
print(greet("Noman"))
print(f"Area of rectangle: {calculate_area(5, 3)}")
print(greet_with_title("Noman"))
print(greet_with_title("Sarah", "Ms."))

name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# =====================================
# 8. Built-in Data Structures
# =====================================
"""
Theory: Python provides several built-in data structures:
- List: ordered, mutable collection
- Tuple: ordered, immutable collection  
- Set: unordered collection of unique elements
- Dictionary: key-value pairs
🇧🇩 List, tuple, set ও dictionary হলো Python-এর মৌলিক ডেটা স্ট্রাকচার।
"""

# Lists
print("=== LISTS ===")
fruits = ['apple', 'banana', 'orange']
print(f"Original list: {fruits}")

# List operations
fruits.append('mango')  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, 'grape')  # Insert at index
print(f"After insert: {fruits}")

fruits.remove('banana')  # Remove element
print(f"After remove: {fruits}")

print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"List length: {len(fruits)}")

# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"First 3 numbers: {numbers[:3]}")
print(f"Last 3 numbers: {numbers[-3:]}")
print(f"Middle numbers: {numbers[2:7]}")

# Tuples
print("\n=== TUPLES ===")
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(f"Days tuple: {days}")
print(f"First day: {days[0]}")
print(f"Last day: {days[-1]}")

# Tuples are immutable
# days[0] = 'Sunday'  # This would cause an error

# Sets
print("\n=== SETS ===")
colors = {'red', 'green', 'blue', 'red', 'yellow'}  # Duplicates removed
print(f"Colors set: {colors}")

colors.add('purple')
print(f"After adding purple: {colors}")

colors.remove('red')
print(f"After removing red: {colors}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# Dictionaries
print("\n=== DICTIONARIES ===")
student = {
    'name': 'Noman',
    'age': 25,
    'city': 'Dhaka',
    'subjects': ['Math', 'Physics', 'Chemistry']
}
print(f"Student info: {student}")

# Access dictionary values
print(f"Student name: {student['name']}")
print(f"Student age: {student.get('age', 'Not specified')}")

# Add/update dictionary
student['grade'] = 'A'
student['age'] = 26
print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# =====================================
# 9. String Manipulation
# =====================================
"""
Theory: Strings are sequences of characters. Python provides many methods
for string manipulation and formatting.
🇧🇩 স্ট্রিং হলো ক্যারেক্টারের সমষ্টি। Python-এ স্ট্রিং নিয়ে কাজ করার অনেক পদ্ধতি আছে।
"""

# Basic string operations
text = "Hello World"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")

# String slicing
print(f"First 5 characters: {text[:5]}")
print(f"Last 5 characters: {text[-5:]}")
print(f"Characters 2-7: {text[1:7]}")

# String methods
sentence = "  Python is awesome!  "
print(f"Original: '{sentence}'")
print(f"Stripped: '{sentence.strip()}'")
print(f"Split: {sentence.strip().split()}")
print(f"Replace: {text.replace('World', 'Python')}")

# String formatting
name = "Noman"
age = 25
# f-string (Python 3.6+)
message = f"My name is {name} and I am {age} years old."
print(message)

# format() method
message2 = "My name is {} and I am {} years old.".format(name, age)
print(message2)

# % formatting (older style)
message3 = "My name is %s and I am %d years old." % (name, age)
print(message3)

# =====================================
# 10. Input and Output
# =====================================
"""
Theory: input() function gets user input, print() displays output.
You can format output in various ways.
🇧🇩 input() দিয়ে ব্যবহারকারীর কাছ থেকে ইনপুট নেওয়া যায়, print() দিয়ে আউটপুট দেখানো যায়।
"""

# Getting user input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name}! You are {age} years old.")

# Formatted output
print("=== FORMATTED OUTPUT ===")
print("Name: %-10s Age: %3d" % ("Noman", 25))
print("Name: %-10s Age: %3d" % ("Sarah", 30))

# Multiple print statements
print("Line 1", end=" ")
print("Line 2", end=" ")
print("Line 3")

# =====================================
# 11. Basic Error Handling
# =====================================
"""
Theory: Errors can occur during program execution. Basic error handling
helps make programs more robust.
🇧🇩 প্রোগ্রাম চালানোর সময় ভুল হতে পারে। ভুল ধরতে try-except ব্যবহার করা হয়।
"""

# Basic try-except
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Multiple exception handling
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("Error: Invalid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")

# =====================================
# 12. Basic File Operations
# =====================================
"""
Theory: Files can be read from and written to using Python's built-in functions.
Always use proper file handling to avoid resource leaks.
🇧🇩 Python দিয়ে ফাইল পড়া ও লেখা করা যায়।
"""

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.\n")
    file.write("Learning Python is fun!")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
with open("sample.txt", "r") as file:
    print("\nReading line by line:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

# =====================================
# 13. Basic Math Operations
# =====================================
"""
Theory: Python provides built-in math functions and the math module
for advanced mathematical operations.
🇧🇩 Python-এ গণিতের কাজ করার জন্য অনেক ফাংশন আছে।
"""

import math

# Basic math operations
print("=== MATH OPERATIONS ===")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Power of 2^3: {math.pow(2, 3)}")
print(f"Absolute value of -5: {abs(-5)}")
print(f"Round 3.7: {round(3.7)}")
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print(f"Floor of 3.8: {math.floor(3.8)}")

# Trigonometric functions
angle = math.pi / 4  # 45 degrees in radians
print(f"Sin(45°): {math.sin(angle):.3f}")
print(f"Cos(45°): {math.cos(angle):.3f}")
print(f"Tan(45°): {math.tan(angle):.3f}")

# =====================================
# 14. Practice Exercises
# =====================================
"""
Here are some practice exercises to reinforce what you've learned:
"""

print("\n=== PRACTICE EXERCISES ===")

# Exercise 1: Calculate BMI
def calculate_bmi(weight, height):
    """Calculate Body Mass Index."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = 70  # kg
height = 1.75  # meters
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi}")

# Exercise 2: Check if number is even or odd
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:", [num for num in numbers if is_even(num)])

# Exercise 3: Simple calculator
def simple_calculator(a, b, operation):
    """Simple calculator function."""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print(f"10 + 5 = {simple_calculator(10, 5, '+')}")
print(f"10 - 5 = {simple_calculator(10, 5, '-')}")
print(f"10 * 5 = {simple_calculator(10, 5, '*')}")
print(f"10 / 5 = {simple_calculator(10, 5, '/')}")

print("\n=== END OF BEGINNER LEVEL ===")
print("Congratulations! You've completed the Python basics.")
print("Next: Move to Intermediate Level for more advanced concepts.")