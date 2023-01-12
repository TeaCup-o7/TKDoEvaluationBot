import MarkFinder
import DbManager as dbm

def PFC(test):
    
    input = ['Weapon master, instructed by']
    bool, mark = MarkFinder.Mark_Test(test, input[0])
    
    if bool == True:
        PFC = 1
        
    else:
        PFC = 0
        mark = ["Not a Weapon Master"]
    
    return(PFC, mark[0])

def CheckSecret(person):
    point, message = dbm.getSecretMastery(person)
    return(point, message)

def CheckSecondary(person):
    point, message = dbm.getSecondaryForms(person)
    return(point, message)

def CheckPrimary(person):
    point, message = dbm.getPrimary(person)
    return(point, message)

def CheckWeapon(person):
    point, message = dbm.getWeaponForms(person)
    return(point, message)








    