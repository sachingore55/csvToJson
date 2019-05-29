import csv
import json

csvFilePath="test.csv"
jsonFilePath="My.json"

# global data
data = {}

with open(csvFilePath, encoding="utf-8-sig") as csvfile:
    #global data
    csvReader=csv.DictReader(csvfile)
    for csvRow in csvReader:
        print(csvRow)
        college=csvRow['college']
        data[college] = csvRow

print(data)

with open(jsonFilePath,"w",encoding="utf-8-sig") as jsonFile:
    jsonFile.write(json.dumps(data))

