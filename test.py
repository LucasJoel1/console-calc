from functions.statistics import *

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [1,6,8,7,10,9,3,5,2,4]
result = spearman(numbers, numbers2)
print(result)