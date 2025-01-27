import numpy as np
import random as rd
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self):
        self.x = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        self.y = [rd.randint(-4, 8) for i in range(12)] # syntax = [expression for item in iterable]

    def bar(self):
        """Plot a bar chart"""

        plt.style.use("dark_background")
        # plt.figure(figsize=(10, 6))
        color = [("r" if i < 0 else "g") for i in self.y] # list comprehension to color the bars
        plt.bar(self.x, self.y, width=0.5, color=color)
        plt.show()

plotter = Plotter()
plotter.bar()
