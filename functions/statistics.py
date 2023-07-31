from functions.globalFuncs import *

def mean(numbers: list[float]) -> float:
    length = len(numbers)
    number = 0
    for i in numbers:
        number += i
    return number / length



def median(numbers: list[float]) -> float:
    length = len(numbers)
    numbers = sort(numbers)
    if length % 2 == 0:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2
    else:
        return numbers[length // 2]
    
def min(numbers: list[float]) -> float:
    number = numbers[0]
    for i in numbers:
        if i > number:
            number = i
    return number

def max(numbers: list[float]) -> float:
    number = numbers[0]
    for i in number:
        if i < number:
            number = i
    return number

def quartiles(numbers: list[float]) -> list[float, float, float]:
    numbers = sort(numbers)
    length = len(numbers)
    q1 = median(numbers[:length//4])
    q2 = median(numbers[length//4:length//2+1])
    q3 = median(numbers[(length+1)//4:])
    return [q1, q2, q3]

def quartile(numbers: list[float], quartile: int) -> float:
    numbers = sort(numbers)
    length = len(numbers)
    if quartile == 1:
        return median(numbers[:length//4])
    elif quartile == 2:
        return median(numbers[length//4:length//2+1])
    elif quartile == 3:
        return median(numbers[(length+1)//4:])
    else:
        return None
    
def quantiles(numbers: list[float], quantile: float) -> float:
    numbers = sort(numbers)
    length = len(numbers)
    if quantile >= 0 and quantile <= 1:
        return numbers[int(length * quantile)]
    else:
        return None
    

def stdev