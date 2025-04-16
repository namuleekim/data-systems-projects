# README.txt
# CS181 Project 2 - Requirement 2
# Data Parsing
# Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
# Date: 16 April 2024

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

# files:
    Motor_Vehicle_Collisions_-_Crashes.csv
    Motor_Vehicle_Collisions_-_Vehicles.csv
    Motor_Vehicle_Collisions_-_Person.csv
    NYSERDA_Electric_Vehicle_Drive_Clean_Rebate_Data_Beginning_2017.csv
    Air_Quality.json
    Vehicle_Snowmobile_and_Boat_Registrations.csv
    kimyoonparsingv2.py
    README.txt
    LABREPORT.txt


# Motor_Vehicle_Collisions_-_Crashes.csv
        This dataset is about motor vehicle collisions in NYC. This dataset 
    provides information on the details of the crash event gathered from the
    police reports. However, this dataset only includes information on crash
    events in which someone is injured or killed or where is at least $1,000
    worth of damages from the crash.
        This data was parsed with the function "csv_to_dataframe" which reads 
    the csv file then construct a pandas dataframe from it.

# Motor_Vehicle_Collisions_-_Vehicles.csv
        This dataset is about motor vehicle collisions in NYC. This dataset
    provides information on each vehicle involved in the crash event. The
    information within this dataset is from the police reports in NYC. These
    police reports are submitted when someone is injured or killed or where 
    is at least $1,000 worth of damages from the crash. The information in this 
    dataset goes back to 2016 and updated regularly.
        This data was parsed with the function "csv_to_dataframe" which reads 
    the csv file then construct a pandas dataframe from it.

# Motor_Vehicle_Collisions_-_Person.csv
        This dataset is about motor vehicle collisions in NYC. This dataset
    provides information on the person involved in the crash event. The
    information within this dataset is from the police reports in NYC. These
    police reports are submitted when someone is injured or killed or where 
    is at least $1,000 worth of damages from the crash. The information on this 
    dataset also goes back to 2016 and updated since.
        This data was parsed with the function "csv_to_dataframe" which reads 
    the csv file then construct a pandas dataframe from it.


# NYSERDA_Electric_Vehicle_Drive_Clean_Rebate_Data_Beginning_2017.csv
        This dataset is about the rebate application with NYSERDA from electric
    vehicle buyers. This includes details on the specific electric vechicle 
    bought, the battery-only range of the vehicle, and the rebate amoung 
    charged by the State of New York up to $2,000. The dataset contains details
    starting from 2017.
        This data was parsed with the function "csv_to_dataframe" which reads 
    the csv file then construct a pandas dataframe from it.
    
    
# Air_Quality.json
        This dataset is about the air quality surveillance from NYC. Provided
    by the City of New York, this dataset contains information on the exposure
    of air pollutants in order to obtain information of air pollution and health.
    This dataset goes back to as far as 2005.
        This data was parsed with the function "json_to_dataframe" which reads
    the json file and then constructs a pandas dataframe from it.

# Vehicle_Snowmobile_and_Boat_Registrations.csv
        This dataset is about the registration of vehicles, snowmobiles, and boats
    in the State of New York. Provided by the State of New York, this dataset
    provides details on the registration of different types of transportation.
        This data was parsed with the function "csv_to_dataframe" which reads 
    the csv file then construct a pandas dataframe from it.
    
# kimyoonparsingv2.py
        This python file contains the actual code that reads the data and constructs
    a pandas dataframe. This code contains different functions to read different
    dataset types, such as csv and json, and construct a pandas dataframe from it.

# Caveats
        The python program takes a while to parse the large files. In the cleaning
    part of this project, we'll read the chunky csv files by specifying columns that
    we need to decrease computation time.
    