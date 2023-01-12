import exceptionRecorder as er
import sqlite3
import ScrapeClean
import Life_of_Breath as LBC
import RaiseSpiritCircle as RSC
import Perfect_Form_Circle as PFC
import Sharp_Stone_Circle as SSC
import ThousandSteps as TSC
import Pure_Water_Diplo as PWD
import Pure_Water_Praise as PWP
import Pure_Water_Engagement as PWE
import Pure_Water_Remain as PWR
import Tender_flesh as TFC
import Bloodspill as BSC
import True_Harm as THC
import True_Harm_Final as THCF
import DbManager as dbm
import DocWriter as dw
import Hard_Steel as hs
import DoDB as db

class errTooLong(Exception):
    print('A message was too long')
class errTooShort(Exception):
    print('A message was too short')

#this script is handling creating object to handle each type of input and discord bot response.

class evalHandler:
    def __init__(self, contentIn): #accepts the raw discord input
            self.content = contentIn.content
            self.author = contentIn.author #this is the discord users real name
            self.nick = contentIn.author.nick
            self.msg = contentIn.content.split(" ")
            self.person = self.msg[1] #this is the name the way the user input
            self.count = str(int(db.getEvalCount())+1)
            self.charName = None
            self.charRank = None
            self.legend = None

            known = dbm.checkIfKnown(str(self.author))
            if known != True:
                self.message = "I need to learn your name before I can start doing paperwork for you. Say \"!My name is [name]\" For example: My name is Master Pai Mei"
                return
            self.authTkName = dbm.getDiscTKname(str(self.author))
    
            try: #main data scrape
                self.charName, self.charRank, self.legend = ScrapeClean.PullData(self.person)
                self.message = True #this is stating the evaluation worked
            except Exception as err:
                self.message = 'An error happened pulling the data from user pages.'
                er.evalExcHandler(self) #this is logging the last traceback + input data to a text file
                tp = type(err)
                if tp == AttributeError:
                    self.message =  'I was unable to do that. Its likely the user page does not exist.'
                    return
                if tp == ValueError:
                    self.message = 'I was unable to do that. Its likely the user page exists, but the legend does not.'
                    return

            try: #life of breath circle - checks level and rank
                self.level, self.LBC = LBC.LifeOfBreath(self.charRank, self.charName)
            except Exception as err:
                self.message = 'An error happened that I could not handle while checking Life of Breath. An error report was filed appropriately.'
                er.evalExcHandler(self) #this is logging the last traceback + input data to a text file
            
            self.RSCreward, self.RSCmsg1, self.RSCmsg2 = RSC.checkKarma(self)#collects data about the targets karma if it is in database
            
            self.HSCreward, self.HSCmarks = hs.Hard_Steel_Final(self.legend)
            self.HSCtigerReward, self.HSCtigerMsg = hs.CheckTiger(self.charName)
            self.HSCwisdomReward, self.HSCwisdomMsg = hs.CheckWsidom(self.charName)
            self.HSCreward = self.HSCreward + self.HSCtigerReward + self.HSCwisdomReward

            self.PFCreward, self.PFCmarks = PFC.PFC(self.legend)
            self.PFCsecretReward, self.PFCsecretMsg = PFC.CheckSecret(self.charName)
            self.PFCsecondaryReward, self.PFCsecondaryMsg = PFC.CheckSecondary(self.charName)
            self.PFCprimaryReward, self.PFCprimaryMsg = PFC.CheckPrimary(self.charName)
            self.PFCweaponReward, self.PFCweaponMsg = PFC.CheckWeapon(self.charName)
            self.PFCreward = self.PFCreward + self.PFCsecretReward + self.PFCsecondaryReward + self.PFCprimaryReward + self.PFCweaponReward
                #1 weapo mast                      #1 point                   #1 point                #1 point                   1 point


            self.TSCreward, self.TSCmarks = TSC.mqtest(self.legend)
            
            #Sharp Stone Circle
            self.empty, self.gather = SSC.Gather_search(self.legend)
            self.empty, self.refine = SSC.Refine_search(self.legend)
            self.empty, self.manuf = SSC.Manuf_search(self.legend)
            self.otherScore, self.other = SSC.SSCOther(self.legend)
            self.SSCcrafting = SSC.evalSharp(self.gather, self.refine, self.manuf)
            self.SSCreward, self.SSCshieldMsg = SSC.CheckShield(self.charName)
            self.SSCreward = self.SSCreward + self.SSCcrafting + self.otherScore 

            self.PWCdiplo, self.diplomarks = PWD.PWC_final(self.legend)
            self.PWCeng, self.engMarks = PWE.PWC_Engagement(self.legend)
            self.PWCpra, self.praMarks = PWP.PWC_Praise(self.legend)
            #self.PWChonorable, self.PWChonorMarks = Remain.Honor_Position_Test(self.legend)
            self.PWRhonorReward, self.PWRhonorMsg = PWR.CheckHonor(self.charName)
            
            self.empty, self.PWCHan, self.hanMarks, self.empty = PWR.Hanjiho(self.legend)
            self.PWCpoetry, self.poetMark = PWR.Poetry(self.legend)
            self.PWCstory, self.storyMark = PWR.Story(self.legend)
            self.PWCwep, self.wepLore = PWR.Wep_lore(self.legend)
            self.PWCreward = (self.PWCdiplo + self.PWCeng
            + self.PWCpra + self.PWRhonorReward + self.PWCHan + self.PWCpoetry 
            + self.PWCstory + self.PWCwep)

            self.TFCreward, self.TFCmarks = TFC.Tender_Flesh_Test(self.legend)
            self.TFCsoloReward, self.TFCsoloMsg = TFC.Checksolo(self.charName)
            self.TFCreward = self.TFCreward + self.TFCsoloReward
            
            self.BSCcarnage, self.BSCcarnageMark = BSC.carnage(self.legend)
            self.BSCcomb, self.BSCcombMarks = BSC.combined(self.legend)
            self.BSCspvic, self.BSCspvicMarks = BSC.SpVics(self.legend)
            self.BSCvictory, self.BSCvictoryMarks = BSC.victory(self.legend)
            self.BSCreward = self.BSCcarnage + self.BSCcomb + self.BSCspvic + self.BSCvictory
            
            self.Sublime, self.Greater, self.Lesser = THC.alliance(self.legend)
            self.allianceScore = THCF.evalAlliances(self.Sublime, self.Greater, self.Lesser)
            self.hanScore, self.hanMark2 = THCF.evalHajio(self.legend)
            self.THCstudied, self.THCstudiedMark = THC.Studiedtest(self.legend)
            self.THCreward = self.allianceScore + self.hanScore + self.THCstudied    
            
            dw.writeSection1(self) #general info
            
            dw.writeSection2(self) #general chambers info

            dw.writeSection3(self) #life of breath + Raise spirit circle

            dw.writeSection4(self) #Hard steel circle

            dw.writeSection5(self) #perfect form circle

            dw.writeSection6(self) #thousand steps circle

            dw.writeSection7(self) #sharp stone circle

            dw.writeSection8(self) #pure water circle

            dw.writeSection9(self) # Tender flesh circle

            dw.writeSection10(self) #Blood spill circle

            dw.writeSection12(self) #True Harmony circle

            #Raise spirit circle # this is karma

class addHandler:
    def __init__(self, contentIn): #contentIn is a discord message
        self.content = contentIn.content #this is how it was input by user
        self.author = contentIn.author #this is the discord users real name
        self.splitMsg = self.content.split(' ')
        self.action = self.splitMsg[1].lower()
        self.person = None
        try: #deletes extra spaces someone may insert
            for x in self.splitMsg:
                self.splitMsg.remove('')
        except:
            pass

        self.message = "General input error. Check if the syntax is correct for what you're trying to do - I was not able to understand your request."

        if self.action.lower() == 'karma': #message looks like !add karma [person] [level]
            
            try:
                if len(self.splitMsg) > 5:
                    raise errTooLong
                self.karmaLevel = (' ').join(self.splitMsg[3:])
                self.person = self.splitMsg[2].lower()
                self.message = dbm.setKarmaRank(self.person, self.karmaLevel, self.author) #exceptions? 
            except Exception as err:
                tp = type(err)
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Karma [name] [karma level]"
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Karma [name] [karma level] (max 5 words ~ !add karma Philles Angel tear)"
                else:
                    self.message = "Unhandled error happened during adding Karma. An error report was filed appropriately."
                    er.basicHandler()
#####################################################################################################

        if self.action.lower() == 'tiger': #message looks like !add tiger armor [person]
            try:
                if len(self.splitMsg) > 4:
                    raise errTooLong
                self.person = self.splitMsg[3]
                self.message = dbm.setTigerArmor(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Tiger armor credit is already recorded for {}.".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Tiger armor [name]"
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Tiger armor [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Tiger armor. An error report was filed appropriately."
                    er.basicHandler()
                    

        if self.action.lower() == 'wisdom': #message looks like !add wisdom clothes [person]         
            try:
                if len(self.splitMsg) > 4:
                    raise errTooLong  
                self.person = self.splitMsg[3]
                self.message = dbm.setWisdom(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Wisdom clothes credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add wisdom clothes [name]"
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add wisdom clothes [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding wisdom clothes. An error report was filed appropriately."
                    er.basicHandler()

                
############################################################################
        if self.action.lower() == 'secret': #message looks like !add secret mastery [person]
            try:
                if len(self.splitMsg) > 4:
                    raise errTooLong
                self.person = self.splitMsg[3]
                self.message = dbm.setSecretMastery(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Secret Mastery credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Secret mastery [name]"
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Secret mastery [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Secret mastery. An error report was filed appropriately."
                    er.basicHandler()
        if self.action.lower() == 'secondary': #message looks like !add secondary form [person]
            try:
                if len(self.splitMsg) > 4:
                    raise errTooLong
                self.person = self.splitMsg[3]
                self.message = dbm.setSecondaryForms(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Secondary form credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Secondary form [name]"
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Secondary form [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Secondary form. An error report was filed appropriately."
                    er.basicHandler()
        if self.action.lower() == 'primary': #message looks like !add primary form [person]
            try:
                if len(self.splitMsg) > 4:
                    raise errTooLong
                self.person = self.splitMsg[3]
                self.message = dbm.setPrimary(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Primary form credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Primary form [name]"
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Primary form [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Primary form. An error report was filed appropriately."
                    er.basicHandler()

        if self.splitMsg[2].lower() == 'weapon': #message looks like !add count weapon forms [person]
            try:
                if len(self.splitMsg) > 5:
                    raise errTooLong
                if len(self.splitMsg) < 5:
                    raise errTooShort
                self.person = self.splitMsg[4]
                self.count = self.splitMsg[1]
                self.message = dbm.setWeaponForms(self.person, self.count, self.author)
            except Exception as err:
                tp = type(err)
                print(tp)
                #if tp == sqlite3.IntegrityError:
                #    self.message = "Weapon forms credit is already recorded for {}".format(self.person)
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add [count] weapon forms [name]" 
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add [count] weapon forms [name]"
                    return
                if tp == errTooShort:
                    self.message = "Command syntax appears too short. Message should read !add [count] weapon forms [name]"
                else:
                    self.message = "Unhandled error happened during adding Primary form. An error report was filed appropriately."
                    er.basicHandler()
        if self.splitMsg[1].lower() == 'weapon':
            self.message = 'Did you mean to say \'!add [count] weapon forms [name]\' ?'

        if self.action.lower() == 'shield': #message looks like !add weapon forms [person]
            try:
                if len(self.splitMsg) > 5:
                    raise errTooLong
                self.person = self.splitMsg[3]
                self.message = dbm.setshield(self.person, self.author)  
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Shield credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Shield credit [name]"
                    return 
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Shield credit [name] "
                    return
                else:
                    self.message = "Unhandled error happened during adding Shield credit. An error report was filed appropriately."
                    er.basicHandler() 
                
        if self.action.lower() == 'honorable': #message looks like !add honorable position [person]
            try:
                if len(self.splitMsg) > 5:
                    raise errTooLong                
                self.person = self.splitMsg[3]
                self.message = dbm.setHonor(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Honorable position credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Honorable position [name]"  
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Honorable position [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Honorable position. An error report was filed appropriately."
                    er.basicHandler() 
        if self.action.lower() == 'solo': #message looks like !add solo formidable opponent [person]
            try:
                if len(self.splitMsg) > 5:
                    raise errTooLong                
                self.person = self.splitMsg[4]
                self.message = dbm.setSolo(self.person, self.author)
            except Exception as err:
                tp = type(err)
                if tp == sqlite3.IntegrityError:
                    self.message = "Solo formidable opponent credit is already recorded for {}".format(self.person)
                    return
                if tp == IndexError:
                    self.message = "Command syntax appears too short. Message should read !add Solo formidable opponent [name]"  
                    return
                if tp == errTooLong:
                    self.message = "Command syntax appears too long. Message should read !add Solo formidable opponent [name]"
                    return
                else:
                    self.message = "Unhandled error happened during adding Solo formidable opponent. An error report was filed appropriately."
                    er.basicHandler() 








class nameHandler:
    def __init__(self, contentIn) -> None:
        self.author = contentIn.author
        self.content = contentIn.content #this is how it was input by user
        self.splitMsg = self.content.split(' ') #message looks like this !my name is So and so Sifu
        if self.splitMsg[2].lower() == 'is':
            self.name = self.splitMsg[3:]
            self.name = ' '.join(self.name)
            dbm.setName(self.author, self.name)
            self.message = "Hello {}. I\'ll use the name you gave me to record what records you update. To change your name later, just say \'!My name is [name]\' again.".format(self.name)

class getHandler:
    def __init__(self, contentIn):
        self.content = contentIn.content #this is how it was inserted
        self.author = contentIn.author #this is the discord users real name
        self.splitMsg = self.content.split(' ')
        self.action = self.splitMsg[1].lower()
        self.person = None
        
        if self.action == 'names':
            self.message = dbm.getNames()
    




