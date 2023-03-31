import DoDB as db
import sqlite3

marks = ['Tiger Armor', 'Forms and Abilities', 'Forged a Shield', 'Honorable Position', 'Solo Formidable Opponent']
def getMarks():
    return(marks)

dic = {
    'tiger armor' : 'Hard Steel Circle',
    'forms and abilities' : 'Perfect Form',
    'forged a shield' : 'Sharp Stone Circle',
    'honorable position' : 'Pure Water Circle',
    'solo formidable opponent' : 'Tender Flesh Circle'
    }

karmaList = {
    'snake' : 0,
    'rat' : 0,
    'cat' : 0,
    'squirrel' : 0,
    'rabbit' : 0,
    'dog' : 0,
    'jindo dog' : 0,
    'ox' : 1,
    'bear' : 1,
    'tiger' : 2,
    'dragon' : 3,
    'spirit' : 4,
    'angel\'s tear' : 5,
    'angels tear' : 5,
    'angel tear' : 5,
    'angel' : 6
}
def getKarmaDic():
    return(karmaList)


def setName(discName, tkName):
    db.setName(discName, tkName)

#setName("Slavell#8770", "Archivist \'Sifu\' this is for testing remove me in DbManager.py")


def getNames():
    nameList = db.getNamesReport()
    cont = []
    for x in nameList:
        cont.append(x)
    cont = (', ').join(cont)
    message = "These are the names I know: {}".format(cont)
    return(message)

def checkIfKnown(discName):
    discName = str(discName)
    names = db.getNamesDiscord()
    if discName in names:
        return(True)
    else:
        return(False)

def getDiscTKname(discName):
    tkName = db.getNamesByDiscord(discName)
    return(tkName)

def setKarmaRank(person, karmaLevel, discName):
    discName = str(discName)
    person = person.lower()
    karmaLevel = karmaLevel.lower()
    if karmaLevel not in list(karmaList.keys()):
        message = "I do not understand that rank of karma. Try Ox, Bear, Tiger, Dragon, Spirit, Angels tear, or Angel"
        return(message)
    if checkIfKnown(discName) == True:
        db.setKarma(person, karmaLevel, discName)
        tkNick = db.getNamesByDiscord(discName)
        message = "Karma updated for {} to {} by {}".format(person, karmaLevel, tkNick)
    else:
        message = "I need to learn your name before I can update karma for you. Say \"My name is [name]\" For example: My name is Master Pai Mei"
    return(message)

def checkKarma(name):
    karma = db.getKarma(name.lower())
    updater = db.getNamesByDiscord(karma[1])
    date = karma[2]
    karma = karma[0][0].upper() + karma[0][1:] #convert first to 
    return(karma, updater, date)

#def setTigerArmor(person, discName):
#    discName = str(discName)
#    tkNick = db.getNamesByDiscord(discName)
#    if checkIfKnown(discName) == True:
#        try:
#            db.setTiger(person, discName)
#        except Exception as err:
#            tp = type(err)
#            if tp == sqlite3.IntegrityError:
#                message = ("Tiger armor credit already recorded for {}".format(person))
#                return(message)
#        tkNick = db.getNamesByDiscord(discName)
#        message = ("Tiger armor recorded for {} by {}".format(person, tkNick))
#        return(message)
#    else:
#        message = "I need to learn your name before I can update Tiger armor for you. Say \"My name is [name]\" For example: My name is Sensei Fuzzy Lumpkins"
#        return(message)

def setTigerArmor(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setTiger(person, discName)
        return("Tiger armor credit set for {}".format(person))
    else:
        return("I need to learn your name before I can update Tiger armor for you. Say \"My name is [name]\" For example: My name is Sensei Fuzzy Lumpkins")



def getTigerArmor(person):
    person = str(person.lower())
    try:
        updater, date = db.getTiger(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Tiger armor credit is recorded. To add a record say !add Tiger armor [name]")
    tkNick = db.getNamesByDiscord(updater)
    message = ("Tiger armor was recorded by {} on {}".format(tkNick, date))
    return(1, message)

 ##################################
def setWisdom(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setWisdom(person, discName)
        message = ("Wisdom clothes credit set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Wisdom clothes for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getWisdom(person):
    person = str(person.lower())
    try:
        updater, date = db.getWisdom(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Wisdom clothes credit is recorded. To add a record say !add Wisdom clothes [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Wisdom clothes credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)
#####################################################################################
def setSecretMastery(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setSecretMastery(person, discName)
        message = ("Secrety mastery credit set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Secret mastery for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getSecretMastery(person):
    person = str(person.lower())
    try:
        updater, date = db.getSecretMastery(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Secret mastery credit is recorded. To add a record say !add Secret mastery [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Secret mastery credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)

def setSecondaryForms(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setSecondaryForms(person, discName)
        message = ("Secondary Form credit set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Secondary Form for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getSecondaryForms(person):
    person = str(person.lower())
    try:
        updater, date = db.getSecondaryForms(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Secondary Form credit is recorded. To add a record say !add Secondary form [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Secondary Form credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)

def setPrimary(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setPrimary(person, discName)
        message = ("Primary form credit set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Primary form for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getPrimary(person):
    person = str(person.lower())
    try:
        updater, date = db.getPrimary(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Primary form credit is recorded. To add a record say !add Primary form [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Primary form credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)


#First Weapon Form Learned
#Third Weapon Form Learned
#Five or more Weapon Forms Learned




def setWeaponForms(person, count, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    count = str(count)
    if checkIfKnown(discName) == True:
        db.setWeaponForms(person, count, discName)
        message = ("{} weapon forms recorded for {}".format(count, person))
        return(message)
    else:
        message = "I need to learn your name before I can update Weapon forms for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)


def getWeaponForms(person):
    person = str(person.lower())
    reward = 0
    try:
        count, updater, date = db.getWeaponForms(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Weapon forms is recorded. To add a record say !add [count] Weapon forms [name]")
    count = int(count)
    if count >= 5:
        reward = 1
    tkNick = db.getNamesByDiscord(updater)
    message = ("{} weapon forms were recorded by {} on {}".format(str(count), tkNick, date))
    return(reward, message)

########################################################################################

def setshield(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setShield(person, discName)
        message = ("Shield credit set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Shield credit for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getShield(person):
    person = str(person.lower())
    try:
        updater, date = db.getShield(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Shield credit is recorded. To add a record say !add Shield credit [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Shield credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)
############################################################################

def setHonor(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setHonor(person, discName)
        message = ("Honorable position set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update honorable position credit for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getHonor(person):
    person = str(person.lower())
    try:
        updater, date = db.getHonor(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No honorable position credit is recorded. To add a record say !add honorable position [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Honorable position credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)

def setSolo(person, discName):
    discName = str(discName)
    tkNick = db.getNamesByDiscord(discName)
    if checkIfKnown(discName) == True:
        db.setSolo(person, discName)
        message = ("Solo Formidable Opponent set for {}".format(person))
        return(message)
    else:
        message = "I need to learn your name before I can update Solo Formidable Opponent credit for you. Say \"My name is [name]\" For example: My name is Sensei BeautyBeast"
        return(message)

def getSolo(person):
    person = str(person.lower())
    try:
        updater, date = db.getSolo(person)
    except Exception as err:
        tp = type(err)
        if tp == IndexError:
            return(0, "No Solo Formidable Opponent credit is recorded. To add a record say !add Solo formidable opponent [name]")

    tkNick = db.getNamesByDiscord(updater)
    message = ("Solo Formidable Opponent credit was recorded by {} on {}".format(tkNick, date))
    return(1, message)
