import pandas as pd
import matplotlib.pyplot as plt


Data = pd.read_csv('Iris.csv')



#  Plot the scatter of Sepal
plt.figure(figsize=(10, 6))
plt.scatter(Data['SepalLengthCm'], Data['SepalWidthCm'], c='blue', label='Sepal')
plt.scatter(Data['PetalLengthCm'], Data['PetalWidthCm'], c='red', label='Petal')
plt.title('Scatter Plot of Sepal vs Petal')
plt.xlabel('Length (Cm)')
plt.ylabel('PetalWidth (Cm)')
plt.grid(True)
plt.legend()
plt.show()