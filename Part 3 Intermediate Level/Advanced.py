
# =====================================
# Advanced Python Concepts
# =====================================

# 1. Decorators
# Theory: Functions that modify the behavior of other functions.
# 🇧🇩 ডেকোরেটর দিয়ে ফাংশনের আচরণ পরিবর্তন করা যায়।

def decorator_func(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_func
def say_hello():
    print("Hello from decorated function!")

say_hello()


# 2. Generators
# Theory: Used to generate a sequence using yield (memory efficient).
# 🇧🇩 জেনারেটর দিয়ে একটি একটি করে মান তৈরি করা যায় যা মেমোরি সাশ্রয়ী।

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)


# 3. Iterators & Iterable Protocol
# Theory: Objects with __iter__() and __next__() methods.
# 🇧🇩 ইটারেটর এমন একটি অবজেক্ট যা নিজেই একে একে মান দেয়।

class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 3:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

nums = MyNumbers()
for x in nums:
    print(x)


# 4. Regular Expressions (re module)
# Theory: Pattern matching in strings.
# 🇧🇩 স্ট্রিং-এ নির্দিষ্ট প্যাটার্ন খুঁজতে Regular Expression ব্যবহার হয়।

import re
text = "My phone number is 01712345678"
match = re.search(r"01[0-9]{9}", text)
if match:
    print("Phone number found:", match.group())


# 5. Context Managers (with statement)
# Theory: Manages resources like files, locks using __enter__ and __exit__.
# 🇧🇩 Context Manager দিয়ে স্বয়ংক্রিয়ভাবে রিসোর্স ব্যবস্থাপনা করা যায়।

class MyContext:
    def __enter__(self):
        print("Entering context")
        return "Hello"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext() as val:
    print(val)


# 6. Virtual Environments
# Theory: Used to isolate Python environments for different projects.
# 🇧🇩 Virtual Environment দিয়ে আলাদা আলাদা প্রজেক্টের জন্য প্যাকেজ ব্যবস্থাপনা করা যায়।

# (No runnable code. Use: python -m venv env)


# 7. Type Hinting
# Theory: Optional annotations to improve readability and catch errors.
# 🇧🇩 টাইপ হিন্টিং কোড পড়া ও ভুল ধরতে সাহায্য করে।

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))


# 8. Unit Testing (unittest)
# Theory: Helps automate code testing.
# 🇧🇩 ইউনিট টেস্টিং দিয়ে স্বয়ংক্রিয়ভাবে কোড যাচাই করা যায়।

import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# To run: use `unittest.main()` in command-line context (not in notebook)


# 9. Multithreading
# Theory: Run tasks in parallel threads.
# 🇧🇩 মাল্টিথ্রেডিং দিয়ে একাধিক কাজ একসাথে চালানো যায়।

import threading

def print_numbers():
    for i in range(3):
        print("Number:", i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()


# 10. Working with APIs (requests)
# Theory: Used to fetch data from web services.
# 🇧🇩 API ব্যবহার করে ওয়েব থেকে ডেটা আনা যায়।

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.json())

# (Commented out to avoid online call)
