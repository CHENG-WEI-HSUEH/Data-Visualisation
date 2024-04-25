import pandas as pd
import matplotlib.pyplot as plt



def Boxplot_of_Rainfall(Raw_Data, Year):
    Data = Raw_Data[(Raw_Data['Type of period'] == 'Monthly') & (Raw_Data['Year'] == Year)]
    # Plot Boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot(Data['Avg rainfall(in mm)'])
    
    plt.ylabel('Average Rainfall (mm)')
    plt.title(f'Monthly Average Rainfall Boxplot in {Year}')
    plt.grid(True)
    plt.show()

Raw_Data = pd.read_csv('Weather_Info_In_UK.csv')
Boxplot_of_Rainfall(Raw_Data, 2013)