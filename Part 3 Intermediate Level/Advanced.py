
# =====================================
# Advanced Python Concepts - Extended Examples
# =====================================

"""
This file contains extended examples of advanced Python concepts
with more detailed implementations and real-world applications.
"""

# =====================================
# 1. Advanced Decorators with Parameters
# =====================================
"""
Theory: Decorators can accept parameters and be used for caching,
logging, authentication, and more advanced use cases.
🇧🇩 ডেকোরেটর দিয়ে ফাংশনের আচরণ পরিবর্তন করা যায়।
"""

print("=== ADVANCED DECORATORS ===")

# Caching decorator
def cache_result(func):
    """Decorator to cache function results."""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"Cache hit for {func.__name__}")
            return cache[key]
        
        print(f"Cache miss for {func.__name__}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

@cache_result
def expensive_calculation(n):
    """Simulate expensive calculation."""
    import time
    time.sleep(0.1)  # Simulate work
    return n ** 2

print(f"First call: {expensive_calculation(5)}")
print(f"Second call: {expensive_calculation(5)}")  # Should use cache

# Rate limiting decorator
def rate_limit(calls_per_second):
    """Decorator to limit function call rate."""
    import time
    last_called = [0.0]
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = 1.0 / calls_per_second - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kwargs)
            last_called[0] = time.time()
            return ret
        return wrapper
    return decorator

@rate_limit(2)  # Max 2 calls per second
def api_call():
    """Simulate API call."""
    print("API call made")

# Test rate limiting
for i in range(3):
    api_call()

# =====================================
# 2. Advanced Generators and Coroutines
# =====================================
"""
Theory: Generators can be used as coroutines with send(), throw(), and close()
methods for more advanced control flow.
🇧🇩 জেনারেটর দিয়ে একটি একটি করে মান তৈরি করা যায় যা মেমোরি সাশ্রয়ী।
"""

print("\n=== ADVANCED GENERATORS ===")

# Generator as coroutine
def number_processor():
    """Generator that processes numbers as a coroutine."""
    result = None
    while True:
        received = yield result
        if received is not None:
            if isinstance(received, int):
                result = received * 2
            elif isinstance(received, str):
                result = received.upper()
            else:
                result = f"Processed: {received}"

# Using coroutine
processor = number_processor()
next(processor)  # Start the coroutine

print(f"Processed 5: {processor.send(5)}")
print(f"Processed 'hello': {processor.send('hello')}")
print(f"Processed [1,2,3]: {processor.send([1,2,3])}")

# Generator pipeline
def source():
    """Data source generator."""
    for i in range(1, 11):
        yield i

def filter_even(gen):
    """Filter even numbers."""
    for item in gen:
        if item % 2 == 0:
            yield item

def square(gen):
    """Square numbers."""
    for item in gen:
        yield item ** 2

# Create pipeline
pipeline = square(filter_even(source()))
print(f"Pipeline result: {list(pipeline)}")

# =====================================
# 3. Custom Iterators and Iterables
# =====================================
"""
Theory: Custom iterators provide fine-grained control over iteration
and can implement complex iteration patterns.
🇧🇩 ইটারেটর এমন একটি অবজেক্ট যা নিজেই একে একে মান দেয়।
"""

print("\n=== CUSTOM ITERATORS ===")

# Custom iterator with state
class FibonacciIterator:
    """Custom Fibonacci iterator with configurable start values."""
    
    def __init__(self, max_count, a=0, b=1):
        self.max_count = max_count
        self.count = 0
        self.a = a
        self.b = b
    
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

# Using custom iterator
fib_iter = FibonacciIterator(10)
print(f"Fibonacci sequence: {list(fib_iter)}")

# Iterator with custom behavior
class RangeIterator:
    """Custom range iterator with step and reverse support."""
    
    def __init__(self, start, stop, step=1, reverse=False):
        self.start = start
        self.stop = stop
        self.step = step
        self.reverse = reverse
        self.current = start if not reverse else stop - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.reverse:
            if self.current < self.start:
                raise StopIteration
            result = self.current
            self.current -= self.step
        else:
            if self.current >= self.stop:
                raise StopIteration
            result = self.current
            self.current += self.step
        
        return result

# Using custom range iterator
custom_range = RangeIterator(1, 10, 2)
print(f"Custom range: {list(custom_range)}")

reverse_range = RangeIterator(1, 10, 2, reverse=True)
print(f"Reverse range: {list(reverse_range)}")

# =====================================
# 4. Advanced Regular Expressions
# =====================================
"""
Theory: Regular expressions can be used for complex text processing,
validation, and transformation tasks.
🇧🇩 স্ট্রিং-এ নির্দিষ্ট প্যাটার্ন খুঁজতে Regular Expression ব্যবহার হয়।
"""

print("\n=== ADVANCED REGULAR EXPRESSIONS ===")

import re

# Complex pattern matching
def extract_phone_numbers(text):
    """Extract phone numbers from text."""
    # Pattern for various phone number formats
    patterns = [
        r'\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})',  # US format
        r'01[0-9]{9}',  # Bangladeshi format
        r'\+880[0-9]{10}',  # International Bangladeshi format
    ]
    
    phone_numbers = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        phone_numbers.extend(matches)
    
    return phone_numbers

# Test phone number extraction
text_with_phones = """
Contact us at 01712345678 or +8801712345678.
US number: (555) 123-4567 or 555.123.4567
"""
phones = extract_phone_numbers(text_with_phones)
print(f"Extracted phone numbers: {phones}")

# Text transformation with regex
def clean_text(text):
    """Clean and normalize text."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters except basic punctuation
    text = re.sub(r'[^\w\s.,!?]', '', text)
    # Normalize case
    text = text.lower()
    return text.strip()

sample_text = "  Hello!!!   World...   How are you???  "
cleaned = clean_text(sample_text)
print(f"Original: '{sample_text}'")
print(f"Cleaned: '{cleaned}'")

# Advanced regex with named groups
def parse_log_entry(log_line):
    """Parse log entry with named groups."""
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (?P<level>\w+) - (?P<message>.*)'
    match = re.match(pattern, log_line)
    
    if match:
        return match.groupdict()
    return None

log_line = "2024-01-15 10:30:45 - ERROR - Database connection failed"
parsed = parse_log_entry(log_line)
print(f"Parsed log: {parsed}")

# =====================================
# 5. Advanced Context Managers
# =====================================
"""
Theory: Context managers can be used for resource management,
transaction handling, and more complex scenarios.
🇧🇩 Context Manager দিয়ে স্বয়ংক্রিয়ভাবে রিসোর্স ব্যবস্থাপনা করা যায়।
"""

print("\n=== ADVANCED CONTEXT MANAGERS ===")

# Database transaction context manager
class DatabaseTransaction:
    """Context manager for database transactions."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.transaction_started = False
    
    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        print("Starting transaction")
        self.transaction_started = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Rolling back transaction due to error")
            print(f"Error: {exc_val}")
        else:
            print("Committing transaction")
        
        print("Closing database connection")
        self.connection = None
        return False  # Don't suppress exceptions
    
    def execute_query(self, query):
        """Execute a database query."""
        if not self.transaction_started:
            raise RuntimeError("Transaction not started")
        print(f"Executing query: {query}")
        return f"Result of: {query}"

# Using database transaction
with DatabaseTransaction("myapp_db") as db:
    db.execute_query("SELECT * FROM users")
    db.execute_query("UPDATE users SET last_login = NOW()")
    # Uncomment next line to test error handling
    # raise Exception("Simulated error")

# Resource pooling context manager
class ResourcePool:
    """Context manager for resource pooling."""
    
    def __init__(self, pool_size=3):
        self.pool_size = pool_size
        self.available_resources = list(range(pool_size))
        self.used_resources = set()
    
    def __enter__(self):
        if not self.available_resources:
            raise RuntimeError("No resources available")
        
        resource_id = self.available_resources.pop()
        self.used_resources.add(resource_id)
        print(f"Acquired resource {resource_id}")
        return resource_id
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Return resource to pool
        if hasattr(self, '_resource_id'):
            self.available_resources.append(self._resource_id)
            self.used_resources.remove(self._resource_id)
            print(f"Released resource {self._resource_id}")

# Using resource pool
pool = ResourcePool(2)

with pool as resource1:
    print(f"Using resource {resource1}")
    with pool as resource2:
        print(f"Using resource {resource2}")

# =====================================
# 6. Virtual Environments and Package Management
# =====================================
"""
Theory: Virtual environments isolate Python environments for different projects.
Package management ensures consistent dependencies across environments.
🇧🇩 Virtual Environment দিয়ে আলাদা আলাদা প্রজেক্টের জন্য প্যাকেজ ব্যবস্থাপনা করা যায়।
"""

print("\n=== VIRTUAL ENVIRONMENTS ===")

# Simulate virtual environment management
class VirtualEnvironment:
    """Simulate virtual environment operations."""
    
    def __init__(self, name):
        self.name = name
        self.packages = {}
        self.python_version = "3.9.0"
    
    def install_package(self, package_name, version="latest"):
        """Install a package in the virtual environment."""
        self.packages[package_name] = version
        print(f"Installed {package_name} version {version}")
    
    def uninstall_package(self, package_name):
        """Uninstall a package from the virtual environment."""
        if package_name in self.packages:
            del self.packages[package_name]
            print(f"Uninstalled {package_name}")
        else:
            print(f"Package {package_name} not found")
    
    def list_packages(self):
        """List all installed packages."""
        print(f"Packages in {self.name}:")
        for package, version in self.packages.items():
            print(f"  {package}=={version}")
    
    def freeze_requirements(self):
        """Generate requirements.txt content."""
        requirements = []
        for package, version in self.packages.items():
            requirements.append(f"{package}=={version}")
        return "\n".join(requirements)

# Using virtual environment
venv = VirtualEnvironment("my_project")
venv.install_package("requests", "2.28.0")
venv.install_package("numpy", "1.21.0")
venv.install_package("pandas", "1.3.0")

venv.list_packages()
print(f"\nRequirements.txt:\n{venv.freeze_requirements()}")

# =====================================
# 7. Advanced Type Hinting
# =====================================
"""
Theory: Type hints improve code readability and enable static type checking.
Advanced type hints include generics, unions, and more complex types.
🇧🇩 টাইপ হিন্টিং কোড পড়া ও ভুল ধরতে সাহায্য করে।
"""

print("\n=== ADVANCED TYPE HINTING ===")

from typing import List, Dict, Optional, Union, Callable, TypeVar, Generic

# Generic types
T = TypeVar('T')

class Stack(Generic[T]):
    """Generic stack implementation."""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """Push item onto stack."""
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        """Pop item from stack."""
        if self._items:
            return self._items.pop()
        return None
    
    def peek(self) -> Optional[T]:
        """Peek at top item."""
        if self._items:
            return self._items[-1]
        return None
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0

# Using generic stack
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(f"Popped: {int_stack.pop()}")

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")
print(f"Peeked: {str_stack.peek()}")

# Union types and optional
def process_data(data: Union[str, int, List[str]]) -> Optional[str]:
    """Process different types of data."""
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, int):
        return str(data)
    elif isinstance(data, list):
        return ", ".join(data)
    return None

print(f"Processed string: {process_data('hello')}")
print(f"Processed int: {process_data(42)}")
print(f"Processed list: {process_data(['a', 'b', 'c'])}")

# Callable types
def apply_function(func: Callable[[int], int], value: int) -> int:
    """Apply a function to a value."""
    return func(value)

def square(x: int) -> int:
    return x ** 2

def double(x: int) -> int:
    return x * 2

print(f"Square of 5: {apply_function(square, 5)}")
print(f"Double of 5: {apply_function(double, 5)}")

# =====================================
# 8. Advanced Unit Testing
# =====================================
"""
Theory: Advanced testing includes mocking, fixtures, parameterized tests,
and integration testing strategies.
🇧🇩 ইউনিট টেস্টিং দিয়ে স্বয়ংক্রিয়ভাবে কোড যাচাই করা যায়।
"""

print("\n=== ADVANCED UNIT TESTING ===")

import unittest
from unittest.mock import Mock, patch, MagicMock

class AdvancedMath:
    """Advanced math operations for testing."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        result = a + b
        self.history.append(f"add({a}, {b}) = {result}")
        return result
    
    def divide(self, a: int, b: int) -> float:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"divide({a}, {b}) = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """Get calculation history."""
        return self.history.copy()

class TestAdvancedMath(unittest.TestCase):
    """Advanced test cases for AdvancedMath."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.math = AdvancedMath()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.math.add(2, 3)
        self.assertEqual(result, 5)
        self.assertIn("add(2, 3) = 5", self.math.get_history())
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.math.add(-1, -2)
        self.assertEqual(result, -3)
    
    def test_divide_normal_case(self):
        """Test division in normal case."""
        result = self.math.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ValueError):
            self.math.divide(10, 0)
    
    def test_history_tracking(self):
        """Test that history is properly tracked."""
        self.math.add(1, 2)
        self.math.divide(6, 2)
        
        history = self.math.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("add(1, 2) = 3", history)
        self.assertIn("divide(6, 2) = 3.0", history)

# Mock testing
class TestWithMocks(unittest.TestCase):
    """Test cases using mocks."""
    
    def test_mock_external_service(self):
        """Test with mocked external service."""
        # Create a mock object
        mock_service = Mock()
        mock_service.get_data.return_value = {"status": "success", "data": [1, 2, 3]}
        
        # Use the mock
        result = mock_service.get_data()
        self.assertEqual(result["status"], "success")
        self.assertEqual(len(result["data"]), 3)
        
        # Verify the mock was called
        mock_service.get_data.assert_called_once()
    
    @patch('builtins.print')
    def test_print_mocking(self, mock_print):
        """Test with mocked print function."""
        def greet(name):
            print(f"Hello, {name}!")
        
        greet("World")
        
        # Verify print was called with correct arguments
        mock_print.assert_called_once_with("Hello, World!")

# Run tests
if __name__ == "__main__":
    unittest.main(verbosity=2)

# =====================================
# 9. Advanced Multithreading and Concurrency
# =====================================
"""
Theory: Advanced concurrency includes thread pools, synchronization primitives,
and coordination between threads.
🇧🇩 মাল্টিথ্রেডিং দিয়ে একাধিক কাজ একসাথে চালানো যায়।
"""

print("\n=== ADVANCED MULTITHREADING ===")

import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor, as_completed

# Thread-safe counter
class ThreadSafeCounter:
    """Thread-safe counter using locks."""
    
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        """Increment counter safely."""
        with self._lock:
            self._value += 1
    
    def get_value(self):
        """Get current counter value."""
        with self._lock:
            return self._value

# Using thread-safe counter
counter = ThreadSafeCounter()

def worker(counter, iterations):
    """Worker function that increments counter."""
    for _ in range(iterations):
        counter.increment()
        time.sleep(0.001)  # Simulate work

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(counter, 10))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter.get_value()}")

# Thread pool executor
def fetch_url(url):
    """Simulate fetching URL."""
    time.sleep(0.1)  # Simulate network delay
    return f"Data from {url}"

urls = [f"http://example.com/page{i}" for i in range(5)]

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit all tasks
    futures = [executor.submit(fetch_url, url) for url in urls]
    
    # Process completed tasks
    for future in as_completed(futures):
        result = future.result()
        print(f"Completed: {result}")

# Producer-Consumer pattern
def producer(queue, items):
    """Producer function."""
    for item in items:
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(0.1)
    
    # Signal end of production
    queue.put(None)

def consumer(queue, name):
    """Consumer function."""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumer {name} consumed: {item}")
        time.sleep(0.1)
        queue.task_done()

# Using producer-consumer
q = queue.Queue()
items = [f"item_{i}" for i in range(5)]

# Start producer
producer_thread = threading.Thread(target=producer, args=(q, items))
producer_thread.start()

# Start consumers
consumer_threads = []
for i in range(2):
    consumer_thread = threading.Thread(target=consumer, args=(q, i))
    consumer_threads.append(consumer_thread)
    consumer_thread.start()

# Wait for completion
producer_thread.join()
for thread in consumer_threads:
    thread.join()

# =====================================
# 10. Working with APIs and Web Services
# =====================================
"""
Theory: Advanced API integration includes authentication, rate limiting,
error handling, and data processing.
🇧🇩 API ব্যবহার করে ওয়েব থেকে ডেটা আনা যায়।
"""

print("\n=== ADVANCED API WORKING ===")

import json
import time
from urllib.parse import urlencode

class APIClient:
    """Advanced API client with authentication and rate limiting."""
    
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.rate_limit_delay = 1  # seconds between requests
        self.last_request_time = 0
    
    def _rate_limit(self):
        """Implement rate limiting."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - time_since_last
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def _make_request(self, endpoint, params=None):
        """Make API request with error handling."""
        self._rate_limit()
        
        # Simulate API request
        url = f"{self.base_url}/{endpoint}"
        if params:
            url += "?" + urlencode(params)
        
        # Simulate response
        response_data = {
            "status": "success",
            "data": f"Mock data from {endpoint}",
            "timestamp": time.time()
        }
        
        return response_data
    
    def get_users(self, page=1, limit=10):
        """Get users from API."""
        params = {"page": page, "limit": limit}
        return self._make_request("users", params)
    
    def get_user(self, user_id):
        """Get specific user from API."""
        return self._make_request(f"users/{user_id}")
    
    def create_user(self, user_data):
        """Create new user via API."""
        # Simulate POST request
        response = self._make_request("users")
        response["data"] = f"Created user: {user_data}"
        return response

# Using API client
api_client = APIClient("https://api.example.com", "your-api-key")

# Get users
users_response = api_client.get_users(page=1, limit=5)
print(f"Users response: {users_response}")

# Get specific user
user_response = api_client.get_user(123)
print(f"User response: {user_response}")

# Create user
new_user = {"name": "Noman", "email": "noman@example.com"}
create_response = api_client.create_user(new_user)
print(f"Create response: {create_response}")

# API response processing
class APIResponseProcessor:
    """Process API responses and handle errors."""
    
    @staticmethod
    def process_response(response):
        """Process API response."""
        if response["status"] == "success":
            return response["data"]
        else:
            raise Exception(f"API error: {response.get('error', 'Unknown error')}")
    
    @staticmethod
    def extract_pagination_info(response):
        """Extract pagination information."""
        return {
            "page": response.get("page", 1),
            "total_pages": response.get("total_pages", 1),
            "total_items": response.get("total_items", 0)
        }

# Using response processor
processor = APIResponseProcessor()
try:
    processed_data = processor.process_response(users_response)
    print(f"Processed data: {processed_data}")
    
    pagination = processor.extract_pagination_info(users_response)
    print(f"Pagination info: {pagination}")
except Exception as e:
    print(f"Error processing response: {e}")

print("\n=== END OF ADVANCED CONCEPTS ===")
print("You've mastered advanced Python concepts!")
print("These examples demonstrate professional-level Python programming.")
