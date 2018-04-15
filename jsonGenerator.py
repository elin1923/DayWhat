from datetime import timedelta, date
import json

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def isweekday(target):
    if (1 <= target.isoweekday() <= 5):
        return True
    else:
        return False

def converter(num):
    if (num % 2 == 0):
       return 'A'
    else:
        return 'B'

special = {
    date(2018, 5, 7): "PD Day",
    date(2018, 5, 14): "BBQ"
}

beginning = date(2018, 4, 15)
end = date(2018, 5, 15)
r = daterange(beginning, end)

d = 0

jsonFile = {}

for current in r:
    if current in special:
        #print(current.isoformat() + ": " + special[current])
        jsonFile.update({current.isoformat(): special[current]})
    elif isweekday(current):
       # print(current.isoformat() + ": " + converter(d))
        jsonFile.update({current.isoformat(): converter(d)})
        d += 1
    else:
        #print(current.isoformat() + ": weekend")
        jsonFile.update({current.isoformat(): "Weekend"})

#print(jsonFile)
print(json.dumps(jsonFile, sort_keys=True, indent=4))      