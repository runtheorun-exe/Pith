import math
import random


def stdev(variance):
    return(math.sqrt(variance))


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return (variance)

randset = []

for i in range(0, 15):
    randset.append(random.randint(0, 99999))

n = len(randset)
var = variance(randset)
mean = sum(randset) / n

print (mean, var, stdev(var))
