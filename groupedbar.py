#importing libraries
from matplotlib import pyplot as plt
import numpy as np

#selecting a style for the plot
plt.style.use("seaborn")

#data to be plotted
students = ['boys', 'girls']
exrtracurr = [75,60]
nonextracurr = [50,86]

width = 0.25
x_val = np.arange(len(students))

#plotting a grouped bar
plt.bar(x_val, exrtracurr, width=width, label = "Extracurricular")
plt.bar(x_val+width, nonextracurr, width=width, label = "Nonextracurricular")
#changing the label of x-axis
plt.xticks(ticks=x_val, labels=students)
plt.title("Average Marks Scored")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.show()








