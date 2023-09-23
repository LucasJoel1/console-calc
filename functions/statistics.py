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
    
def stdev(numbers: list[float]) -> float:
    length = len(numbers)
    numbersMean = mean(numbers)
    result = 0
    top = 0
    for i in numbers:
        top += (i - numbersMean) ** 2
    result = top / (length - 1)
    return sqrt(result)

def stdevp(numbers: list[float]) -> float:
    length = len(numbers)
    numbersMean = mean(numbers)
    result = 0
    top = 0
    for i in numbers:
        top += (i - numbersMean) ** 2
    result = top / length
    return sqrt(result)

def var(numbers: list[float]) -> float:
    length = len(numbers)
    numbersMean = mean(numbers)
    top = 0
    for i in numbers:
        top += (i - numbersMean) ** 2
    return top / (length - 1)

def mad(numbers: list[float]) -> float:
    length = len(numbers)
    numbersMean = mean(numbers)
    top = 0
    for i in numbers:
        top += abs(i - numbersMean)
    return top / length

def cov(numbers1: list[float], numbers2: list[float]):
    if len(numbers1) != len(numbers2):
        return None
    numbers1Mean = mean(numbers1)
    numbers2Mean = mean(numbers2)
    length = len(numbers1)
    top = 0
    for i in range(length):
        top += (numbers1[i] - numbers1Mean) * (numbers2[i] - numbers2Mean)
    return top / (length - 1)

def covp(numbers1: list[float], numbers2: list[float]) -> float:
    if len(numbers1) != len(numbers2):
        return None
    numbers1Mean = mean(numbers1)
    numbers2Mean = mean(numbers2)
    length = len(numbers1)
    top = 0
    for i in range(length):
        top += (numbers1[i] - numbers1Mean) * (numbers2[i] - numbers2Mean)
    return top / (length)

def corr(numbers1: list[float], numbers2: list[float]) -> float:
    if len(numbers1) != len(numbers2):
        return None
    return cov(numbers1, numbers2) / (stdev(numbers1) * stdev(numbers2))

def spearman(numbers1: [float], numbers2: [float]) -> float:
    if len(numbers1) != len(numbers2):
        return None
    numbers1Ranked = []
    numbers2Ranked = []
    sortedNumbers1, sortedNumbers2 = sort(numbers1), sort(numbers2)

    for i in range(len(numbers1)):
        for j in range(len(numbers1)):
            if numbers1[i] == sortedNumbers1[j]:
                numbers1Ranked.append(j)
            if numbers2[i] == sortedNumbers2[j]:
                numbers2Ranked.append(j)
    topRight = 0
    for i in range(len(numbers1)):
        topRight += abs(((numbers1Ranked[i] - numbers2Ranked[i]))) ** 2
    bottom = len(numbers1) * ((len(numbers1) ** 2) - 1)
    return 1 - 6 * topRight / bottom
