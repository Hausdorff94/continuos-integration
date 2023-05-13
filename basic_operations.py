def mysum(a: int, b: int) -> int:
    """
    This function returns the sum of two numbers

    Parameters:
    a: int
    b: int

    Returns:
    int
    """
    return a + b


def sub(a: int, b: int) -> int:
    """
    This function returns the difference of two numbers

    Parameters:
    a: int
    b: int

    Returns:
    int
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    This function returns the product of two numbers

    Parameters:
    a: int
    b: int

    Returns:
    int
    """
    return a * b


def div(a: int, b: int) -> float:
    """
    This function returns the division of two numbers

    Parameters:
    a: int
    b: int

    Returns:
    float
    """
    if b == 0:
        return "Error: Division by zero"

    return a / b
