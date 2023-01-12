import pandas as pd
import numpy
import DoDB as db

data = pd.read_excel(open("DoPaperwork.xlsx", "rb"))

#dataList = list(data.columns.values)
#print(dataList[1:])

karmaList = {
    1 : 'ox',
    2 : 'tiger',
    3 : 'dragon',
    4 :'spirit',
    5 :'angel\'s tear',
    6 : 'angel'
}

def testSpot(person): #
    for per in list(data.columns.values):
        if per.lower() == person.lower():
            i = 4
            while i < 69:
                print(str(data.at[i, per]), ' At index pos {}'.format(str(i)))
                i = i + 1
testSpot('sajuuk')

def GetKarmaPoint():
    for person in list(data.columns.values):
        x = 0
        i = 10
        print(person)
        while i < 16:
            mark = data.at[i, person]
            i = i + 1
            if mark == '✓':
                x = x + 1
        try:
            print()
            db.setKarma(person.lower(), karmaList[x], 'Slavell#8770')
        except:
            pass

def GetExistingPoints():
    s = 'Slavell#8770' #-5
    for person in list(data.columns.values):
        if data.at[18, person] == '✓': 
            db.setTiger(person.lower(), s)

        if data.at[23, person] == '✓': 
            db.setWisdom(person.lower(), s)
        
        if data.at[27, person] == '✓': #secret mastery
            db.setSecretMastery(person.lower(), s)
        
        if data.at[29, person] == '✓': #first weapon form
            db.setWeaponForms(person.lower(), 1, s)
        if data.at[30, person] == '✓': #3rd weapon form
            db.setWeaponForms(person.lower(), 3, s)
        if data.at[31, person] == '✓': #5 weapon form
            db.setWeaponForms(person.lower(), 5, s)
        if data.at[32, person] == '✓': #secondary form
            db.setSecondaryForms(person.lower(), s)
        if data.at[33, person] == '✓': #primary form
            db.setPrimary(person.lower(), s)

        if data.at[45, person] == '✓': #shield
            db.setShield(person.lower(), s)

        if data.at[61, person] == '✓': #honorable pos #line 63 is honorable
            db.setHonor(person.lower(), s)
        print(data.at[61])

        if data.at[74, person] == '✓': #solo
            db.setSolo(person.lower(), s)

#GetKarmaPoint()
#GetExistingPoints()