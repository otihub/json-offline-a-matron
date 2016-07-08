#!/usr/bin/env python

import json

filePath = raw_input("Paste the full path to the geoJSON you want to edit for offline use: ")
varName = raw_input("What variable are you referencing this JSON as?: ")

with open(filePath, "r+") as f:
    data = json.load(f)
    newData ="var " + varName + "="
    f.seek(0)
    f.write(newData)
    f.truncate()
    f.write(json.dumps(data))
print "Finished"
