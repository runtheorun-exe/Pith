import random
import matplotlib.pyplot as plt


def coin(N, start):
    for y in range(0, N):
        flipped = random.random()
        if flipped > 0.5:  # heads
            if start < 1000:
                start += 1
                position.append(start)
        else:
            if start > 0:
                start -= 1
                position.append(start)


def biaseddcoin(N, start):
    for y in range(0, N):
        flipped = random.random()
        if flipped > 0.7:  # heads
            if start < 1000:
                start += 1
                position.append(start)
        else:
            if start > 0:
                start -= 1
                position.append(start)


set = [10, 50, 100, 1000]
for i in range(0, len(set)):
    start = 500
    position = [start]
    coin(set[i], start)
    plt.plot(position)
    x = str(set[i])
    name = "randomwalk" + x + ".png"
    plt.savefig(name)
    plt.show()

for i in range(0, len(set)):
    start = 500
    position = [start]
    coin(set[i], start)
    plt.plot(position)
    x = str(set[i])
    name = "biasedwalk" + x + ".png"
    plt.savefig(name)
    plt.show()
