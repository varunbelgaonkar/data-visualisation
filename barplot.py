from matplotlib import pyplot as plt
import pandas as pd

plt.style.use("ggplot")

data = pd.read_csv("olpay.csv")
x = data["Financial Year"]
y = data["Total Digital Transactions (In Crore)"]
width = 0.5
color = ['#7454F4', '#6454BC', '#3B99DE', '#109FC8']

plt.bar(x, y, color = color, width = width)
plt.xlabel("Financial layer")
plt.ylabel("Total Digital Transactions (In Crore)")
plt.tight_layout()
plt.show()





