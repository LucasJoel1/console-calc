from functions.globalFuncs import *

def sin_degrees(degrees: float) -> float:
    radians = deg_to_rad(degrees)
    result = 0
    sign = 1
    for i in range(1, 21, 2):
        result += sign * (radians ** i) / factorial(i)
        sign *= -1
    return result

def sin_radians(radians: float) -> float:
    result = 0
    sign = 1
    for i in range(1, 21, 2):
        result += sign * (radians ** i) / factorial(i)
        sign *= -1
    return result

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

def tan_degrees(degrees: float) -> float:
    try :
        return sin_degrees(degrees) / cos_degrees(degrees)
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

def tan_degrees(degrees: float) -> float:
    try:
        return sin_degrees(degrees) / cos_degrees(degrees)
    except ZeroDivisionError:
        return None

def tan_radians(radians: float) -> float:
    try:
        return cos_radians(radians) / sin_radians(radians)
    except ZeroDivisionError:
        return None

