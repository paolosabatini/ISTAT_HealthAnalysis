import os


def ageConverter(id):
    if int(id) == 1:
        return "15-17yo"
    elif int(id) ==2:
        return "18-19yo"
    elif int(id) ==3:
        return "20-24yo"
    elif int(id) ==4:
        return "24-34yo"
    elif int(id) ==5:
        return "35-44yo"
    elif int(id) ==6:
        return "45-54yo"
    elif int(id) ==7:
        return "55-59yo"
    elif int(id) ==8:
        return "60-64yo"
    elif int(id) ==9:
        return "65-74yo"
    elif int(id) ==9:
        return "75+yo"

def studyConverter(id):
    if int(id) == 1:
        return "None"
    elif int(id) ==2:
        return "Primary"
    elif int(id) ==3:
        return "HighSchool"
    elif int(id) ==4:
        return "BSc+"

def birthPlaceConverter(id):
    if int(id) == 1:
        return "Italy"
    elif int(id) == 2:
        return "Abroad"

def geoConverter(id):
    if int(id) == 1:
        return "NordWest"
    elif int(id) == 2:
        return "NordEast"
    elif int(id) == 3:
        return "Center"
    elif int(id) == 4:
        return "South"

def smokeConverter(id):
    if int(id) == 1:
        return "Everyday"
    elif int(id) == 2:
        return "Occasionally"
    elif int(id) == 3:
        return "No"
    else:
        return "UNKNOWN"

    
def smokeTypeConverter(id):
    if int(id) == 1:
        return "Sigarettes"
    elif int(id) == 2:
        return "Cigars"
    elif int(id) == 3:
        return "Pipe"
    elif int(id) == -2:
        return "Other"
    else:
        return "UNKNOWN"

