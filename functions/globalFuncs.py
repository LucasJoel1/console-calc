PI = 3.141592653589793

def deg_to_rad(degrees: float) -> float:
    return degrees * PI/180

def rad_to_deg(radians: float) -> float:
    return radians * 180/PI

def factorial(n: float) -> float:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sort(numbers: list[float]) -> list[float]:
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
    total = 0
    for i in numbers:
        total += i
    return total

def diff(numbers: list[float]) -> float:
    total = 0
    for i in numbers:
        total -= i
    return total

def prod(numbers: list[float]) -> float:
    total = 0
    for i in numbers:
        total *= i
    return total

def quot(numbers: list[float]) -> float:
    total = 0
    for i in numbers:
        total /= i
    return total