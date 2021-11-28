#Name: Shahida Hoque
#Email: shahida.hoque03@myhunter.cuny.edu
#Date: March 17, 2020

kill = input("Enter borough name: ")
bill = input("Enter output file name: ")
    
#Libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Compute the fraction of the population in the Bronx, and save as new column:
pop['Fraction'] = pop[kill]/pop['Total']

#Create a plot of year versus fraction of pop. in Bronx (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to the file:  fractionBX.png
fig = plt.gcf()
fig.savefig(bill)
plt.show()
plt.imshow()
