import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Data = pd.read_csv('Iris.csv')

# Select numerical columns
Numerical_Data = Data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# Compute the correlation matrix
Corr = Numerical_Data.corr()

# Generate a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(Corr, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
plt.title('Correlation Heatmap of Iris Dataset Features')
plt.show()