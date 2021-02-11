#importing library
from matplotlib import pyplot as plt

#selecting a style for the plot
plt.style.use("ggplot")

names = ['Harry', 'Sam', 'Steve', 'David', 'Brian']
marks = [70, 85, 60, 95, 40]
#colors for the bars
color = ['#7454F4', '#6454BC', '#3B99DE', '#109FC8']

#plotting graph
plt.barh(names, marks, color = color)
plt.title("Marks")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()