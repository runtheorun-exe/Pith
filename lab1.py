import random
import csv
import pandas as pd
import plotly.express as px
# Δημιουργείστε ένα πρόγραμμα το οποίο κάθε φορά που εκτελείται θα επιστρέφει ένα τυχαίο αριθμό
def rnd():
    print(random.randint(0, 999999))

# Χρησιμοποιώντας τη συνάρτηση intrand(void) εμφανίστε στην οθόνη 10 τυχαίους αριθμούς.
def rnd_ten():
    for i in range(1, 10):
        print(random.randint(0, 999999))

# Εμφανίστε στην οθόνη τον μέγιστο αριθμό μέχρι τον οποίο μπορεί να αποδοθεί τυχαίος αριθμός
''' Ο τρόπος με τον οποίο δουλεύει η python καθιστά τον μέγιστο αριθμό μέχρι τον οποίο μπορεί να αποδοθεί τυχαίος αριθμός
γνωστό αριθμό που θέτει ο χρήστης'''

#Δημιουργείστε  ένα  πρόγραμμα,  χρησιμοποιώντας τη  γεννήτρια  τυχαίων  αριθμών
# (συναρτήσεις rand ()  &   srand()),  το   οποίο    θα  προσομοιώνει  τη  ρίψη  ενός  ζαριού.
# Εκτυπώστε στην οθόνη τη συχνότητα εμφάνισης των αποτελεσμάτων για Ν=10 ρίψεις

#ρίψη ζαριού χωρίς seed
def dice(N):
    randrow=[]
    nmbr=str(N)
    title= 'dice-rolls' + nmbr + '.csv'
    for i in range(0,N):
        randrow.append((random.randint(1,6)))
    with open(title, mode='a') as dice_rolls:
        writer = csv.writer(dice_rolls, delimiter=',', lineterminator='\n')
        writer.writerow(randrow)
        writer.writerow(" ")
    data = pd.read_csv(title)

#Χρησιμοποιώντας τον κώδικα του ερωτήματος 4, να καταγράψετε σε αρχείο (txt, csv, dat ) τα αποτελέσματα
#(συχνότητες εμφάνισης) της ρίψης ενός ζαριού για 10, 100, 1000, 10.000, 100.000, 1.000.000 φορές
n=10
for i in range(0,6):
    #print (n)
    dice(n)
    n=n*10


