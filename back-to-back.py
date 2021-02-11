#importing libraries
from matplotlib import pyplot as plt
import numpy as np

#selecting a style for the plot
plt.style.use("ggplot")
#data to be plotted
males = np.array([50, 100, 80, 90, 75])
females = np.array([75, 50, 65, 80, 90])
year = [2000, 2001, 2002, 2003, 2004]

#plotting back-to-back bar plot
plt.barh(year, males, color = "#2A9392", label = "male")
plt.barh(year, -females, color = "#FCE2C6", label = "female")
plt.xticks(range(-100,101,20), list(range(100,0,-20)) + list(range(0,101,20)))
plt.title("Population composition")
plt.xlabel("Population")
plt.legend()
plt.tight_layout()
plt.show()