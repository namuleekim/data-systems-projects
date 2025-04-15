# README.txt
# CS181 Project 1 - Requirement 2
# Data Parsing
# Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
# Date: 26 February 2024

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

# files:
    drugs.csv
    state_crime.csv
    Youth_Tobacco_Survey_YTS_Data.csv
    Multiple_Cause_of_Death_2016.txt
    Multiple_Cause_of_Death_2017.txt
    main.py
    README.txt
    LABREPORT.txt

# drugs.csv
        This dataset is about substance abuse (cigarettes, marijuana, cocaine,
    alcohol) among different age groups and states. Data was collected from
    individual states as part of the NSDUH study. The data ranges from 2002 to 2018
    Both totals (in thousands of people) and rates (as a percentage of the
    population) are given.
        This data was parsed with the function "csv_to_lol()" which read the csv file
    into a list of lists then converted it into a pandas dataframe.

# state_crime.csv
        The following data set has information on the crime rates and totals for
    states across the United States for a wide range of years. The crime reports are
    divided into two main categories: property and violent crime. Property crime
    refers to burglary, larceny, and motor related crime while violent crime refers
    to assault, murder, rape, and robbery. These reports go from 1960 to 2019.
        This data was parsed with the function "csv_to_dol()" which read the csv file
    first into a list of lists. It was then converted to a dictionary with the column
    names as keys. The dictionary was then converted to a pandas dataframe.

# Youth_Tobacco_Survey_YTS_Data.csv
        Provided, by the U.S. department of health and human services, this dataset 
    is about the exposure of tobacco among middle and high school stduents. The data 
    ranges from 1999-2017 and helps gain information on the exposure of tobacco 
    including tobacco usage, exposure to environmental tobacco smoke, minors'
    ability to purchase or obtain tobacco products, etc. The survey was done on the
    topics of cigarette smoking prevalence, cigarette smoking frequency, smokeless
    tobacco products prevalence and quit attempts.
        This data was parsed using the function "csv_to_dataframe()" and was
    converted directly as a pandas dataframe.


# Multiple_Cause_of_Death_2016.txt & Multiple_Cause_of_Death_2017.tx
        From CDC Wonder website. This is data from 2016 and 2017. Each State has
    different rows representing different causes of death, and what percent of the
    population it affected.
        These datasets were tab separated and were parsed using the function 
    "tsv_to_dataframe()" to be converted directly as a pandas dataframe. Instead of
    splitting on a comma, it splits on a tab.

# main.py
        this python file contains all of our funtions used for data parsing. It will
    print all of the parsed data as dataframes and pause for an input before closing.