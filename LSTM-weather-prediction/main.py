import numpy as np 
import pandas as pd 
import itertools
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
%matplotlib inline

data=pd.read_csv("./testset.csv")
print(f"READ -> {data.head()}")

data=data[["datetime_utc"," _tempm"]]
print(f"EXTRACT -> {data.head()}")

data.columns=["date","temp"]

# Converting to pandas datetime
data["date"]=pd.to_datetime(data["date"],format="%Y%m%d-%H:%M")

# Making index of dataframe == date
data=data.set_index("date")


# Sample plot
fig=plt.figure(figsize=(13,7),facecolor="green")
ax = plt.axes()
ax.set_facecolor("yellow")
plt.xlabel("Year",fontsize="15",fontweight="bold")
plt.ylabel("Mean Temperature",fontsize="15",fontweight="bold")
plt.grid(True)
plt.plot(data)
plt.show()