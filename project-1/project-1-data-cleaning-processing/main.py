# -*- coding: utf-8 -*-
"""
CS181 Project 1 - Requirement 3
Data Cleaning and Processing

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 23 February 2024
"""
import os
import kimyooncleaning as kyc
def main():
    """
    Cleans data using functions created, plot graphs of data for each year.
    Returns
    -------
    None.

    """
    ##Calling each function to return cleaned dataframe.
    death16 = kyc.clean_cause_of_death(2016)
    death17 = kyc.clean_cause_of_death(2017)
    crime16 = kyc.clean_crime_data(2016)
    crime17 = kyc.clean_crime_data(2017)
    drugs16 = kyc.clean_drugs_data(2016)
    drugs17 = kyc.clean_drugs_data(2017)
    print('>>\'Multiple_Causes_of_Death_2016.txt\' cleaned up:\n', death16,'\n')
    print('>>\'Multiple_Causes_of_Death_2017.txt\' cleaned up:\n', death17,'\n')
    print('>>\'state_crime.csv\' cleaned up, only 2016 data:\n', crime16,'\n')
    print('>>\'state_crime.csv\' cleaned up, only 2017 data:\n', crime17,'\n')
    print('>>\'drugs.csv\' cleaned up, only 2016 data:\n', drugs16,'\n')
    print('>>\'drugs.csv\' cleaned up, only 2017 data:\n', drugs17,'\n')

    ## Output file to readable .csv file.
    crime16.to_csv('crime16.csv')
    crime17.to_csv('crime17.csv')
    death16.to_csv('death16.csv')
    death17.to_csv('death17.csv')
    drugs16.to_csv('drugs16.csv')
    drugs17.to_csv('drugs17.csv')

    ##Plotting (saved as .png within 'plots' folder).
    drugs16.plot(
        x='State',
        y=['Alcohol', 'Illicit.Drugs', 'Marijuana'],
        kind='bar',
        title = 'Number of Substance Use, 2016'
        )
    drugs17.plot(
        x='State',
        y=['Alcohol', 'Illicit.Drugs', 'Marijuana'],
        kind='bar', title = 'Number of Substance Use, 2017'
        )
    crime16.plot(
        x='State',
        y='Data.Totals.Violent.All',
        kind='bar',
        title = 'Number of Violent Crimes, 2016',
        color ='purple'
        )
    crime17.plot(
        x='State', y='Data.Totals.Violent.All',
        kind='bar', title = 'Number of Violent Crimes, 2017',
        color ='purple'
        )
    death16.loc[death16['State'] == 'California'].plot(
        x='Underlying Cause of death',
        y='Deaths',
        kind ='bar',
        title = 'Different Causes of Death, California, 2016',
        color ='r'
        )
    death16.loc[death16['State'] == 'Texas'].plot(
        x='Underlying Cause of death',
        y='Deaths',
        kind ='bar',
        title = 'Different Causes of Death, Texas, 2016',
        color ='r'
        )
    death17.loc[death17['State'] == 'California'].plot(
        x='Underlying Cause of death',
        y='Deaths',
        kind ='bar',
        title = 'Different Causes of Death, California, 2017',
        color ='r'
        )
    death17.loc[death17['State'] == 'Texas'].plot(
        x='Underlying Cause of death',
        y='Deaths',
        kind ='bar',
        title = 'Different Causes of Death, Texas, 2017',
        color ='r'
        )
main()
os.system('pause')
