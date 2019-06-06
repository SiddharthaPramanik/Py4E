
# [Air Pollution](Air_Pollution.py)

The code connects to the data.gov.in API using an api-key and downloads the data to a local json file.

Methods implemented :
* Method to print a JSON data in a proper format
* Method to get the data from the API and write it to a file
* Method to create a list from the json data for a given state
* Method to get the list of state from the saved json file
* Method to get the list of cities, given the name of state
* Method to fill the missing data or 'NA' with 0
* Method to get the data for a particular state from the clean data
* Method to plot the data using matplotlib

## [Air Pollution Data](air_pollution_data.json)

This file contains the offline version of the API data. You can update it using the code.

## [Output](Output.png)

A simple scatter plot to show the amount of pollution in every state (only those for which data is available) in India.