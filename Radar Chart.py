import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def Plot_Player_Attributes(Data):

   #for Name in Data['Name']:
        #Attributes_Data = Data[(Data['Name'] == Name)]
    Attributes_Name = ["STR","VIT","LUK","INT","DEX","AGV"]
    Attributes_Value = Data[["STR","VIT","LUK","INT","DEX","AGV"]].to_numpy()

    # Number of attributes
    Num_Attributes = len(Attributes_Name)

    # Calculate angle for each attribute
    Angles = np.linspace(0, 2 * np.pi, Num_Attributes, endpoint=False).tolist()

    # Make the plot close
    Attributes_Value = np.concatenate((Attributes_Value, Attributes_Value[:,[0]]), axis=1)
    Angles += Angles[:1]
    
    # Plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for i in range(len(Attributes_Value)):
        ax.plot(Angles, Attributes_Value[i], linewidth=1, linestyle='solid', label=Data['Name'][i])
    ax.fill(Angles, Attributes_Value[i], alpha=0.25)

    # Add labels
    ax.set_yticklabels([])
    ax.set_xticks(Angles[:-1])
    ax.set_xticklabels(Attributes_Name)
    ax.legend(loc='upper right')

    # Title
    plt.title('Player Attributes')

    # Show the plot
    plt.show()

Raw_Data = pd.read_csv('Ragnarok RPG State.csv')
Plot_Player_Attributes(Raw_Data)
