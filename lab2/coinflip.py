import random
import matplotlib.pyplot as plt

def flip():
    return 'H' if random.random() < 0.5 else 'T'

