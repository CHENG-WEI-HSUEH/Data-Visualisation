import pandas as pd
import matplotlib.pyplot as plt


def Piechart_of_Rainfall(Raw_Data, Year):
    Data = Raw_Data[(Raw_Data['Type of period'] == 'Season') & (Raw_Data['Year'] == Year)]
    # Plot pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(Data['Avg rainfall(in mm)'], labels=Data['Period'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of Rainfall by Season in {Year}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()
    
Raw_Data = pd.read_csv('Weather_Info_In_UK.csv')
Piechart_of_Rainfall(Raw_Data, 2013)