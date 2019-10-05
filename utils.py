# imports for data analysis (ignore)
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# loading datasets
rideshare = pd.read_csv('data/rideshare.csv')
cabRides = pd.read_csv('data/cab_rides.csv')
cabRides = cabRides[cabRides['cab_type'].str.lower() == "lyft"]


def display_cabRides():
    return cabRides.head()

def plot_distributions():
    # see plots below
    fig, ax = plt.subplots(1,2, figsize=(20,4))

    # left plot
    sns.distplot(cabRides['distance'], hist=False, ax=ax[0])
    ax[0].set_title("Distribution of Ride Distances")
    ax[0].set_xlabel('miles')

    # right plot
    sns.distplot(cabRides['time_stamp'], hist=False, ax=ax[1])
    ax[1].set_title("Distribution of Ride Times")
    min_hour = min(cabRides['time_stamp'])
    max_hour = max(cabRides['time_stamp'])
    ax[1].set_xticks(np.linspace(min_hour, max_hour, 24))
    ax[1].set_xticklabels([int(i) for i in np.linspace(1,24,24)])
    ax[1].set_xlabel('hour of day')
    plt.show()

    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Mean distance: ", np.mean(cabRides['distance']), "(miles)")
    print("Std distance: ", np.std(cabRides['distance']), "(miles)")
    print("- - - - - - - - - - - - - - - - - - - - - - - - -")
    
def plot_facebook_rideshare():
    (sns.catplot(x='university', y='num_followers', 
                 data=rideshare.sort_values("num_followers", ascending=False)
                 .iloc[0:6,:], kind='bar', aspect=3))
    plt.title("Popular Facebook Rideshare Pages", fontsize=20)
    plt.ylabel("Member Count", fontsize=14)
    plt.xlabel("University", fontsize=14)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.show()