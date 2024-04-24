import pandas as pd
import matplotlib.pyplot as plt


def Transform_Bubble(Raw_Data, X, Y):

    New_Data = pd.DataFrame(columns=[X, Y, 'Size'])
    
    X_Min =int(Raw_Data[X].min())
    X_Max =int(Raw_Data[X].max())
    Y_Min =int(Raw_Data[Y].min())
    Y_Max =int(Raw_Data[Y].max())
              
    for Step_X in range(X_Min, X_Max, 1):
        for Step_Y in range(Y_Min, Y_Max, 1):
            Size_in_range = 0
            # Filter the DataFrame for values within the X and Y range
            Filtered_Df = Raw_Data[(Raw_Data[X] >= Step_X-0.5) & (Raw_Data[X] <= Step_X+0.5) & (Raw_Data[Y] >= Step_Y-0.5) & (Raw_Data[Y] <= Step_Y+0.5)]
            
            # Count the number of entries within the specified range
            Size_in_range = Filtered_Df.shape[0]
             
            if Size_in_range > 0:
                Temp_Data = pd.DataFrame({X: [Step_X], Y: [Step_Y], 'Size': [Size_in_range]})
                New_Data = pd.concat([New_Data,Temp_Data], ignore_index=True)
    
    # Convert 'Size' to float and check if there's any inappropriate value
    New_Data['Size'] = pd.to_numeric(New_Data['Size'], errors='coerce').fillna(0)
    New_Data['Size'] = New_Data['Size'] * 20

    return New_Data

# Load the data
Raw_Data = pd.read_csv('Iris.csv')
Sepal_Data = Transform_Bubble(Raw_Data, 'SepalLengthCm', 'SepalWidthCm')
Petal_Data = Transform_Bubble(Raw_Data, 'PetalLengthCm', 'PetalWidthCm')

# Plot the bubble chart
plt.figure(figsize=(10, 10))

# Sepal data
plt.scatter(Sepal_Data['SepalLengthCm'], Sepal_Data['SepalWidthCm'], s=Sepal_Data['Size'], c='blue', alpha=0.5, edgecolor='black', label='Sepal')

# Petal data
plt.scatter(Petal_Data['PetalLengthCm'], Petal_Data['PetalWidthCm'], s=Petal_Data['Size'], c='red', alpha=0.5, edgecolor='black', label='Petal')

plt.title('Bubble Chart of Sepal vs Petal')
plt.xlabel('Length (Cm)')
plt.ylabel('Width (Cm)')
plt.grid(True)
plt.legend()
plt.show()
