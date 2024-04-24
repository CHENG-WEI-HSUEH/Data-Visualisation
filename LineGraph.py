import pandas as pd
import matplotlib.pyplot as plt


def Plot_Rainfall(Data, Year):
    
    # Plotting
    plt.figure(figsize=(12, 6))
    coloar_table = ['b','c','g','k','m','r','w','y']
    Coloar_Index = 0
    for Year_Var in Year:
        # Filter the DataFrame for the year 
        New_Data = Data[(Data['Year'] == Year_Var) & (Data['Type of period'] == 'Monthly')]
        plt.plot(New_Data['Period'], New_Data['Avg rainfall(in mm)'], marker='o', linestyle='-', color=coloar_table[Coloar_Index], label=f'{Year_Var}')
        plt.legend()
        Coloar_Index = Coloar_Index + 1
        
    plt.title(f'Monthly Rainfall for the Year {Year}')
    plt.xlabel('Month')
    plt.ylabel('Average Rainfall (in mm)')
    plt.grid(True)
    plt.show()

Raw_Data = pd.read_csv('Weather_Info_In_UK.csv')
Plot_Rainfall(Raw_Data, [2010,2011,2012,2013])
