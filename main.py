import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/clean_data.csv")

# =============================================================================
# First plot: PIE PLOT of Class
# =============================================================================
path1 = "./img/1_Introduction/"
os.makedirs(path1, exist_ok=True)

n = 3
labels = [name for name in df["class"].value_counts().index[0:n]]
m = len(df["class"].value_counts().index) - n
labels.extend(["" for i in range(m)])

filename = "1_1_class_pie.png"

plt.figure()
plt.pie(df["class"].value_counts(), labels = labels)
plt.title("Asteroids per class")
plt.savefig(path1 + filename)