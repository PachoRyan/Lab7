# Hello Project

A simple Python project demonstrating basic functions and testing.

## Features

- `greet(name)`: Returns a greeting message.
- `add(a, b)`: Adds two integers.
- `is_even(n)`: Checks if a number is even.

## Installation

```bash
pip install -r requirements.txt
```

## Testing

```bash
pytest
```

## Usage

```python
from hello import greet, add, is_even

print(greet("World"))  # Hello, World!
print(add(2, 3))       # 5
print(is_even(4))      # True
```