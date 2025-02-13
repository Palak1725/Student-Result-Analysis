import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\palak\.vscode\Python\student_performance_dataset.csv")

print(df.head())
df.describe()
df.info()
print(df.isnull().sum())
plt.figure(figsize = (4, 5))
ax = sns.countplot(data = df, x = "gender", color="magenta")
ax.bar_label(ax.containers[0])
plt.title("Gender of Students")
plt.show()

gb = df.groupby("student_id").agg({"math_score": "mean", "science_score": "mean", "english_score": "mean"})
print(gb)
sns.heatmap(gb, annot = True)
plt.title("score comparison of different students.")
plt.show()

sns.boxplot(data = df, x = "overall_score")
plt.show()

print(df["extracurricular"].unique())
