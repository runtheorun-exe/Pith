import csv
import random
import matplotlib.pyplot as plt


def flip(N):
    nmbr = str(N)
    csv_file = "coin" + nmbr + "roll.csv"
    chartname = "coin" + nmbr
    h, t = 0, 0
    coinflip = {
        "Heads": h,
        "Tails": t
    }

    csv_columns = ['Heads', 'Tails']
    for y in range(0, N):
        flipped = random.random()
        if flipped > 0.5:
            coinflip["Heads"] += 1
        else:
            coinflip["Tails"] += 1
    plt.bar(*zip(*coinflip.items()))
    plt.ylabel(chartname)
    chartname += ".png"
    plt.savefig(chartname)
    plt.show()
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',')
        writer.writeheader()
        writer.writerow(coinflip)

def biasedflip(N):
    nmbr = str(N)
    csv_file = "biasedcoin" + nmbr + "roll.csv"
    chartname = "biasedcoin" + nmbr
    h, t = 0, 0
    coinflip = {
        "Heads": h,
        "Tails": t
    }

    csv_columns = ['Heads', 'Tails']
    for y in range(0, N):
        flipped = random.random()
        if flipped > 0.4:
            coinflip["Heads"] += 1
        else:
            coinflip["Tails"] += 1
    plt.bar(*zip(*coinflip.items()))
    plt.ylabel(chartname)
    chartname += ".png"
    plt.savefig(chartname)
    plt.show()

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',')
        writer.writeheader()
        writer.writerow(coinflip)


n = 10
for i in range(0, 6):
    print(n)
    flip(n)
    biasedflip(n)
    n = n * 10
