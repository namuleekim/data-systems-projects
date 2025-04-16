# -*- coding: utf-8 -*-
"""
CS181 Project 2 - Requirement 2
Data Parsing - kimyoonparsing2.py
This function reads data into pandas dataframes.

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 11 April 2024
"""
#import os
import json
import pandas as pd

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def json_to_dataframe(jsonname):
    """
    Takes a json file by file name and converts the data into a pandas DataFrame.
    The created DataFrame is returned.

    Parameters
    ----------
    jsonname : str
        The name of json file to be read.

    Returns
    -------
    df : pandas DataFrame
        The json file's data converted into a pandas DataFrame. Needs cleaning
        of extra columns created from meta data.
    """
    ##Open file and create Dataframe
    with open(jsonname, 'r', encoding='utf-8') as jfile:
        file = json.loads(jfile.read())
    dataframe = pd.json_normalize(file,record_path='data')
    ## Pull column names ans assign to dataframe
    cols = pd.json_normalize(file, record_path=['meta', 'view', 'columns'])
    col_list = cols['name'].to_dict()
    dataframe.rename(columns=col_list,inplace=True)
    return dataframe

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def csv_to_dataframe(csvname):
    """
    Takes path as input. Reads a csv file then converts it into a pandas dataframe.

    Parameters
    ----------
    csvname : string path to csv file.

    Returns
    -------
    pdframe : pandas dataframe.

    """
    pdframe = pd.read_csv(csvname, dtype=str)
    return pdframe

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def main():
    """
    This reads different types of files into pandas dataframes, using different
    functions. It prints the dataframe then pauses before closing the prompt.

    Returns:
        nothing, prints output.
    -------

    """
    print('>>>Please wait, generating dataframes from files. This may take a moment. \n')

    dataframe_1 = csv_to_dataframe('Motor_Vehicle_Collisions_-_Crashes.csv')
    print('>>>(1/5)Motor_Vehicle_Collisions_-_Crashes.csv \n', dataframe_1, '\n')
    dataframe_2 = csv_to_dataframe('Motor_Vehicle_Collisions_-_Vehicles.csv')
    print('>>>(2/5)Motor_Vehicle_Collisions_-_Vehicles.csv \n', dataframe_2, '\n')
    dataframe_3 = csv_to_dataframe(
        'NYSERDA_Electric_Vehicle_Drive_Clean_Rebate_Data__Beginning_2017.csv'
        )
    print(
        '>>>(3/5)NYSERDA_Electric_Vehicle_Drive_Clean_Rebate_Data__Beginning_2017.csv \n',
        dataframe_3,
        '\n')
    dataframe_4 = json_to_dataframe('Air_Quality.json')
    print('>>>(4/5)Air_Quality.json \n', dataframe_4, '\n')
    dataframe_5 = csv_to_dataframe('Vehicle__Snowmobile__and_Boat_Registrations.csv')
    print('>>>(5/5)Vehicle__Snowmobile__and_Boat_Registrations.csv \n', dataframe_5, '\n')

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

#main()
#os.system('pause')
