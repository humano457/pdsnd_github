### Date: 27-Dec-2020
This project and README file were created on 27-Dec-2020 as part of the Udacity Programming for Data Science Nanodegree. 

### Project Title: Bikeshare Python Project and GitHub

### Description

In this project, a Python scripts explores data and extracts information from a bike sharing company in three American cities: Chicago, New York City, and Washington D.C. The code prompts the user to select a city to be analized, how to filter the data (no filter, by month, by weekday), and whether the user wishes to see the raw data, five rows at a time. The script will continue to ask the user if he/she wishes to display particular statistics: time, trip duration, station, or user. Every time a statistic is calculated, the script will display how much time was necessary to complete the task. Finally, the user is asked if he/she wants to restart or terminate the script. 

### Files used

The required files for running this program are the python script plus the three CSV datasets:

* bikeshare.py
* washington.csv
* new_york_city.csv
* chicago.csv

### Credits and libraries

The script uses pandas, numpy, and time libraries.

### Updates

Script now shows time required for calculations in milliseconds. Script has been optimized to avoid unnecesary statistical calculations if data is not available in the dataset, i.e. selected city is Washington

### Future scope
