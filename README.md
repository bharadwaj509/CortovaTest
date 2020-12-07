# CortovaTest
Cortova Assessment Test
Used Python 3.6 in the code. All the modules used are in-built. So no need to install any new ones.

## ExcelLoader.py

This file will take all the filenames and extracts the data. The data will returned in an generator object.
It handles the exceptions such as wether the file exists or if the file does not have any data. 

## JsonExtractor.py

This file takes the generator obkect from the ExcelLoader, loops through it and creates the json. 

## main.py

This is the main file to be compiled. We pass the csv files as arguments to it.<br>
<i>python main.py eg1.csv /Users/Desktop/eg2.csv</i><br>

