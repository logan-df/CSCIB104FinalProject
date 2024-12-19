# Programmers: Ford, Logan & Hohmann, Soeren
# Assignment: Final Project
# Course: CSCI/ISAT B104

#All necessary imports needed for generating graphs and statistical analysis.

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#Using pandas to read our excel file into python as a dataframe.

df = pd.read_excel(r'C:/Users/ldfor/OneDrive/Desktop/CSCIB104/SQLDATA.xlsx.xlsx')

#We chose to assign our graphics to functions in order to limit memory usage 
#and create a more stremlined user experience.

def heatmap():
    sns.heatmap(df.corr(), 
                cmap="Blues", 
                annot=True, 
                fmt=".3f",
                annot_kws={
                    'fontsize': 8,
                    'fontweight': 'bold'
                }
            ).set(title='Dataset Heatmap')
    plt.show()

def histplotM():
    h = sns.FacetGrid(df, col="Sex")
    h.map(sns.histplot,
                 'Marijuana',  
                 bins=11, 
                 stat='percent',
                 palette='Blues',
                 shrink = 1.5
            )
    plt.show()
    
def histplotA():
    h = sns.FacetGrid(df, col="Sex")
    h.map(sns.histplot,
                 'Alcohol',  
                 bins=15, 
                 stat='percent',
                 palette='Blues',
                 shrink = 1.5
            ).set_titles(col_template=('{col_name}')
            )
    plt.show()
    
#This is the loop that is called upon when the code is ran, and will loop 
#indefinitely, allowing the user to call upon selected graphs.

while True:
    try:
        print('\nSelect a graph to display:\n\tHeatmap: [1]\n\tHistogram: [2]')
        i = int(input('Choice: '))
    except ValueError:
        print('Invalid Value, please provide an integer from the listed options.\n-------------------------------------------------------------------')
        continue
    if i == 1:
        heatmap()
        print('\n-------------------------------------------------------------------')
        continue
    if i == 2:
        print('\nSelect a Histogram graph to display:\n\tMarijuana Histogram: [1]\n\tAlcohol Histogram: [2]')
        j = int(input('Choice: '))
        if j == 1:
            histplotM()
        if j == 2:
            histplotA()
        print('\n-------------------------------------------------------------------')
    else:
        print('\nInvalid Value, please provide an integer from the listed options.\n-------------------------------------------------------------------')

    
