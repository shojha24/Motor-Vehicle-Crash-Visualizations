# Purpose: Removes whitespace from csv files
# Author: Sharabh Ojha
# Notes: This script is used to remove whitespace from csv files. An intermediate file was made to strip leading and trailing whitespace from the csv files. The intermediate file was then used to remove every other line from the csv file. This was done because every other line in the csv file was blank. The intermediate file was then deleted. This script was run for each csv file; you can change the variables used below to do that.
# Year(4)-CountyCode(2)-MunicipalityCode(2)-CaseNumber(9),County Name,Municipality Name,Crash Date,Crash Day of Week,Crash Time,Police Department Code,Police Department,Police Station,Total Killed,Total Injured,Pedestrians Killed,Pedestrians Injured,Severity,Intersection,Alcohol Involved,Hazmat Involved,Crash Type,Total Vehicles,Location,Location Direction,Route,Route Suffix,Std Rte Identifier,MilePost,Road System,Road Character,Road Horizontal Alignment,Road Grade,Road Surface Type,Surface Condition,Light Condition,Environmental Condition,Road Divided By,Temporary Traffic Control Zone,Distance To Cross Street,Unit Of Measurement,Direction From Cross Street,Cross Street Name,Is Ramp,Ramp To/From Route Name,Ramp To/From Route Direction,Posted Speed,Posted Speed Cross Street,First Harmful Event,Latitude,Longitude,Cell Phone In Use Flag,Other Property Damage,Reporting Badge No.


import csv

csv_2020 = "Monmouth2020Drivers.csv"
new_csv_2020 = "intermediate.csv"
new_new_csv_2020 = "2020Drivers.csv"
csv_2019 = "Monmouth2019Drivers.csv"
new_csv_2019 = "intermediate.csv"
new_new_csv_2019 = "2019Drivers.csv"
csv_2018 = "Monmouth2018Drivers.csv"
new_csv_2018 = "intermediate.csv"
new_new_csv_2018 = "2018Drivers.csv"

with open(csv_2020, 'r') as infile, open(new_csv_2020, 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    row_count = 0

    for row in reader:
        row = [item.strip() for item in row]
        writer.writerow(row)
        print(row)

with open(new_csv_2020, 'r') as infile, open(new_new_csv_2020, 'w') as outfile:
    for i, line in enumerate(infile):
        if i % 2 == 0:
            outfile.write(line)
