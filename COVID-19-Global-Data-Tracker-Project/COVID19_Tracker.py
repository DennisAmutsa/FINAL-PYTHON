# COVID-19 Global Data Tracker Project

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configure default style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 2. Load the COVID-19 Dataset from Our World in Data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# 3. View the structure
print("Shape of dataset:", df.shape)
print("\nFirst few rows of the dataset:")
print(df.head())

# 4. Basic Data Information
print("\nDataset Information:")
print(df.info())

# 5. Basic Statistics
print("\nBasic Statistics:")
print(df.describe()) 