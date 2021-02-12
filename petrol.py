#importring libraries
import matplotlib.pyplot as plt
import pandas as pd

#reading data from a csv file
data = pd.read_csv("petrol_price.csv")

month = data["Month"]
avg_price_m = data["Monthly average Retail Selling Price of Petrol (Rs./Ltr) - Mumbai"]
avg_price_d = data["Monthly average Retail Selling Price of Petrol (Rs./Ltr) - Delhi"]
avg_price_c = data["Monthly average Retail Selling Price of Petrol (Rs./Ltr) - Chennai"]
avg_price_k = data["Monthly average Retail Selling Price of Petrol (Rs./Ltr) - Kolkata"]

#plotting time-series plot
plt.style.use("ggplot")
plt.plot_date(month, avg_price_m, linestyle = 'solid', label = "Mumbai")
plt.plot_date(month, avg_price_d, linestyle = 'solid', label = "Delhi")
plt.plot_date(month, avg_price_c, linestyle = 'solid', label = "Chennai")
plt.plot_date(month, avg_price_k, linestyle = 'solid', label = "Kolkata")

plt.title("Monthly average Retail Selling Price of Petrol \n(Rs./Ltr)")
plt.ylabel("Average price")
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.show()