Report of the project: http://crime2017.georgetown.domains/uncategorized/crime-analysis-in-washington-dc/

CrimeAndDistrict.py: Just run this file and this file will use crime2017_cleaned_preprocessed.csv, compute safety value we define ourselves and add this values to a new column.
Related tableau link: https://public.tableau.com/profile/jiachi.zhang#!/vizhome/crime2017_safety_district_sheet/Sheet1
https://public.tableau.com/profile/jiachi.zhang#!/vizhome/crime2017_safety/Safetyevaluationof7districts
Related plotly link: https://plot.ly/~milliondegree/12

d3.py: Because I cannot install d3py on python3, I test this file in python2. Hope it can run in your computer with python3 and d3py.
So just run this file. Firstly it will generate every_years'_juvenile_crime_numbers' line graph. Then you should enter control+c and this file will generate districts_crime_number's line graph.(I was going to draw a bar graph but failed. Original code is from github's example so it is real confusing)
This file is related to snapshots juvenile_crime_number_d3.png and district_crime_number.png


CrimeAndMethods.py:  Produce a pie chart about number of crime and the methods by Plotly(gun, knife and others).

Juve.py: Use the juvenilearrests.csv, compute and add some information into it and create a scatter plot with Plotly. Finally output a new csv file.
The modified csv is called juvenile_district.csv.

felony.py: Because we regard the suspects under 20 years old as juveniles, we add a new attribute isJuvenile into this csv. 
The modified csv is felony2016_IsJuvenile.

juvenile_plotly.py：This file is to use plotly to draw the line plot about the relationship between the average number of juvenile crime and months.
Related dataset: juvenilearrests_tableau.csv
Related graph: Juvenile Crime by Month.png
Related plotly link: https://plot.ly/~zeyikwong/36


*********************************************************
Graphs using Plotly:
district_crime_number.png
Juvenile arrests 2011-2017.png 
CrimeMethods.png
Juvenile Crime by Month.png

Graphs using Tableau: 
Crime and shift.png
District and Arrests.png
Felony and Juvenile.png
Safety and Number of Juvenile Crime.png
Word Cloud of Types of Juvenile Crime.png
Key Words of Juvenile Crime.png
Juvenile Crime by District.png
Juvenile Crime Category by District.png
Juvenile Crime by Month.png

Tableau URL:
https://public.tableau.com/views/2_3979/1_1?:embed=y&:display_count=yes
https://public.tableau.com/views/2_3979/2?:embed=y&:display_count=yes
https://public.tableau.com/views/2_3979/3?:embed=y&:display_count=yes
https://public.tableau.com/profile/zheyi.wang#!/vizhome/Safety_10/Safety
https://public.tableau.com/profile/zheyi.wang#!/vizhome/_27570/sheet4
https://public.tableau.com/profile/zheyi.wang#!/vizhome/byDistrict/byDistrict
https://public.tableau.com/profile/zheyi.wang#!/vizhome/byDistrict_0/byDistrict_1


Plotly URL: 
https://plot.ly/~milliondegree/12
https://plot.ly/~rivenseiun/18/methods-of-crime/
https://plot.ly/~rivenseiun/20/juvenile-arrests-2011-2017/
https://plot.ly/~zeyikwong/36
