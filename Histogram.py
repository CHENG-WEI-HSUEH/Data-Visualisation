import pandas as pd
import matplotlib.pyplot as plt

def Historgram_of_Rainfall(Raw_Data, Year):
    
    Data = Raw_Data[(Raw_Data['Type of period'] == 'Monthly') & (Raw_Data['Year'] == Year)]
    # Plot histogram
    plt.figure(figsize=(8, 6))
    plt.bar(Data['Period'], Data['Avg rainfall(in mm)'], color='blue', alpha=0.7)
    plt.xlabel('Month')
    plt.ylabel('Average Rainfall (mm)')
    plt.title(f'Average Monthly Rainfall in {Year}')
    plt.show()

Raw_Data = pd.read_csv('Weather_Info_In_UK.csv')
Historgram_of_Rainfall(Raw_Data, 2010)


