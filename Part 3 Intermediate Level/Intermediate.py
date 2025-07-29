
# =====================================
# Intermediate Level: Deeper Python Concepts
# =====================================

# 9. String Manipulation
# Theory: Strings can be sliced and formatted.
# 🇧🇩 স্ট্রিং কেটে, যোগ করে বা পরিবর্তন করে ব্যবহার করা যায়।

text = "Hello World"
print(text.upper())
print(text[0:5])
print("world" in text)
print(text.replace("World", "Python"))


# 10. File Handling
# Theory: Reading and writing files.
# 🇧🇩 ফাইল থেকে পড়া ও লেখা করার জন্য open() ব্যবহার করা হয়।

with open("data.txt", "w") as file:
    file.write("Hello, Python!")

with open("data.txt", "r") as file:
    print(file.read())


# 11. Exception Handling
# Theory: Catch and handle runtime errors.
# 🇧🇩 ভুল ধরতে try-except ব্লক ব্যবহার করা হয়।

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 12. Modules and Packages
# Theory: Code organization using modules.
# 🇧🇩 Modules হলো একক Python ফাইল, Packages হলো মডিউল সমষ্টি।

import math
print(math.sqrt(16))


# 13. OOP – Classes and Objects
# Theory: Real-world modeling using classes.
# 🇧🇩 OOP দিয়ে বাস্তব জিনিসকে প্রোগ্রামে উপস্থাপন করা যায়।

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

p = Person("Noman")
print(p.greet())


# 14. Standard Libraries
# Theory: Python has powerful built-in libraries.
# 🇧🇩 Python-এর নিজস্ব অনেক দরকারি লাইব্রেরি আছে।

import random
print(random.randint(1, 10))
