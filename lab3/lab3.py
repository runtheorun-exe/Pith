import random
import csv
import matplotlib.pyplot as plt


def rangen(n):
    nmbr = str(n)
    csv_file = "rangen" + nmbr + ".csv"
    chartname = "rangen" + nmbr
    a, b, c, d, e, f, g, h, i, j = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    results = {
        "[0-0.1)": a,
        "[0.1-0.2)": b,
        "[0.2-0.3)": c,
        "[0.3-0.4)": d,
        "[0.4-0.5)": e,
        "[0.5-0.6)": f,
        "[0.6-0.7)": g,
        "[0.7-0.8)": h,
        "[0.8-0.9)": i,
        "[0.9-1]": j
    }
    csv_columns = [
        '[0-0.1)',
        '[0.1-0.2)',
        '[0.2-0.3)',
        '[0.3-0.4)',
        '[0.4-0.5)',
        '[0.5-0.6)',
        '[0.6-0.7)',
        '[0.7-0.8)',
        '[0.8-0.9)',
        '[0.9-1]'
    ]

    for i in range(0, n):
        result = (random.random())
        if result < 0.1:
            results["[0-0.1)"] += 1
        elif result < 0.2:
            results["[0.1-0.2)"] += 1
        elif result < 0.3:
            results["[0.2-0.3)"] += 1
        elif result < 0.4:
            results["[0.3-0.4)"] += 1
        elif result < 0.5:
            results["[0.4-0.5)"] += 1
            results["[0.5-0.6)"] += 1
        elif result < 0.7:
            results["[0.6-0.7)"] += 1
        elif result < 0.8:
            results["[0.7-0.8)"] += 1
        elif result < 0.9:
            results["[0.8-0.9)"] += 1
        else:
            results["[0.9-1]"] += 1

    fig, ax = plt.subplots()

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',')
        writer.writeheader()
        writer.writerow(results)


n = 10
for i in range(0, 6):
    rangen(n)
    n *= 10
