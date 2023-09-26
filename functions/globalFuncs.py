PI = 3.141592653589793

def deg_to_rad(degrees: float) -> float:
    """
    Purpose: Converts degrees to radians
    Input: Float
    Output: Float
    """
    return degrees * PI/180

def rad_to_deg(radians: float) -> float:
    """
    Purpose: Converts radians to degrees
    Input: Float
    Output: Float
    """
    return radians * 180/PI

def factorial(n: float) -> float:
    """
    Purpose: Calculates the factorial of a number
    Input: Float
    Output: Float
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sort(numbers: list[float]) -> list[float]:
    """
    Purpose: Sorts numbers from least to greatest based on their values using the quicksort algoritm
    Input: Array of Floats
    Output: Array of Floats
    """
    if len(numbers) > 1:
        pivot = int(len(numbers) // 2)
        value = numbers[pivot]
        left = []
        right = []
        mid = []
        for i in numbers:
            if i > value:
                right.append(i)
            elif i < value:
                left.append(i)
            else:
                mid.append(i)
        res = sort(left) + mid + sort(right)
        return res
    else:
        return numbers

def sum(numbers: list[float]) -> float:
    """
    Purpose: Calculates the sum of an array of floats
    Input: Array of Floats
    Output: Float
    """
    total = 0
    for i in numbers:
        total += i
    return total

def diff(numbers: list[float]) -> float:
    """
    Purpose Calculates the difference of an array of floats
    Input: Array of Floats
    Output: Float
    """
    total = 0
    for i in numbers:
        total -= i
    return total

def prod(numbers: list[float]) -> float:
    """
    Purpose: Calculates the product of an array of floats
    Input: Array of Floats
    Output: Float
    """
    total = 0
    for i in numbers:
        total *= i
    return total

def quot(numbers: list[float]) -> float:
    """
    Purpose: Calculates the quotient of an array of floats
    Input: Array of Floats
    Output: Float
    """
    total = 0
    for i in numbers:
        total /= i
    return total

def sqrt(number: float) -> float:
    """
    Purpose: Calculate the square root of a float
    Input: Float
    Output: Float
    """
    return number ** 0.5

def abs(number: float) -> float:
    """
    Purpose: Calculate the absolute value of a float
    Input: Float
    Output: Float
    """
    if number >= 0:
        return number
    else:
        return -number