# -*- coding: utf-8 -*-
"""
CS181 Project 1 - Requirement 2
Data Parsing - kimyoonparsing.py
This function reads data into pandas dataframes.

Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
Date: 23 February 2024
"""
from collections import defaultdict
import pandas as pd

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

def csv_to_lol(csvname):
    """
        Takes path as input. Reads a csv file and constructs a list of lists. List
        of lists is then converted into a pandas dataframe.

        Parameters
        ----------
        csvname : string path to csv file.

        Returns
        -------
        pdframe : pandas dataframe.

        """
    lol = []
    with open(csvname, encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            lsplit = line.split(',')
            lol.append(lsplit)
        pdframe = pd.DataFrame(lol[1:], columns=lol[0])
        return pdframe


#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789


def csv_to_dol(csvname):
    """
        Takes path as input. Reads a csv file and constructs a list of lists, which
        is then converted into a dictionary of lists. Dol is then converted into a
        pandas dataframe.

        Parameters
        ----------
        csvname : string path to csv file.

        Returns
        -------
        pdframe : pandas dataframe

        """
    lol = []
    dol = defaultdict(list)
    with open(csvname, encoding='utf-8') as infile:
        for line in infile:
            line = line.strip()
            lsplit = line.split(',')
            lol.append(lsplit)
        #
    key_index = 0
    for key in lol[0]:
        for row in range(len(lol)):
            if row == 0:
                pass
            else:
                dol[key].append(lol[row][key_index])
        key_index += 1
    pdframe = pd.DataFrame.from_dict(dol)
    return pdframe


#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789


def tsv_to_dataframe(tsvname):
    """
        Takes path as input. Reads a tsv file then converts it into a pandas dataframe.

        Parameters
        ----------
        tsvname : string path to tsv file.

        Returns
        -------
        pdframe : pandas dataframe.

        """
    pdframe = pd.read_csv(tsvname, sep='\t', encoding='UTF-8')
    return pdframe


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
    pdframe = pd.read_csv(csvname)
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

    dataframe_1 = csv_to_lol('drugs.csv')
    print('>>>drugs.csv \n', dataframe_1, "\n")
    dataframe_2 = csv_to_dol('state_crime.csv')
    print('>>>state_crime.csv \n', dataframe_2, "\n")
    dataframe_3 = csv_to_dataframe('Youth_Tobacco_Survey_YTS_Data.csv')
    print('>>>Youth_Tobacco_Survey_YTS_Data.csv \n', dataframe_3, "\n")
    dataframe_4 = tsv_to_dataframe('Multiple_Cause_of_Death_2016.txt')
    print('>>>Multiple_Cause_of_Death_2016.csv \n', dataframe_4, "\n")
    dataframe_5 = tsv_to_dataframe('Multiple_Cause_of_Death_2017.txt')
    print('>>>Multiple_Cause_of_Death_2017.csv \n', dataframe_5, "\n")


#main()
#os.system('pause')
