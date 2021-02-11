#importing libraries
from matplotlib import pyplot as plt

#selecting a style for the plot
plt.style.use("fivethirtyeight")

#data to be plotted
names = ['Harry', 'Sam', 'Steve', 'David', 'Brian']
speed = [65, 50, 45, 63, 38]
error = [10, 5, 7, 5, 6]

#adding error bars
plt.bar(names, speed,color = "#F7BC6C", yerr = error)
plt.title(" Adding error bar")
plt.ylabel("Typing speed(wpm)")
plt.tight_layout()
plt.show()






