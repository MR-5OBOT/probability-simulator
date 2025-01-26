import numpy as np
import random as rd
import matplotlib.pyplot as plt

def rand_plots():
    # prepare 
    x = ["jan", "feb", "mar"]
    range_n = 100
    for n in range(range_n):
        n = rd.randrange(-1, 10, 1)
        # render
        plt.subplot()
        plt.plot(x, n)
        plt.show()

rand_plots()
