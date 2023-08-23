#Import bibliotek
import pandas as pd
import csv as csv
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import scipy
sns.set_theme(style="darkgrid")

def Korelacja(K1:pd.DataFrame, K2:pd.DataFrame):
    #Kand_coef, Kand_p = scipy.stats.kendalltau(K1,K2)
    Kand_coef, Kand_p = scipy.stats.pearsonr(K1,K2)
    print("Korelacja Pearsona: " + str(Kand_coef) + "; p = " + str(Kand_p))
    Spear_coef, Spear_p = scipy.stats.spearmanr(K1,K2)
    print("Korelacja Spearmana: " + str(Spear_coef) + "; p = " + str(Spear_p))
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(K1,K2)
    print("R^2: " + str(r_value) + " Std_err:" + str(std_err))

def Kompiluj_Dane(df:pd.DataFrame, Kolumna1:pd.DataFrame, Kolumna2:pd.DataFrame, bin1 = 10, bin2 = 10):
    #dfTemp=pd.concat([Kolumna1,Kolumna2], axis=1, ignore_index=True)
    
    Kolumna1.hist(bins=bin1)
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    Kolumna2.hist(bins=bin2)
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    plt.scatter(x = Kolumna1,y = Kolumna2);  # Plot some data on the axes.
    plt.show()

    coef, p = scipy.stats.kendalltau( df['Srednie dobowe cisnienie na poziomie stacji [hPa]'], df['Suma dobowa opadu [mm]'])
    print("Korelacja kandella: " + str(coef))
    coef, p = scipy.stats.spearmanr(df['Srednie dobowe cisnienie na poziomie stacji [hPa]'], df['Suma dobowa opadu [mm]'] )
    print("Korelacja spearmana: " + str(coef))
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(Kolumna1, Kolumna2)
    print("R^2: " + str(r_value) + " Std_err:" + str(std_err))

