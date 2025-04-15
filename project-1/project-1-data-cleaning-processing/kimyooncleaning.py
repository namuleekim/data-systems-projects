# -*- coding: utf-8 -*-
"""
CS181 Project 1 - Requirement 3
Data Cleaning and Processing - kimyooncleaning.py
This cleans data and returns dataframes based on desired year.

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 8 March 2024
"""

#import os
import kimyoonparsing as kyp

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789


def clean_drugs_data(year):
    """
    This function cleans the 'drugs.csv' data. This function takes the columns
    divided by age into a single column. We have selected specific columns
    such as alcohol use, illicit drugs, and marijuanna use. All the others
    are dropped. The function returns a cleaned up drugs data.

    Parameters
    ----------
    year : integer value of either 2016 or 2017. Other values are rejected.

    Returns
    -------
    filtered_drugs_df : cleaned up drugs data

    """
    if year == 2016 or year == 2017:
        drugs_df = kyp.csv_to_dataframe('drugs.csv')

        ##Since data is scattered between columns, finding sum of related columns.
        drugs_df['Population'] = drugs_df[[
            'Population.12-17', 'Population.18-25', 'Population.26+'
        ]].sum(axis=1)
        drugs_df['Alcohol'] = drugs_df[[
            'Totals.Alcohol.Use Disorder Past Year.12-17',
            'Totals.Alcohol.Use Disorder Past Year.18-25',
            'Totals.Alcohol.Use Disorder Past Year.26+'
        ]].sum(axis=1)
        drugs_df['Illicit.Drugs'] = drugs_df[[
            'Totals.Illicit Drugs.Cocaine Used Past Year.12-17',
            'Totals.Illicit Drugs.Cocaine Used Past Year.18-25',
            'Totals.Illicit Drugs.Cocaine Used Past Year.26+'
        ]].sum(axis=1)
        drugs_df['Marijuana'] = drugs_df[[
            'Totals.Marijuana.Used Past Year.12-17',
            'Totals.Marijuana.Used Past Year.18-25',
            'Totals.Marijuana.Used Past Year.26+'
        ]].sum(axis=1)

        ##Selection and projection of the rows and columns needed.
        relevent_columns_drugs = [
            'State', 'Year', 'Population', 'Alcohol', 'Illicit.Drugs',
            'Marijuana'
        ]
        filtered_drugs_df = drugs_df.loc[(drugs_df['Year'] == year) & (
            drugs_df['State'].isin(['California', 'Texas'])),
                                         relevent_columns_drugs]
        return filtered_drugs_df

    else:
        print("Please choose 2016 or 2017 as parameter")
        return 0


#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789


def clean_crime_data(year: int):
    """
    This function selecting California and Texas data for the year 2016 or
    2017. We have selected Data.Population and Data.Totals.Violent.All
    and dropped everything else. The function returns a cleaned up version
    of the crime data with everything else dropped.

    Parameters
    ----------
    year : integer value of either 2016 or 2017. Other values are rejected.

    Returns
    -------
    filtered_crime_df : cleaned up crime data

    """
    if year == 2016 or year == 2017:
        crime_df = kyp.csv_to_dataframe('state_crime.csv')

        ##Selection and projection of the rows and columns needed.
        relevent_columns_crime = [
            'State', 'Year', 'Data.Population', 'Data.Totals.Violent.All'
        ]
        filtered_crime_df = crime_df.loc[(crime_df['Year'] == year) & (
            crime_df['State'].isin(['California', 'Texas'])),
                                         relevent_columns_crime]

        return filtered_crime_df
    else:
        print("Please choose 2016 or 2017 as parameter")
        return 0


#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789


def clean_cause_of_death(year):
    """
  This function is capable of selecting California and Texas for the year 2016
  or 2017. Underlying causes of death relative to our project have been selected,
  and the rest are dropped. The function returns a cleaned dataframe.
  
    Parameters
    ----------
    year : integer value of either 2016 or 2017. Other values are rejected.

    Returns
    -------
    filtered_deaths_df : Multiple_Cause_of_death data cleaned up. 

    """
    if year == 2016:
        deaths_df = kyp.tsv_to_dataframe('Multiple_Cause_of_Death_2016.txt')
    elif year == 2017:
        deaths_df = kyp.tsv_to_dataframe('Multiple_Cause_of_Death_2017.txt')
    else:
        print("Please choose 2016 or 2017 as parameter")
        return 0

    deaths_df = deaths_df.drop([
        'Notes', 'Year', 'State Code', 'Year Code',
        'Underlying Cause of death Code', 'Population', 'Crude Rate'
    ],
                               axis='columns')
    ##Selection of only California and Texas rows. Rows including specific cause of death are selected.
    filtered_deaths_df = deaths_df.loc[(deaths_df['State'] == 'California') |
                                       (deaths_df['State'] == 'Texas')]
    filtered_deaths_df = filtered_deaths_df.loc[
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Alcoholic cirrhosis of liver') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Accidental poisoning by and exposure to other and unspecified drugs, medicaments and biological substances'
         ) | (filtered_deaths_df['Underlying Cause of death'] ==
              'Assault by other and unspecified firearm discharge') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Accidental poisoning by and exposure to narcotics and psychodysleptics [hallucinogens], not elsewhere classified'
         ) |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Mental and behavioural disorders due to use of alcohol, dependence syndrome'
         ) | (filtered_deaths_df['Underlying Cause of death'] ==
              'Alcoholic liver disease, unspecified') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Assault by sharp object') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Mental and behavioural disorders due to use of alcohol, harmful use')
        | (filtered_deaths_df['Underlying Cause of death'] ==
           'Accidental poisoning by and exposure to alcohol') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Assault by handgun discharge') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Alcoholic hepatic failure') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Alcoholic hepatitis') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Assault by unspecified means') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Mental and behavioural disorders due to multiple drug use and use of other psychoactive substances, harmful use'
         ) | (filtered_deaths_df['Underlying Cause of death'] ==
              'Alcoholic cardiomyopathy') |
        (filtered_deaths_df['Underlying Cause of death'] ==
         'Alcoholic fatty liver')]
    return filtered_deaths_df
