# =====================================
# Advanced Level: Expert Python Programming
# =====================================

"""
This file contains advanced Python concepts with detailed explanations
and practical examples. Topics include decorators, metaclasses, async programming,
advanced OOP, and professional development practices.
"""

# =====================================
# 1. Advanced Decorators
# =====================================
"""
Theory: Decorators are functions that modify the behavior of other functions
or classes. They're a powerful tool for code reuse and separation of concerns.
🇧🇩 ডেকোরেটর দিয়ে ফাংশনের আচরণ পরিবর্তন করা যায়।
"""

print("=== ADVANCED DECORATORS ===")

# Basic decorator
def simple_decorator(func):
    """A simple decorator that adds functionality."""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """A simple greeting function."""
    return f"Hello, {name}!"

print(greet("Noman"))

# Decorator with arguments
def repeat(times):
    """Decorator that repeats function execution."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    """Function that says hello."""
    return "Hello!"

print(f"Repeated function: {say_hello()}")

# Class-based decorator
class CountCalls:
    """Decorator that counts function calls."""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def calculate_square(x):
    """Calculate square of a number."""
    return x ** 2

print(f"Square of 5: {calculate_square(5)}")
print(f"Square of 3: {calculate_square(3)}")

# Property decorator
class Circle:
    """Circle class with property decorators."""
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Get radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Set radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Calculate area."""
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(f"Circle radius: {circle.radius}")
print(f"Circle area: {circle.area:.2f}")

# =====================================
# 2. Advanced Generators and Iterators
# =====================================
"""
Theory: Generators are memory-efficient iterators that yield values on demand.
They're essential for handling large datasets and creating custom iteration patterns.
🇧🇩 জেনারেটর দিয়ে একটি একটি করে মান তৈরি করা যায় যা মেমোরি সাশ্রয়ী।
"""

print("\n=== ADVANCED GENERATORS ===")

# Generator with send() method
def number_generator():
    """Generator that can receive values via send()."""
    while True:
        received = yield
        if received is not None:
            print(f"Received: {received}")
        yield received

gen = number_generator()
next(gen)  # Start the generator
gen.send(42)  # Send value to generator

# Generator expression with filtering
numbers = (x for x in range(100) if x % 2 == 0)
print(f"First 5 even numbers: {list(next(numbers) for _ in range(5))}")

# Custom iterator class
class FibonacciIterator:
    """Custom iterator for Fibonacci numbers."""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        
        if self.count == 0:
            result = self.a
        elif self.count == 1:
            result = self.b
        else:
            self.a, self.b = self.b, self.a + self.b
            result = self.b
        
        self.count += 1
        return result

fib_iter = FibonacciIterator(10)
print(f"Fibonacci numbers: {list(fib_iter)}")

# Generator for file processing
def process_large_file(filename):
    """Process large files line by line using generator."""
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                yield line_num, line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")

# =====================================
# 3. Metaclasses
# =====================================
"""
Theory: Metaclasses are classes whose instances are classes. They control
class creation and can modify class behavior at creation time.
🇧🇩 Metaclass হলো এমন ক্লাস যার instance হলো ক্লাস।
"""

print("\n=== METACLASSES ===")

# Simple metaclass
class SingletonMeta(type):
    """Metaclass that creates singleton classes."""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection singleton."""
    def __init__(self):
        self.connected = True
        print("Database connection created")

# Test singleton behavior
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")

# Metaclass for automatic method registration
class CommandMeta(type):
    """Metaclass that registers command methods."""
    def __new__(cls, name, bases, attrs):
        commands = {}
        for key, value in attrs.items():
            if callable(value) and key.startswith('cmd_'):
                commands[key[4:]] = value
        attrs['commands'] = commands
        return super().__new__(cls, name, bases, attrs)

class CommandProcessor(metaclass=CommandMeta):
    """Command processor with automatic registration."""
    
    def cmd_hello(self):
        return "Hello command executed"
    
    def cmd_goodbye(self):
        return "Goodbye command executed"
    
    def execute_command(self, cmd):
        if cmd in self.commands:
            return self.commands[cmd]()
        return f"Unknown command: {cmd}"

processor = CommandProcessor()
print(f"Available commands: {list(processor.commands.keys())}")
print(f"Execute hello: {processor.execute_command('hello')}")

# =====================================
# 4. Context Managers
# =====================================
"""
Theory: Context managers provide a way to manage resources using the 'with' statement.
They ensure proper setup and cleanup of resources.
🇧🇩 Context Manager দিয়ে স্বয়ংক্রিয়ভাবে রিসোর্স ব্যবস্থাপনা করা যায়।
"""

print("\n=== CONTEXT MANAGERS ===")

# Class-based context manager
class TimerContext:
    """Context manager for timing code execution."""
    def __init__(self, name="Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        import time
        self.start_time = time.time()
        print(f"Starting {self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end_time = time.time()
        duration = end_time - self.start_time
        print(f"{self.name} completed in {duration:.4f} seconds")
        
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Using the context manager
with TimerContext("Data Processing"):
    import time
    time.sleep(0.1)  # Simulate work
    print("Processing data...")

# Function-based context manager using contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Context manager for file operations."""
    file = None
    try:
        file = open(filename, mode)
        print(f"File {filename} opened")
        yield file
    except Exception as e:
        print(f"Error occurred: {e}")
        raise
    finally:
        if file:
            file.close()
            print(f"File {filename} closed")

# Using the file context manager
try:
    with file_manager("test.txt", "w") as f:
        f.write("Hello, World!")
except Exception as e:
    print(f"File operation failed: {e}")

# =====================================
# 5. Async Programming (asyncio)
# =====================================
"""
Theory: Asynchronous programming allows concurrent execution of tasks
without blocking the main thread. Essential for I/O-bound operations.
🇧🇩 Async programming দিয়ে একসাথে অনেক কাজ করা যায়।
"""

print("\n=== ASYNC PROGRAMMING ===")

import asyncio
import time

# Basic async function
async def fetch_data(url, delay):
    """Simulate fetching data from a URL."""
    print(f"Fetching data from {url}...")
    await asyncio.sleep(delay)  # Simulate network delay
    return f"Data from {url}"

# Async function with multiple tasks
async def main_async():
    """Main async function."""
    # Create multiple tasks
    tasks = [
        fetch_data("api1.com", 1),
        fetch_data("api2.com", 2),
        fetch_data("api3.com", 1.5)
    ]
    
    # Run tasks concurrently
    results = await asyncio.gather(*tasks)
    return results

# Run async function
async def run_async_example():
    """Run async example."""
    start_time = time.time()
    results = await main_async()
    end_time = time.time()
    
    print(f"Async results: {results}")
    print(f"Total time: {end_time - start_time:.2f} seconds")

# Note: In a real environment, you would run: asyncio.run(run_async_example())
print("Async programming example (would run with asyncio.run())")

# =====================================
# 6. Advanced OOP Concepts
# =====================================
"""
Theory: Advanced OOP includes abstract classes, multiple inheritance,
method resolution order, and design patterns.
🇧🇩 উন্নত OOP-এ abstract class, multiple inheritance ইত্যাদি আছে।
"""

print("\n=== ADVANCED OOP CONCEPTS ===")

# Abstract base class
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses."""
        pass
    
    def describe(self):
        """Common method for all shapes."""
        return f"This is a {self.name}"

class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implementation."""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Using abstract classes
shapes = [
    Rectangle(5, 3),
    Circle(4)
]

for shape in shapes:
    print(f"{shape.describe()}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

# Multiple inheritance
class Flyable:
    """Mixin for flying capability."""
    def fly(self):
        return f"{self.name} is flying"

class Swimmable:
    """Mixin for swimming capability."""
    def swim(self):
        return f"{self.name} is swimming"

class Duck(Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says quack!"

duck = Duck("Donald")
print(f"{duck.quack()}")
print(f"{duck.fly()}")
print(f"{duck.swim()}")

# Method Resolution Order (MRO)
print(f"Duck MRO: {Duck.__mro__}")

# =====================================
# 7. Design Patterns
# =====================================
"""
Theory: Design patterns are reusable solutions to common programming problems.
They provide templates for solving recurring design challenges.
🇧🇩 Design pattern হলো সাধারণ সমস্যার সমাধানের পুনরায় ব্যবহারযোগ্য টেমপ্লেট।
"""

print("\n=== DESIGN PATTERNS ===")

# Observer Pattern
class Subject:
    """Subject in Observer pattern."""
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        """Attach an observer."""
        self._observers.append(observer)
    
    def detach(self, observer):
        """Detach an observer."""
        self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, state):
        """Set state and notify observers."""
        self._state = state
        self.notify()
    
    def get_state(self):
        """Get current state."""
        return self._state

class Observer:
    """Observer interface."""
    def update(self, subject):
        """Update method to be implemented by concrete observers."""
        pass

class ConcreteObserver(Observer):
    """Concrete observer implementation."""
    def __init__(self, name):
        self.name = name
    
    def update(self, subject):
        print(f"{self.name} received update: {subject.get_state()}")

# Using Observer pattern
subject = Subject()
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("New state!")

# Factory Pattern
class AnimalFactory:
    """Factory for creating animals."""
    
    @staticmethod
    def create_animal(animal_type, name):
        """Create animal based on type."""
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Meow!"

# Using Factory pattern
dog = AnimalFactory.create_animal("dog", "Buddy")
cat = AnimalFactory.create_animal("cat", "Whiskers")

print(f"{dog.speak()}")
print(f"{cat.speak()}")

# =====================================
# 8. Advanced Data Processing
# =====================================
"""
Theory: Advanced data processing techniques including pandas-like operations,
data validation, and performance optimization.
🇧🇩 উন্নত ডেটা প্রসেসিং টেকনিক যেমন pandas-like operations।
"""

print("\n=== ADVANCED DATA PROCESSING ===")

# Data validation using decorators
def validate_data_types(**expected_types):
    """Decorator to validate function argument types."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            # Validate types
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"{param_name} must be {expected_type.__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_data_types(name=str, age=int, salary=float)
def create_employee(name, age, salary):
    """Create employee with type validation."""
    return {"name": name, "age": age, "salary": salary}

try:
    emp = create_employee("Noman", 25, 50000.0)
    print(f"Employee created: {emp}")
except TypeError as e:
    print(f"Validation error: {e}")

# Data processing pipeline
class DataPipeline:
    """Data processing pipeline."""
    
    def __init__(self):
        self.steps = []
    
    def add_step(self, func):
        """Add processing step."""
        self.steps.append(func)
        return self
    
    def process(self, data):
        """Process data through all steps."""
        result = data
        for step in self.steps:
            result = step(result)
        return result

# Using data pipeline
def filter_even(data):
    """Filter even numbers."""
    return [x for x in data if x % 2 == 0]

def square_numbers(data):
    """Square all numbers."""
    return [x ** 2 for x in data]

def sum_numbers(data):
    """Sum all numbers."""
    return sum(data)

pipeline = DataPipeline()
pipeline.add_step(filter_even).add_step(square_numbers).add_step(sum_numbers)

numbers = list(range(1, 11))
result = pipeline.process(numbers)
print(f"Pipeline result: {result}")

# =====================================
# 9. Memory Management and Optimization
# =====================================
"""
Theory: Understanding Python's memory management, garbage collection,
and optimization techniques for better performance.
🇧🇩 Python-এর মেমোরি ব্যবস্থাপনা ও অপ্টিমাইজেশন।
"""

print("\n=== MEMORY MANAGEMENT ===")

import sys
import gc
from weakref import WeakValueDictionary

# Memory usage tracking
def get_memory_usage():
    """Get current memory usage."""
    return sys.getsizeof(locals())

# Weak references
class Person:
    """Person class for weak reference example."""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person({self.name})"

# Weak value dictionary
weak_dict = WeakValueDictionary()

person1 = Person("Noman")
person2 = Person("Sarah")

weak_dict[1] = person1
weak_dict[2] = person2

print(f"Weak dict before deletion: {dict(weak_dict)}")

# Delete strong references
del person1
gc.collect()  # Force garbage collection

print(f"Weak dict after deletion: {dict(weak_dict)}")

# Memory-efficient data structures
class MemoryEfficientList:
    """Memory-efficient list implementation."""
    
    def __init__(self):
        self._data = []
        self._deleted_indices = set()
    
    def append(self, item):
        """Append item to list."""
        if self._deleted_indices:
            # Reuse deleted index
            index = self._deleted_indices.pop()
            self._data[index] = item
        else:
            self._data.append(item)
    
    def delete(self, index):
        """Delete item by index."""
        if 0 <= index < len(self._data):
            self._data[index] = None
            self._deleted_indices.add(index)
    
    def __getitem__(self, index):
        """Get item by index."""
        if index in self._deleted_indices:
            raise IndexError("Item has been deleted")
        return self._data[index]
    
    def __len__(self):
        """Get length excluding deleted items."""
        return len(self._data) - len(self._deleted_indices)

# Using memory-efficient list
mem_list = MemoryEfficientList()
mem_list.append("item1")
mem_list.append("item2")
mem_list.append("item3")

print(f"List length: {len(mem_list)}")
print(f"Item at index 0: {mem_list[0]}")

mem_list.delete(1)
print(f"List length after deletion: {len(mem_list)}")

# =====================================
# 10. Testing and Debugging
# =====================================
"""
Theory: Professional testing practices including unit testing,
integration testing, and debugging techniques.
🇧🇩 পেশাদার টেস্টিং ও ডিবাগিং টেকনিক।
"""

print("\n=== TESTING AND DEBUGGING ===")

import unittest
import logging

# Unit testing
class MathOperations:
    """Math operations for testing."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def factorial(self, n):
        """Calculate factorial."""
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

class TestMathOperations(unittest.TestCase):
    """Test cases for MathOperations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.math = MathOperations()
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(self.math.add(2, 3), 5)
        self.assertEqual(self.math.add(-1, 1), 0)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(self.math.divide(10, 2), 5)
        self.assertRaises(ValueError, self.math.divide, 10, 0)
    
    def test_factorial(self):
        """Test factorial."""
        self.assertEqual(self.math.factorial(5), 120)
        self.assertEqual(self.math.factorial(0), 1)
        self.assertRaises(ValueError, self.math.factorial, -1)

# Run tests
if __name__ == "__main__":
    unittest.main(verbosity=2)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def debug_function(func):
    """Decorator for debugging function calls."""
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} raised exception: {e}")
            raise
    return wrapper

@debug_function
def calculate_square(x):
    """Calculate square with debugging."""
    return x ** 2

# Test debugging
try:
    result = calculate_square(5)
    print(f"Square calculation result: {result}")
except Exception as e:
    print(f"Error occurred: {e}")

# =====================================
# 11. Professional Development Practices
# =====================================
"""
Theory: Professional development practices including code organization,
documentation, version control, and deployment considerations.
🇧🇩 পেশাদার ডেভেলপমেন্ট অনুশীলন।
"""

print("\n=== PROFESSIONAL DEVELOPMENT ===")

# Configuration management
class Config:
    """Configuration management class."""
    
    def __init__(self):
        self._config = {}
    
    def set(self, key, value):
        """Set configuration value."""
        self._config[key] = value
    
    def get(self, key, default=None):
        """Get configuration value."""
        return self._config.get(key, default)
    
    def load_from_dict(self, config_dict):
        """Load configuration from dictionary."""
        self._config.update(config_dict)
    
    def to_dict(self):
        """Convert to dictionary."""
        return self._config.copy()

# Using configuration
config = Config()
config.set("database_url", "postgresql://localhost:5432/mydb")
config.set("debug", True)
config.set("max_connections", 100)

print(f"Database URL: {config.get('database_url')}")
print(f"Debug mode: {config.get('debug')}")

# Error handling and recovery
class RobustCalculator:
    """Calculator with robust error handling."""
    
    def __init__(self):
        self.history = []
    
    def safe_divide(self, a, b):
        """Safe division with error handling."""
        try:
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result
        except ZeroDivisionError:
            self.history.append(f"{a} / {b} = Error: Division by zero")
            return None
        except Exception as e:
            self.history.append(f"{a} / {b} = Error: {e}")
            return None
    
    def get_history(self):
        """Get calculation history."""
        return self.history

# Using robust calculator
calc = RobustCalculator()
print(f"10 / 2 = {calc.safe_divide(10, 2)}")
print(f"10 / 0 = {calc.safe_divide(10, 0)}")
print(f"History: {calc.get_history()}")

# =====================================
# 12. Advanced Practice Projects
# =====================================
"""
Here are advanced practice projects to apply expert-level concepts:
"""

print("\n=== ADVANCED PRACTICE PROJECTS ===")

# Project 1: Web Scraper with Async
class AsyncWebScraper:
    """Async web scraper using advanced concepts."""
    
    def __init__(self):
        self.session = None
        self.results = []
    
    async def fetch_url(self, url):
        """Fetch URL content (simulated)."""
        import asyncio
        await asyncio.sleep(0.1)  # Simulate network delay
        return f"Content from {url}"
    
    async def scrape_urls(self, urls):
        """Scrape multiple URLs concurrently."""
        tasks = [self.fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Project 2: Caching System
class LRUCache:
    """Least Recently Used cache implementation."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_order = []
    
    def get(self, key):
        """Get value from cache."""
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        """Put value in cache."""
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                lru_key = self.access_order.pop(0)
                del self.cache[lru_key]
            
            self.cache[key] = value
            self.access_order.append(key)

# Using LRU Cache
cache = LRUCache(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)
cache.put("d", 4)  # This will evict "a"

print(f"Cache contents: {cache.cache}")
print(f"Get 'b': {cache.get('b')}")
print(f"Get 'a': {cache.get('a')}")  # Should return None

# Project 3: Plugin System
class PluginManager:
    """Plugin management system."""
    
    def __init__(self):
        self.plugins = {}
    
    def register_plugin(self, name, plugin_class):
        """Register a plugin."""
        self.plugins[name] = plugin_class()
    
    def execute_plugin(self, name, *args, **kwargs):
        """Execute a plugin."""
        if name in self.plugins:
            return self.plugins[name].execute(*args, **kwargs)
        else:
            raise ValueError(f"Plugin '{name}' not found")

class BasePlugin:
    """Base plugin class."""
    def execute(self, *args, **kwargs):
        """Execute plugin - to be overridden."""
        raise NotImplementedError

class GreetingPlugin(BasePlugin):
    """Greeting plugin."""
    def execute(self, name="World"):
        return f"Hello, {name}!"

class MathPlugin(BasePlugin):
    """Math plugin."""
    def execute(self, operation, a, b):
        if operation == "add":
            return a + b
        elif operation == "multiply":
            return a * b
        else:
            raise ValueError(f"Unknown operation: {operation}")

# Using plugin system
plugin_manager = PluginManager()
plugin_manager.register_plugin("greeting", GreetingPlugin)
plugin_manager.register_plugin("math", MathPlugin)

print(f"Greeting plugin: {plugin_manager.execute_plugin('greeting', 'Noman')}")
print(f"Math plugin: {plugin_manager.execute_plugin('math', 'add', 5, 3)}")

print("\n=== END OF ADVANCED LEVEL ===")
print("Congratulations! You've completed advanced Python programming.")
print("You're now ready for professional Python development!")
