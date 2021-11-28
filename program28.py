#Name: Shahida Hoque
#Email: shahida.hoque03@myhunter.cuny.edu
#Date: March 25, 2020

A = input("Enter borough: ")

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop.plot(x="Year")

print("Minimum population:", pop[A].min())
print("Maximum population:", pop[A].max())
print("Average population:", pop[A].mean())
print("Standard deviation:", pop[A].std())
