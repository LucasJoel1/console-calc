from functions.globalFuncs import *


# uses Taylor series to calculate sin and cos https://en.wikipedia.org/wiki/Taylor_series#Trigonometric_functions
# then uses sin and cos to calculate tan, csc, sec, and cot using trig identities

def sin_degrees(degrees: float) -> float:
    # convert degrees to radians
    radians = deg_to_rad(degrees)
    result = 0
    sign = 1
    # run the taylor series 10 times the step is set to two because the taylor series is alternating
    for i in range(1, 21, 2):
        result += sign * (radians ** i) / factorial(i)
        # changes the sign of the next term for either addition or subtraction
        sign *= -1
    return result

# same as above but takes radians instead of degrees so no conversion is needed
def sin_radians(radians: float) -> float:
    result = 0
    sign = 1
    for i in range(1, 21, 2):
        result += sign * (radians ** i) / factorial(i)
        sign *= -1
    return result

# same as above but cos is calculated with i being even instead of odd
def cos_degrees(degrees: float) -> float:
    radians = deg_to_rad(degrees)
    result = 0
    sign = 1
    for i in range(0, 20, 2):
        result += sign * (radians ** i) / factorial(i)
        sign *= -1
    return result

def cos_radians(radians: float) -> float:
    result = 0
    sign = 1
    for i in range(0, 20, 2):
        result += sign * (radians ** i) / factorial(i)
        sign *= -1
    return result

# uses different trig identities to calculate tan, csc, sec, and cot
# tan = sin / cos
# csc = 1 / sin
# sec = 1 / cos
# cot = 1 / tan
def tan_degrees(degrees: float) -> float:
    try :
        return sin_degrees(degrees) / cos_degrees(degrees)
    # check for division by zero as it throws an error
    except ZeroDivisionError:
        return None

def tan_radians(radians: float) -> float:
    try:
        return sin_radians(radians) / cos_radians(radians)
    except ZeroDivisionError:
        return None

def csc_degrees(degrees: float) -> float:
    try:
        return 1 / sin_degrees(degrees)
    except ZeroDivisionError:
        return None

def csc_radians(radians: float) -> float:
    try:
        return 1 / sin_radians(radians)
    except ZeroDivisionError:
        return None

def sec_degrees(degrees: float) -> float:
    try:
        return 1 / cos_degrees(degrees)
    except ZeroDivisionError:
        return None

def sec_radians(radians: float) -> float:
    try:
        return 1 / cos_radians(radians)
    except ZeroDivisionError:
        return None

def cot_degrees(degrees: float) -> float:
    try:
        return 1 / tan_degrees(degrees)
    except ZeroDivisionError:
        return None

def cot_radians(radians: float) -> float:
    try:
        return 1 / tan_radians(radians)
    except ZeroDivisionError:
        return None