import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("telecalling_performance.csv")

fig, ax = plt.subplots(1,0, figsize=(12,5))
ax[0].plot(df["day"],df["calls_made"])
ax[0].set_title("Calling Activity")
ax[0].set_xlabel("days")
ax[0].set_ylabel("calls")

plt.show()