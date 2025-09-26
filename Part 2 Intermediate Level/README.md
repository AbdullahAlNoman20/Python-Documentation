# Part 2: Intermediate Level Python Concepts

![Python Intermediate](https://img.shields.io/badge/Level-Intermediate-orange.svg)
![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

Welcome to the intermediate level of Python programming! This section builds upon the foundational concepts from Part 1 and introduces more advanced Python features and programming techniques.

## 📚 What You'll Learn

This intermediate level covers advanced concepts that will make you a more proficient Python programmer:

### Advanced Concepts
- **Advanced String Manipulation** - Master text processing techniques
- **Advanced Data Structures** - Work with specialized collections
- **List Comprehensions & Generators** - Write efficient, Pythonic code
- **File Handling & I/O Operations** - Process various file formats
- **Exception Handling & Error Management** - Build robust applications
- **Modules & Packages** - Organize and reuse code effectively
- **Object-Oriented Programming** - Design with classes and objects
- **Advanced Function Concepts** - Master decorators and closures
- **Data Structure Operations** - Advanced manipulation techniques
- **Regular Expressions** - Pattern matching and text processing
- **API Integration** - Work with web services and JSON data
- **Performance Optimization** - Write efficient Python code

## 🎯 Learning Objectives

By the end of this section, you will be able to:

✅ **Master advanced string operations and formatting**  
✅ **Use specialized data structures effectively**  
✅ **Write Pythonic code with comprehensions and generators**  
✅ **Handle files in multiple formats (JSON, CSV, text)**  
✅ **Implement robust error handling strategies**  
✅ **Organize code using modules and packages**  
✅ **Design object-oriented programs with inheritance**  
✅ **Use advanced function features like decorators**  
✅ **Process data with advanced operations**  
✅ **Apply regular expressions for text processing**  
✅ **Integrate with web APIs and services**  
✅ **Optimize code for better performance**  

## 📖 Table of Contents

1. [Advanced String Manipulation](#1-advanced-string-manipulation)
2. [Advanced Data Structures](#2-advanced-data-structures)
3. [List Comprehensions and Generators](#3-list-comprehensions-and-generators)
4. [File Handling and I/O Operations](#4-file-handling-and-io-operations)
5. [Exception Handling and Error Management](#5-exception-handling-and-error-management)
6. [Modules and Packages](#6-modules-and-packages)
7. [Object-Oriented Programming](#7-object-oriented-programming)
8. [Advanced Function Concepts](#8-advanced-function-concepts)
9. [Working with Data Structures](#9-working-with-data-structures)
10. [Regular Expressions](#10-regular-expressions)
11. [Working with APIs and JSON](#11-working-with-apis-and-json)
12. [Performance and Optimization](#12-performance-and-optimization)
13. [Practice Projects](#13-practice-projects)

## 🚀 Getting Started

### Prerequisites
- Completion of Part 1 or equivalent knowledge
- Understanding of basic Python syntax
- Familiarity with basic programming concepts
- Experience with variables, functions, and data structures

### Running the Code
```bash
# Navigate to the intermediate level directory
cd "Part 2 Intermediate Level"

# Run the intermediate examples
python Intermediate.py
```

## 📝 Detailed Topics

### 1. Advanced String Manipulation
Master sophisticated text processing techniques.

**Key Points:**
- String methods (strip, upper, lower, title, capitalize)
- String slicing and indexing
- String formatting (f-strings, format method, % formatting)
- String validation and checking
- Text cleaning and normalization

**Example:**
```python
text = "  Hello World!  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Upper: '{text.upper()}'")
print(f"Title: '{text.title()}'")

# Advanced formatting
name = "Noman"
age = 25
salary = 50000.50
info = f"Name: {name}, Age: {age}, Salary: ${salary:,.2f}"
print(info)
```

### 2. Advanced Data Structures
Work with specialized collections for specific use cases.

**Key Points:**
- defaultdict: Provides default values for missing keys
- Counter: Counts occurrences of elements
- OrderedDict: Maintains insertion order
- deque: Double-ended queue operations

**Example:**
```python
from collections import defaultdict, Counter, OrderedDict, deque

# defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')

# Counter
text = "hello world"
counter = Counter(text)
print(f"Character count: {counter}")
print(f"Most common 3: {counter.most_common(3)}")

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to left
dq.append(4)      # Add to right
```

### 3. List Comprehensions and Generators
Write efficient, Pythonic code for data processing.

**Key Points:**
- List comprehensions with conditions
- Dictionary and set comprehensions
- Generator expressions
- Memory-efficient iteration
- Generator functions with yield

**Example:**
```python
# List comprehension
squares = [x**2 for x in range(1, 6)]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}

# Generator function
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator(20)
print(f"Fibonacci numbers: {list(fib_gen)}")
```

### 4. File Handling and I/O Operations
Process various file formats and handle data persistence.

**Key Points:**
- JSON file operations
- CSV file processing
- File existence and size checking
- Context managers for file handling
- Error handling in file operations

**Example:**
```python
import json
import csv

# JSON operations
sample_data = {
    "students": [
        {"name": "Noman", "age": 25, "grade": "A"},
        {"name": "Sarah", "age": 23, "grade": "B"}
    ]
}

# Write JSON
with open("students.json", "w") as file:
    json.dump(sample_data, file, indent=2)

# Read JSON
with open("students.json", "r") as file:
    loaded_data = json.load(file)
    print(f"Loaded data: {loaded_data}")
```

### 5. Exception Handling and Error Management
Build robust applications with comprehensive error handling.

**Key Points:**
- Custom exception classes
- Multiple exception handling
- try-except-finally blocks
- Context managers for error handling
- Error logging and reporting

**Example:**
```python
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide_numbers(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Division error: {e}")
        return None
    finally:
        print("Division operation completed")
```

### 6. Modules and Packages
Organize code effectively using Python's module system.

**Key Points:**
- Import statements and aliasing
- Module creation and organization
- Package structure and __init__.py
- Standard library modules
- Third-party package management

**Example:**
```python
import math
import random
import datetime
from pathlib import Path

# Math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi value: {math.pi}")

# Random module
print(f"Random integer: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'orange'])}")

# Path module
current_path = Path.cwd()
print(f"Current directory: {current_path}")
```

### 7. Object-Oriented Programming
Design programs using classes and objects.

**Key Points:**
- Class definition and instantiation
- Inheritance and method overriding
- Encapsulation with private attributes
- Polymorphism and method resolution
- Abstract base classes

**Example:**
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._energy = 100  # Protected attribute
    
    def eat(self, food):
        self._energy += 10
        return f"{self.name} ate {food} and gained energy"
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def bark(self):
        return f"{self.name} barks: Woof! Woof!"

# Using classes
dog = Dog("Buddy", "Golden Retriever")
print(dog)
print(dog.bark())
```

### 8. Advanced Function Concepts
Master advanced function features and patterns.

**Key Points:**
- Variable arguments (*args, **kwargs)
- Closures and nested functions
- Decorators and decorator patterns
- Function annotations and type hints
- Lambda functions and functional programming

**Example:**
```python
# Variable arguments
def calculate_sum(*args, **kwargs):
    total = sum(args)
    print(f"Sum of {args}: {total}")
    print(f"Keyword arguments: {kwargs}")
    return total

# Closure
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
print(f"Double 5: {double(5)}")

# Decorator
def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper
```

### 9. Working with Data Structures
Master advanced operations on data structures.

**Key Points:**
- Sorting and filtering operations
- Mapping and transformation
- Reduce operations
- Advanced dictionary operations
- Nested data structure handling

**Example:**
```python
from functools import reduce

numbers = [64, 34, 25, 12, 22, 11, 90, 5]

# Sorting
sorted_numbers = sorted(numbers)
print(f"Sorted: {sorted_numbers}")

# Filtering
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Mapping
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled_numbers}")

# Reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_of_numbers}")
```

### 10. Regular Expressions
Master pattern matching and text processing.

**Key Points:**
- Basic pattern matching
- Character classes and quantifiers
- Groups and capturing
- Substitution and replacement
- Validation patterns

**Example:**
```python
import re

text = "My phone number is 01712345678 and email is noman@example.com"
phone_pattern = r"01[0-9]{9}"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

phone_match = re.search(phone_pattern, text)
email_match = re.search(email_pattern, text)

if phone_match:
    print(f"Phone number found: {phone_match.group()}")
if email_match:
    print(f"Email found: {email_match.group()}")

# Validation function
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))
```

### 11. Working with APIs and JSON
Integrate with web services and process JSON data.

**Key Points:**
- JSON data processing
- API response handling
- Data validation and error handling
- Pagination and data extraction
- API integration patterns

**Example:**
```python
import json

# Sample API response
api_response = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Noman", "email": "noman@example.com"},
            {"id": 2, "name": "Sarah", "email": "sarah@example.com"}
        ],
        "total": 2
    }
}

# Process JSON data
if api_response["status"] == "success":
    users = api_response["data"]["users"]
    print(f"Total users: {api_response['data']['total']}")
    
    for user in users:
        print(f"User {user['id']}: {user['name']} ({user['email']})")
```

### 12. Performance and Optimization
Write efficient Python code.

**Key Points:**
- Time complexity analysis
- Memory usage optimization
- Efficient data structure selection
- Algorithm optimization
- Profiling and benchmarking

**Example:**
```python
import time

def slow_approach():
    result = ""
    for i in range(1000):
        result += str(i)
    return result

def fast_approach():
    result = []
    for i in range(1000):
        result.append(str(i))
    return "".join(result)

# Measure execution time
start_time = time.time()
slow_approach()
slow_time = time.time() - start_time

start_time = time.time()
fast_approach()
fast_time = time.time() - start_time

print(f"Slow approach: {slow_time:.4f} seconds")
print(f"Fast approach: {fast_time:.4f} seconds")
print(f"Speed improvement: {slow_time/fast_time:.2f}x faster")
```

## 🎯 Practice Projects

### Project 1: Student Management System
Build a comprehensive system to manage student information.

**Features:**
- Add/remove students
- Track subjects and grades
- Generate reports
- Data persistence

### Project 2: Text Analyzer
Create a tool for analyzing text documents.

**Features:**
- Word and character counting
- Most common words analysis
- Sentence counting
- Text statistics

### Project 3: API Data Processor
Build a system to fetch and process data from APIs.

**Features:**
- API integration
- Data validation
- Error handling
- Data transformation

### Project 4: File Organizer
Create a tool to organize files based on various criteria.

**Features:**
- File type detection
- Automatic organization
- Batch processing
- Configuration management

## 💡 Best Practices

1. **Write Clean Code**: Follow PEP 8 style guidelines
2. **Use Type Hints**: Improve code readability and catch errors
3. **Handle Errors Gracefully**: Implement comprehensive error handling
4. **Document Your Code**: Write clear docstrings and comments
5. **Test Your Code**: Implement unit tests for your functions
6. **Optimize Performance**: Profile and optimize critical code paths
7. **Use Design Patterns**: Apply appropriate design patterns
8. **Version Control**: Use Git for version control

## 🔗 Additional Resources

- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Design Patterns](https://python-patterns.guide/)
- [Real Python](https://realpython.com/)
- [Python Weekly](https://www.pythonweekly.com/)

## 🎓 Next Steps

After completing this intermediate level, you're ready to move on to:

**[Part 3: Advanced Level](../Part%203%20Intermediate%20Level/README.md)**

The advanced level will cover:
- Advanced decorators and metaclasses
- Async programming and concurrency
- Advanced OOP concepts
- Design patterns
- Memory management
- Professional development practices
- And much more!

## 🤝 Getting Help

If you encounter any issues or have questions:

1. **Check Documentation**: Refer to Python's official documentation
2. **Debug Step by Step**: Use print statements and debuggers
3. **Search Online**: Look for solutions on Stack Overflow
4. **Join Communities**: Participate in Python forums and groups
5. **Practice More**: Build projects to reinforce learning

## 📊 Progress Tracking

Track your learning progress:

- [ ] Mastered Advanced String Manipulation
- [ ] Learned Advanced Data Structures
- [ ] Understood List Comprehensions and Generators
- [ ] Implemented File Handling and I/O Operations
- [ ] Built Robust Exception Handling
- [ ] Organized Code with Modules and Packages
- [ ] Designed Object-Oriented Programs
- [ ] Used Advanced Function Concepts
- [ ] Applied Advanced Data Structure Operations
- [ ] Mastered Regular Expressions
- [ ] Integrated with APIs and JSON
- [ ] Optimized Code Performance
- [ ] Completed Practice Projects

## 🏆 Intermediate Level Achievements

Upon completion, you'll have:

- **Advanced Python Skills**: Mastery of intermediate Python concepts
- **Problem-Solving Ability**: Skills to tackle complex programming challenges
- **Code Organization**: Ability to structure and organize large codebases
- **Error Handling**: Robust error management strategies
- **API Integration**: Skills to work with external services
- **Performance Awareness**: Understanding of code optimization

---

## 🎉 Congratulations!

You've completed the intermediate level of Python programming! You now have advanced Python skills and are ready to tackle expert-level concepts.

**Keep pushing forward! 🐍✨**

---

<div align="center">
  <p>Ready for expert-level Python?</p>
  <a href="../Part%203%20Intermediate%20Level/README.md">
    <img src="https://img.shields.io/badge/Next-Part%203%20Advanced-red.svg" alt="Next: Advanced Level">
  </a>
</div>
