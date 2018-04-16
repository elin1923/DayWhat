##########
#JSON Generator
#By Logan Cantin
#Edit the parameters in this file to suit you and then redirect the output into a json file.
##########

# Importing date and timedelta for date functionality, and json for conversion to a json file
from datetime import timedelta, date
import json

# A generator that yields all of the dates in a given range
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# A function to tell you if it is a weekday or not.
def isweekday(target):
    if (1 <= target.isoweekday() <= 5):
        return True
    else:
        return False

# Alternates between day A and B
def converter(num):
    if (num % 2 == 0):
       return 'A'
    else:
        return 'B'

######## EDIT THIS #############

christmas = daterange(date(2017, 12, 23), date(2018, 1, 7))

# Dictionary that holds all of the special dates/anomalies
special = {
    date(2017, 10, 6): "PD Day",
    date(2017, 10, 9): "Thanksgiving",
    date(2017, 11, 24): "PD Day",
    christmas: "Christmas",
    #exams
    date(2018, 1, 31): "PD Day",
    date(2018, 2, 19): "Family Day",
    #march break
    date(2018, 3, 30): "Good Friday",
    date(2018, 4, 2): "Easter Monday",
    date(2018, 5, 18): "PD Day",
    date(2018, 5, 21): "Victoria Day",
    date(2018, 6, 8): "PD Day",
    #exams
    date(2018, 6, 27): "Last Day of School!"

}

# Defining beginning and end dates for the generator
beginning = date(2017, 9, 5)
end = date(2018, 5, 28)

######## STOP EDITING #########

# r is the generator for all of the dates in the date range
r = daterange(beginning, end)

# Variable that determines whether it was a day a or b last
d = 0

# Dictionary that will end up being the json output
jsonFile = {}

# Cycle through the days in the date range
for current in r:
    # If the date is in the special category, add the occasion to the json file
    if current in special:
        jsonFile.update({current.isoformat(): special[current]})
    # If it is a weekday, then add whether its a day A or B to the json file and increment d
    elif isweekday(current):
        jsonFile.update({current.isoformat(): converter(d)})
        d += 1
    # If its a weekend, add weekend to the json file.
    else:
        jsonFile.update({current.isoformat(): "Weekend"})

# Print the JSON file to the output.
print(json.dumps(jsonFile, sort_keys=True, indent=4))      