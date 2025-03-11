Thank you for taking the time to complete this exercise. Please read the instructions carefully.
You will be writing a python program, pushing your code to a repository, and providing us a link to your
branch, within 90 minutes of receiving these instructions.


Requirements
Output a time series CSV
1. Consumes raw data (data.json)
2. Validates / cleanses raw data
3. Outputs to a time series in ascending order in a CSV (time-series.json)


Output a proficiency by skill CSV
1. Consumes raw data (data.json)
2. Validates / cleanses raw data
3. Consume skills (skills.json) and proficiency (proficiency.json)
4. For each skill, calculate the number of records.
5. For each skill, calculate the average proficiency.
6. Output to a CSV a report of skill, number of records, average proficiency.


As example,
given set:
[{ “skill”: “K” : “proficiency” : 10 }, { “skill”: “K” : “proficiency” : 6 }, { “skill”: “A” : “proficiency” : 7 }]
result:
K, 2, 8
A, 1, 7
Visualize results
Using the output from part 2 (Create a proficiency by skill report) develop a visualization with 3
dimensions - skill, size (number of records), and proficiency (average proficiency). Choose any
visualization technology of your choice. You can add a graph in a spreadsheet, develop a web page, or
use a cloud visualization tool.
Create a README file so we know how to install and run your app, and please include any additional
information we should know about your app, or links to any external resources, like visualization
platforms. Push your code to a public repo and email dshoaf@magpie.org a link to your branch.
Time limit: 90 minutes.