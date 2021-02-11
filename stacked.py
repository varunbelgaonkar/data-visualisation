#importing libraries
from matplotlib import pyplot as plt
import numpy as np

#selecting a style for the plot
plt.style.use("ggplot")

#data to be plotted
males = np.array([50, 100, 80, 90, 75])
females = np.array([75, 50, 65, 80, 90])
year = [2000, 2001, 2002, 2003, 2004]

#plotting stacked bar plot
plt.bar(year, males, color = "#66E7F5", label = "male")
plt.bar(year, females, color = "#04444F", bottom = males, label = "female")
plt.title("Population Compostion")
plt.ylabel("Population")
plt.xlabel("Year")
plt.tight_layout()
plt.legend()
plt.show()