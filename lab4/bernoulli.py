import csv
import math
import matplotlib.pyplot as plt

flval = []
sum, sum1 = 0, 0
n = int(input("Πόσους αριθμούς θες να καταχωρήσεις;"))
for i in range(0, n):
    print("Δώσε τον", i + 1, "o αριθμό")
    flval.append(float(input()))
    sum += flval[i]

average = sum / n

for i in range(0, n):
    sum1 += (flval[i] - average) ** 2

variance = sum1 / n
std_dev = math.sqrt(variance)

results = {
    "sum": sum,
    "variance": variance,
    "standard deviation": std_dev,
    "average of elements": average
}
csv_columns = [
    'sum',
    'variance',
    'standard deviation',
    'average of elements'
]
text = {sum, variance, std_dev, average}

plt.bar(*zip(*results.items()))
plt.ylabel("chart")
plt.savefig("chart.png")
plt.show()

with open("bernouliresults.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',')
    writer.writeheader()
    writer.writerow(results)
