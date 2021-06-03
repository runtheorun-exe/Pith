import csv
import random
import matplotlib.pyplot as plt


# Δημιουργείστε ένα πρόγραμμα το οποίο κάθε φορά που εκτελείται θα επιστρέφει ένα τυχαίο αριθμό
def rnd():
    print(random.randint(0, 999999))


# Χρησιμοποιώντας τη συνάρτηση intrand(void) εμφανίστε στην οθόνη 10 τυχαίους αριθμούς.
def rnd_ten():
    for x in range(1, 10):
        print(random.randint(0, 999999))


# Εμφανίστε στην οθόνη τον μέγιστο αριθμό μέχρι τον οποίο μπορεί να αποδοθεί τυχαίος αριθμός
''' Ο τρόπος με τον οποίο δουλεύει η python καθιστά τον μέγιστο αριθμό μέχρι τον οποίο μπορεί να αποδοθεί τυχαίος αριθμός
γνωστό αριθμό που θέτει ο χρήστης'''


# Δημιουργείστε  ένα  πρόγραμμα,  χρησιμοποιώντας τη  γεννήτρια  τυχαίων  αριθμών
# (συναρτήσεις rand ()  &   srand()),  το   οποίο    θα  προσομοιώνει  τη  ρίψη  ενός  ζαριού.
# Εκτυπώστε στην οθόνη τη συχνότητα εμφάνισης των αποτελεσμάτων για Ν=10 ρίψεις

# ρίψη ζαριού χωρίς seed
def dice(N):
    nmbr = str(N)
    csv_file = "dice" + nmbr + "roll.csv"
    a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
    diceroll = {
        "1": a,
        "2": b,
        "3": c,
        "4": d,
        "5": e,
        "6": f
    }
    csv_columns = ['1', '2', '3', '4', '5', '6']
    for y in range(0, N):
        rolled = random.randrange(1, 7)
        if rolled == 1:
            diceroll["1"] += 1
        if rolled == 2:
            diceroll["2"] += 1
        if rolled == 3:
            diceroll["3"] += 1
        if rolled == 4:
            diceroll["4"] += 1
        if rolled == 5:
            diceroll["5"] += 1
        if rolled == 6:
            diceroll["6"] += 1
    plt.bar(*zip(*diceroll.items()))
    plt.show()
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=',')
        writer.writeheader()
        writer.writerow(diceroll)



# Χρησιμοποιώντας τον κώδικα του ερωτήματος 4, να καταγράψετε σε αρχείο (txt, csv, dat ) τα αποτελέσματα
# (συχνότητες εμφάνισης) της ρίψης ενός ζαριού για 10, 100, 1000, 10.000, 100.000, 1.000.000 φορές
n = 10
for i in range(0, 6):
    print(n)
    dice(n)
    n = n * 10
