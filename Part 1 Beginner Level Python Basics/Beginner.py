
# =====================================
# Beginner Level: Python Basics
# =====================================

# 1. Python Installation & Setup
# Theory: Install Python from python.org and use VS Code or Jupyter.
# 🇧🇩 Python লিখতে হলে আপনাকে প্রথমে এটি ইন্সটল করতে হবে এবং একটি কোড এডিটর সেটআপ করতে হবে।

# (No code required for this step)


# 2. Basic Syntax & Structure
# Theory: Python uses indentation instead of curly braces.
# 🇧🇩 Python এ কোড ব্লক বোঝাতে ইনডেন্টেশন (space/tab) ব্যবহার হয়।

print("Hello, World!")

if 5 > 2:
    print("5 is greater than 2")


# 3. Variables & Data Types
# Theory: Python is dynamically typed.
# 🇧🇩 Python-এ ভেরিয়েবল ঘোষণা করার সময় টাইপ বলে দিতে হয় না।

name = "Noman"
age = 25
height = 5.8
is_active = True
print(type(name), type(age), type(height), type(is_active))


# 4. Operators
# Theory: Used to perform operations.
# 🇧🇩 অপারেটর ব্যবহার করে গণনা, তুলনা ও যুক্তি প্রয়োগ করা যায়।

a = 10
b = 3

print(a + b)
print(a > b)
print(a % b)
print(a != b)


# 5. Control Flow
# Theory: Conditional execution using if, elif, else.
# 🇧🇩 if-else ব্যবহার করে নির্দিষ্ট শর্ত অনুযায়ী কোড চালানো যায়।

num = 5

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# 6. Loops: for, while
# Theory: Repeating tasks with loops.
# 🇧🇩 লুপ দিয়ে কোনো কাজ বারবার করানো যায়।

for i in range(5):
    print("For Loop:", i)

i = 0
while i < 5:
    print("While Loop:", i)
    i += 1


# 7. Functions
# Theory: Reusable blocks of code.
# 🇧🇩 ফাংশন হলো পুনরায় ব্যবহারযোগ্য কোড ব্লক।

def greet(name):
    return f"Hello, {name}!"

print(greet("Noman"))


# 8. Built-in Data Structures
# Theory: list, tuple, set, dict
# 🇧🇩 List, tuple, set ও dictionary হলো Python-এর মৌলিক ডেটা স্ট্রাকচার।

fruits = ['apple', 'banana']
fruits.append('mango')

days = ('Sun', 'Mon')
colors = {'red', 'green', 'red'}  # Set removes duplicates
student = {'name': 'Noman', 'age': 25}

print(fruits)
print(days)
print(colors)
print(student)
