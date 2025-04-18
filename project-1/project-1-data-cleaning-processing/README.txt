# README.txt
# CS181 Project 1 - Requirement 3
# Data Cleaning and Processing
# Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
# Date: 8 March 2024

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

# Independent and Dependent Variables
    The independent variables include substance use and vilolent crimes in the
  states of California and Texas. The data spans across two years 2016 to 
  2017. The dependent variables are death rates in each respective state each
  year. The deaths are specified by "Underlying Cause of Death" which allows 
  us to figure out which independent variables are more responsible for death.
  Youth Tobacco Servey data was ommited as it did not have data for California
  and Texas.

# Central Question:
    The Covid-19 pandemic was a tragic event that led to a significant number of
  deaths. Some of the factors that were directly related to death during 
  Covid-19 were masks, vaccination, and social distancing. This analysis of
  mortality rates and the factors that had strong relation to them made us
  question if we could determine factors prior to the pandemic, that were direct
  causes of death. Therefore, we decided to gather data all across the US, and pick
  the two largest states, California and Texas.


# Answer to Central Question:
    We have specified the data we will use to the two states, California and
  Texas during 2016 and 2017, we cleaned the data using selection and projection
  so that we only have such relevant columns left. We also chose to focus on 
  certain specific columns, and removed other columns that we will not be 
  using to make the data easily read. We have created a cleaned up data that
  we can use to answer our central question of why poeple die. We wanted to
  visualize using a graph to show our answer. We implemented a graph
  using the data we have cleaned using appropriate selection and projection.
  Using the crime data, we plotted the number of total violence for each
  California and Texas. We have created two graphs of the same data for each
  year(2016 and 2017). Also, using the drug data, we plotted the data of the
  columns newly created in our functions. Therefore, we plotted Alcohol,
  Illicit drugs, and Marijuana data of each state. We also created two
  separate graphs for each year. Finally, we used the death data and plotted
  the numer of deaths corresponding to a specific cause of death. We left this
  data to show specific causes of death and have created 4 graphs for each state
  and its corresponding year.
    The data says: Alcoholic cirrhosis of liver was the single biggest factor why
  people died in both states. However, the accidental (overdose) on various types
  of hard drugs was similar to alcohol cirrhosiss in California, but nearly twice
  in Texas. Texas also had a much higher number of death by firearms. The data is 
  striking becuase the number of violent crimes is much higher in California, yet
  fatal crimes are much more prevalent in Texas. On a side note, although marijuana
  use is higher than hard drugs and alcohol combined for both states, there were
  no indicators of related deaths in either state.

 # plots (folder)
    Contains .png files of the plots generated by the code in main.py

# cleaned_data_output_sample (folder)
    Contains .csv files outputted by main.py file. Any time you run main.py, new .csv
  files containing our cleaned dataframes will be generated in the work directory. They
  will be identical to the files in this folder.

 # main.py
    Runs main function displaying our process. Plots useful graphs.

# kimyoonparsing.py
    Code from part 2 of the project, reused through import.

# kimyooncleaning.py
    Code from part 3 of the project. All of our work is in this .py file. It has functions
  that alter the dataframes to slice excess data and perform selections and projections.
