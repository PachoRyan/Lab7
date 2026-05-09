def greet(name: str) -> str:
    """Return a greeting message for the given name.

    Args:
        name: The name to greet.

    Returns:
        A string with the greeting message.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two integers and return the result.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum of a and b.
    """
    return a + b


def is_even(n: int) -> bool:
    """Check if a number is even.

    Args:
        n: The integer to check.

    Returns:
        True if n is even, False otherwise.
    """
    return n % 2 == 0


if __name__ == "__main__":
    print(greet("GitHub Actions"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 is even: {is_even(4)}")