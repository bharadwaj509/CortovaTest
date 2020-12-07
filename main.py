from ExcelLoader import ExcelLoader
from JsonExtractor import JsonExtractor

import sys

# This is the mail file to be compiled
# Eg: python main.py file1.csv file2.csv
# sys.argv takes all the arguments passed along in the CLI
# ExcelLoader().loadFile() method takes the file names and processes them returning an generator object.
# The generator object will be passed to JsonExtractor().createJson() method and will be converted into json.
# The result will stored in the same folder as the code.
if len(sys.argv) > 1:
    obj = ExcelLoader().loadFile(sys.argv[1:])
    resFile = JsonExtractor().createJson(obj)
    print("Resuls are stored in", resFile)
else:
    print("No files are mentioned along with the command. Please follow the following syntax.")
    print("test.py eg1.csv eg2.csv")
