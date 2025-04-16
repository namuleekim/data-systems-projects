# -*- coding: utf-8 -*-
"""
CS181 Project 2 - Requirement 3
Data Cleaning and Processing - kimyooncleaningv2.py
This cleans data and creates SQL database to create a table for relevant data.

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 20 April 2024
"""
#import os
import sqlite3
import pandas as pd
import kimyoonparsingv2 as kyp

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def clean_crash_data():
    """
    Selects data from 2017~2020. Aggregates the number of crashes, deaths, and
    injuries for each year. Returns a DataFrame containing selected data.

    Returns
    -------
    year_data : pandas DataFrame
        Contains selection of data from vast file.

    """

    ## Build DataFrame
    print('>>> Parsing Crash Data... Please Wait')
    collist = [
        'CRASH DATE',
        'COLLISION_ID',
        'NUMBER OF PERSONS INJURED',
        'NUMBER OF PERSONS KILLED'
        ]
    crash_df = pd.read_csv('Motor_Vehicle_Collisions_-_Crashes.csv', usecols= collist)
    crash_df['CRASH DATE'] = pd.to_datetime(crash_df['CRASH DATE'])
    ## Only select data in years 2017-2020
    crash_df = crash_df[crash_df['CRASH DATE'].dt.year.isin([2017, 2018, 2019, 2020])]
    ## Aggregate total injured, killed, and crashes for each year
    year_data = crash_df.groupby(crash_df['CRASH DATE'].dt.year).agg(
        total_injured=('NUMBER OF PERSONS INJURED', 'sum'),
        total_killed=('NUMBER OF PERSONS KILLED', 'sum'),
        total_crash=('COLLISION_ID', 'count')
        ).reset_index()
    year_data['CRASH DATE'] = year_data['CRASH DATE'].astype(int)
    return year_data

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def clean_air(year: int):
    """
    Creates dataframe from functions constructed in kimyoonparsing.py. 
    Selects data and returns a list of data.

    Parameters
    ----------
    year : int
        Year info. Allows program to recognize which year to select data from.

    Returns
    -------
    data_list : list
        list containing air polution data for the given year parameter.

    """
    ##Create DataFrame
    df1 = kyp.json_to_dataframe('Air_Quality.json')
    year = str(year)
    data_list=[]
    ##Selecting data
    collist = [
        'Start_Date',
        'Time Period',
        'Name',
        'Data Value',
        'Geo Place Name'
        ]
    namelist = [
        'Nitrogen dioxide (NO2)',
        'Fine particles (PM 2.5)'
        ]
    df2 = df1.loc[
        (df1['Name'].isin(namelist)) &
        (df1['Time Period'].str.contains('Annual Average')) &
        (df1['Geo Place Name'] == 'New York City') &
        (df1['Start_Date'].str.contains(year)), collist
        ]
    ##Appending list to return
    data_list.append(df2.loc[
        (df2['Name']=='Nitrogen dioxide (NO2)') &
        (df2['Start_Date'].str.contains(year)),'Data Value'].item())
    data_list.append(df2.loc[
        (df2['Name']=='Fine particles (PM 2.5)') &
        (df2['Start_Date'].str.contains(year)),'Data Value'].item())
    return data_list

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def clean_evcount(year: int):
    """
    Creates dataframe and selects data. Returns an int value.

    Parameters
    ----------
    year : int
        Year info. Allows program to recognize which year to select data from.

    Returns
    -------
    count : int
        Number of electric vehicles sold in given year.

    """
    year = str(year)
    ##Selecting and creating DataFRame
    collist = [
        'Submitted Date',
        'Make',
        'EV Type'
        ]
    df1 = pd.read_csv(
        'NYSERDA_Electric_Vehicle_Drive_Clean_Rebate_Data__Beginning_2017.csv',
        usecols = collist
        )
    df1['Submitted Date'] = pd.to_datetime(df1['Submitted Date'])
    df1 = df1.sort_values(by='Submitted Date')
    df1['Submitted Date'] = df1['Submitted Date'].astype(str)
    df2 = df1.loc[(df1['Submitted Date'].str.contains(year))]
    count = df2['Submitted Date'].count().item()
    return count
#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def create_table(dbname: str):
    """
    Create database and tables. Returns nothing

    Parameters
    ----------
    dbname : str
        Name of database file to create.

    Returns
    -------
    None.

    """
    ##SQL Connection
    dbname += '.db'
    con = sqlite3.connect(dbname)
    ## Create table.
    cur = con.cursor()
    createquery ="""
                CREATE TABLE IF NOT EXISTS `EV 2017~2020`(
                    `Year` INT NOT NULL PRIMARY KEY,
                    `New EVs` INT NOT NULL,
                    `Collision Count` INT NOT NULL,
                    `Collision Injuries` INT NOT NULL,
                    `Collision Deaths` INT NOT NULL,
                    `Annual NO2` FLOAT NOT NULL,
                    `Annual PM2.5` FLOAT NOT NULL
                    )
                """
    cur.execute(createquery)
    ##Data aggregation and insertion.
    crash_df = clean_crash_data()
    for i in range(4):
        year = 2017+i
        data_dict = [year]
        data_dict.append(clean_evcount(year))
        data_dict.append(crash_df.loc[(crash_df['CRASH DATE'] == year), 'total_crash'].item())
        data_dict.append(crash_df.loc[(crash_df['CRASH DATE'] == year), 'total_injured'].item())
        data_dict.append(crash_df.loc[(crash_df['CRASH DATE'] == year), 'total_killed'].item())
        data_dict.append(clean_air(year)[0])
        data_dict.append(clean_air(year)[1])
        insertquery ='INSERT INTO `EV 2017~2020` VALUES (?, ?, ?, ?, ?, ?, ?)'
        ## Insert data
        cur.execute(insertquery, data_dict)
        con.commit()
    con.close()
