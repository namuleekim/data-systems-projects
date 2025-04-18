# README.txt
# CS181 Project 2 - Requirement 3
# Data Cleaning and Processing
# Author/copyright: Namu Lee Kim & John Yoon. All rights reserved.
# Date: 24 April 2024

#123456789#123456789#123456789#123456789#123456789#123456789#123456789#123456789

# Independent and Dependent Variables
    The independent variables include the number of EVs and the number of 
  crashes in the City of New York from 2017 to 2020. The dependent variables 
  are number of people injurred or killed. The number is obtainable in the crash
  data. Another dependent variable is the gas emission. We can see the 
  correlation between the dependent and independent variables to answer our 
  central question of how safe are EVs.

# Central Question:
    Electric Vehicles(EVs) have become undeniably a significant factor in the 
  car industry. Tesla had a massive impact in doing so and now most car 
  factories have joined the EV market. However, in the early stages, we were 
  able to notice a significant number of casualties resulting from insufficient 
  technology. Therefore, in this project, we wanted to find out how safe are 
  Electric Vehicles in terms of their technology and cars in general. We have 
  decided to gather data regarding the number of Elevtric Vehicles, car 
  accidents, people injured or killed, and the effects on the environment. The 
  main question we aim to answer through this project is "What level of safety 
  can be expected with the integration  of Electric Vehicles (EVs) and 
  sautonomous driving technology on actual roads?""

# Answer to Central Question:
    We have narrowed down to collect data on just one state, New York. We also
  chose to focus on the years 2017-2020 which was the years EV market began to
  show impact. We cleaned all the data we have gathered using selection, 
  projection, and sql queries. We also decided to focus on specific columns and 
  removed other parts that were unnecessary in our project. This part was 
  necessary since our data was very big with too much information. Therefore, we 
  had a cleaned up data we could use to answer our question of how safe are 
  Electric Vehicles. We cleaned up the crash data so that we get a total number
  of people injured in each year, people killed in each year, crashes in each
  year. After analyzing all the data we have collected, we can see that EV 
  owners increase every year. Even though 2020 showed a significant decrease in
  the number of people injurred, it was primarily because of the Covid-19 
  pandemic. Therefore, we did not notice any relevant decrease in the number of
  people injurred or killed from car crashes. However, we were able to notice a
  significant increase in air quality. The emissions have been decreasing
  consistently which results in better air quality. Taking into account that
  EV owners are continuously increasing(from nyserda data), we could say that
  more EVs lead to better air quality. Therefore, although we cannot conclude
  or assume that Electric Vehicles lead to less crashes and casualties, we could
  imply that it leads to less emissions which improves air quality. Most 
  importantly, We did notice a slight decrease in the number of crashes. This 
  shows that EVs did in fact have a positive impact even though it failed to 
  decrease number of people injured or number of people killed. We have plotted 
  three graphs, one showing EV impact on road safety and two showing EV impact 
  on air quality. We have divided these two so we can see the physical impacts 
  of EVs as well as environmental impacts. We have also plotted the air quality 
  impacts separately to make it easier to visualize the actual changes and 
  impact. This visualizes what increases and decreases in each year.
  
 # plots (folder)
    Contains .png files of the plots generated by the code in main.py

 # main.py
    Runs main function displaying our process. Plots useful graphs.

# kimyoonparsingv2.py
    Code from part 2 of the project, reused through import.

# kimyooncleaningv2.py
    Code from part 3 of the project. All of our work is in this .py file. It
  contains code to clean up the data we will use.