#!/usr/bin/env python

# import modules
import json

# get user input for file path and the variable name
filePath = raw_input("Paste the full path to the geoJSON you want to edit for offline use: ")
varName = raw_input("What variable are you referencing this JSON as?: ")

# Read the JSON data and write the user input and original file back to it
with open(filePath, "r+") as f:
    data = json.load(f)
    newData ="var " + varName + "="
    f.seek(0)
    f.write(newData)
    f.truncate()
    f.write(json.dumps(data))

# Friendly Reminders
print "Finished"
print "Remember the var you are using in your js needs to match the var in the json!"
