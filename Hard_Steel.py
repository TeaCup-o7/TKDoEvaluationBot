import MarkFinder
import DbManager as dbm
test = []

Star = 'Mastered the stars'
Moon = 'Understood the moon'
Sun = 'Survived the sun'
SOE = 'Forged the Staff of the Elements'
Wind = 'Captured the wind'

def Hard_Steel_Final(test):
    print("Starting Hard Steel Final")
    HSC = 0
    test = test
    input = [Star, Moon, Sun, SOE, Wind]
    pos = 0
    Marks = []
    Bool, Mark = MarkFinder.Mark_Test(test, input[0])
    while pos <= 4:
        try:
            Bool, Mark = MarkFinder.Mark_Test(test, input[pos])
            Marks.append(Mark[0])
            pos = pos + 1
        except:
            print("Error searching Hard_Steel")
            pos = pos + 1
    
    pos = 0

    while pos <= 8:
        try:
            Bool, Mark = MarkFinder.Mark_Test(test, input[pos])
            if Bool == True:
                HSC = HSC + 1
                pos = pos + 1
            else:
                pos = pos + 1
        except:
            pos = pos + 1
    print("Finished Hard Steel Final with {} points and {} returned".format(str(HSC), str(len(Marks))))
    return(HSC, Marks)

def CheckTiger(person):
    point, message = dbm.getTigerArmor(person)
    return(point, message)

def CheckWsidom(person):
    point, message = dbm.getWisdom(person)
    return(point, message)