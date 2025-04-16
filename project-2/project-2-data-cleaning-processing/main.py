# -*- coding: utf-8 -*-
"""
CS181 Project 1 - Requirement 3
Data Cleaning and Processing

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 20 April 2024
"""
#import os
import sqlite3
from os.path import exists
import pandas as pd
import kimyooncleaningv2 as kyc

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def main():
    """
    Cleans data using the functions we created.
    Plot graphs by retrieving cleaned data from our database.
    
    Returns
    -------
    None.

    """
    ## Cheking if database already exists.
    if not exists('EVcrashes.db'):
        kyc.create_table('EVcrashes')
    con = sqlite3.connect('EVcrashes.db')
    cur = con.cursor()
    ## Selecting data from database.
    selectquery = 'SELECT * FROM `EV 2017~2020`'
    cur.execute(selectquery)
    row = cur.fetchall()
    con.close()
    idx = [row[0][0], row[1][0], row[2][0], row[3][0]]
    df = pd.DataFrame(
        row,
        index = idx,
        columns = ['Year', 'New EVs', 'Crashes', 'Crash Injuries', 'Crash Deaths', 'NO2', 'PM 2.5']
        )
    del df['Year']
    ##Plotting (saved as .png within 'plots' folder).
    df.plot(
        xticks = [2017, 2018, 2019, 2020],
        y = ['New EVs', 'Crashes', 'Crash Injuries', 'Crash Deaths'],
        kind='line',
        title = 'EV Impact Road Safety 2017~2020'
        )
    df.plot(
        xticks = [2017, 2018, 2019, 2020],
        y = ['NO2'],
        kind='line',
        title = 'EV Impact Nitrogen Oxide (ppb) Quality 2017~2020',
        color ='r'
        )
    df.plot(
        xticks = [2017, 2018, 2019, 2020],
        y = ['PM 2.5'],
        kind='line',
        title = 'EV Impact Fine Particles (mcg/m^3) 2017~2020',
        color ='y'
        )

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

main()
