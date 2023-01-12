import datetime as dt
import DoDB as db
import exceptionRecorder as er
def getNow(): #gets the current date in str format D M Y
    date = dt.datetime.now()
    date = dt.datetime.strftime(date, '%h-%d-%Y %H:%M CST')
    return(date)




def writeSection1(Object):
    f = open("temp"+ Object.charName + ".txt", "w")
    print("Starting to write section 1.")
    try:
        f.write("Evaluation report for: " + Object.charRank + " " + Object.charName + "."
        + "\nRequest generated for: " + Object.authTkName + " on " + getNow()  
        + "\nNote: This is report is meant to aid in - not replace an evaluation.")
        f.write("\nEvaluation number: {}".format(Object.count))

        print("Section 1 content write success!")
    except:
        print("Section 1 content exception!")
    
    f.close()
    print("File Closed for Section 1")



def writeSection2(Object):
    try:
        f = open("temp"+ Object.charName + ".txt", "a")
        print("Opened file for section 2 write.")
        f.write("\n\n-----General Evaluation-----"
            +"\n\n**Life of breath Circle**: " + str(Object.LBC) + " of 5."
            +"\n\n**Raise Spirit Circle**: " + Object.RSCmsg1 + "\n" + Object.RSCmsg2
            +"\n\n**Hard Steel Circle**: " + str(Object.HSCreward) + " of 7."
            +"\n{}".format(Object.HSCtigerMsg)
            +"\n{}".format(Object.HSCwisdomMsg)
            #+"\n*Manual check required: Tiger armor / Wisdom clothes."
            +"\n\n**Perfect Form Circle**: " + str(Object.PFCreward) + " of 5."
            +"\n{}".format(Object.PFCsecretMsg)
            +"\n{}".format(Object.PFCsecondaryMsg)
            +"\n{}".format(Object.PFCprimaryMsg)
            +"\n{}".format(Object.PFCweaponMsg)
            #+"\n*Manual check required: Forms and abilities learned."
            +"\n\n**Thousand steps Circle**: " + str(Object.TSCreward) + " of 7."
            +"\n\n**Sharp Stone Circle**: " + str(Object.SSCreward) + " of 9."
            + "\n{}".format(Object.SSCshieldMsg)
            #+"\n*Manual check required: Forged a shield in Nagnag armory."
            +"\n\n**Pure Water Circle**: " + str(Object.PWCreward) + " of 11."
            + "\n{}".format(Object.PWRhonorMsg)
            #+"\n*Manual check required: Honorary Position - Primarch"
            +"\n\n**Tender Flesh Circle**: " + str(Object.TFCreward) + " of 8."
            + "\n{}".format(Object.TFCsoloMsg)
            #+"\n*Manual check required: Solo Formidable Opponent"
            +"\n\n**Blood Spill Circle**: " + str(Object.BSCreward) + " of 10."
            +"\n\n**True Harmony Circle**: " + str(str(Object.THCreward)) + " of 9."
            +"\n\n")
        print("Section 2 write success!")
        print("Closed file for section 2 write.")
        f.close()
    except:
        er.basicHandler()
        print("!!! EXCEPTION IN SECTION2 WRITE !!!")
        

############################################################################
#Life of Breath Circle.
def writeSection3(Object): 
    print("File opened for section 3 write.")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Life Of Breath Circle~~~~~")
    
    if (Object.LBC == 0):
        f.write("\n" + Object.charName + " is level " + str(Object.level)
        + "\nPoints rewarded = " + str(Object.LBC))
    if (Object.LBC == 1):
        f.write("\n" + Object.charName + " is level " + str(Object.level)
        + "\nPoints rewarded = " + str(Object.LBC))
    if (Object.LBC > 1):
        f.write("\n" + Object.charRank + " " + Object.charName
        + "\nLife of Breath points rewarded = " + str(Object.LBC))
##########################################################################
#Raise Spirit Circle
    print("File opened for section 3 write.")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Raise Spirit Circle~~~~~" 
    + '\n' + Object.RSCmsg2
    + "\nRaise Spirit points rewarded for = " + str(Object.RSCreward))
    print("File closed for section 3 write.")
    f.close()

#########################################################################
#Hard Steel Circle
def writeSection4(Object):
    print("File opened for section 4 write.")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Hard Steel Circle~~~~~\n")
    f.write(Object.HSCtigerMsg)
    pos = 0
    while (pos < len(Object.HSCmarks)):
        f.write("\n" + Object.HSCmarks[pos])
        pos = pos + 1
    f.write('\n{}'.format(Object.HSCwisdomMsg))
    f.write("\nHard Steel points rewarded for = " + str(Object.HSCreward))

    print("File closed for section 4 write.")

##########################################################################
#Perfect form circle
def writeSection5(Object):
    print("File opened for section 5 write.")
    f = open("temp"+ Object.charName + ".txt", "a")    
    f.write("\n\n\n~~~~~Perfect Form Circle~~~~~")
    f.write('\n{}'.format(Object.PFCsecretMsg))
    f.write("\n" + Object.PFCmarks)
    f.write('\n{}'.format(Object.PFCsecondaryMsg))
    f.write('\n{}'.format(Object.PFCprimaryMsg))
    f.write('\n{}'.format(Object.PFCweaponMsg))
    f.write("\nPerfect Form points rewarded = " + str(Object.PFCreward))
    f.close()
    print("File closed for section 5 write.")

#########################################################################
#Thousand steps circle
def writeSection6(Object):
    print("File opened for section 6 write.")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Thousand Steps Circle~~~~~")
    f.write("\n" + Object.TSCmarks)
    f.write("\nThousand Steps points rewarded = " + str(Object.TSCreward))
    print("File closed for section 6 write.")
##########################################################################
#Sharp Stone Circle
def writeSection7(Object):
    print("File opened for section 7 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Sharp Stone Circle~~~~~" 
    #+ "\n*Manual check required: Forged a shield in Nagnag armory."
    + "\nSharp Stone Marks found:")
    pos = 0
    while (pos < len(Object.gather)):
        f.write("\n" + Object.gather[pos])
        pos = pos + 1
    pos = 0
    while (pos < len(Object.refine)):
        f.write("\n" + Object.refine[pos])
        pos = pos + 1
    pos = 0
    while (pos < len(Object.manuf)):
        f.write("\n" + Object.manuf[pos])
        pos = pos + 1
    pos = 0
    f.write("\nCrafting points rewarded: " + str(Object.SSCcrafting))
    f.write("\n\nOther Sharp Stone marks:")
    while (pos < len(Object.other)):
        f.write("\n" + Object.other[pos])
        pos = pos + 1
    #while loop display marks found
    f.write("\nOther Points rewarded: " + str(Object.otherScore))
    f.write('\n{}'.format(Object.SSCshieldMsg))
    f.write("\nSharp Stone Circle points rewarded: " + str(Object.SSCreward))
    f.close()
    print("File closed for section 7 write.")
#########################################################################
#Pure Water Circle
def writeSection8(Object):
    print("File opened for section 8 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Pure Water Circle~~~~~")#+ "\n*Manual check required: Honorary Position - Primarch")
    
    f.write("\nDiplomacy marks found:")
    pos = 0
    while pos < len(Object.diplomarks):
        f.write("\n" + Object.diplomarks[pos])
        pos = pos + 1
    f.write("\nDiplomacy level: " + str(Object.PWCdiplo) + "\n")
    
    f.write("\n\nCommunity Engagement marks found:")
    pos = 0
    while pos < len(Object.engMarks):
        f.write("\n" + Object.engMarks[pos])
        pos = pos + 1
    f.write("\nCommunity Engagement points: " + str(Object.PWCeng))
    
    f.write("\n\nSubpath Praise marks found:")
    pos = 0
    while pos < len(Object.praMarks):
        f.write("\n" + Object.praMarks[pos])
        pos = pos + 1
    f.write("\nSubpath Praise points rewarded: " + str(Object.PWCpra))
    
    #f.write("\n\nHonorable position marks found:")
    #pos = 0
    #while pos < len(Object.PWChonorMarks):
    #    f.write("\n" + Object.PWChonorMarks[pos])
    #    pos = pos + 1
    ###
    f.write("\n" + Object.PWRhonorMsg)
    f.write("\nCommunity Engagement points rewarded: " + str(Object.PWRhonorReward))
    ###
    f.write("\n\nHanji marks found:")
    f.write("\n" + Object.hanMarks)
    f.write("\nHanji points rewarded: " + str(Object.PWCHan))
    
    f.write("\n\nFirst qualified poetry mark found:")
    f.write("\n" + Object.poetMark)
    f.write("\nPoetry points rewarded: " + str(Object.PWCpoetry))  

    f.write("\n\nFirst qualified Story mark found:")
    f.write("\n" + Object.storyMark)
    f.write("\nStory points rewarded: " + str(Object.PWCstory))

    f.write("\n\nWeapon Lore mark found:")
    f.write("\n" + Object.wepLore)
    f.write("\nWeapon Lore points rewarded: " + str(Object.PWCwep))

    f.write("\nPure Water Circle points rewarded" + str(Object.PWCreward))
    f.close()
    print("File closed for section 8 write.")
#################################################################################
#Tender Flesh Circle
def writeSection9(Object):
    print("File opened for section 9 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Tender Flesh Circle~~~~~")
    #+ "\n*Manual check required: Solo Formidable Opponent")
    f.write("\n" + Object.TFCsoloMsg)
    f.write("\nTender Flesh Qualified marks found:")
    pos = 0
    while pos < len(Object.TFCmarks):
        f.write("\n" + Object.TFCmarks[pos])
        pos = pos + 1
    f.write("\nTender Flesh points rewarded: " + str(Object.TFCreward))
    f.close()
    print("File closed for section 9 write.")
#################################################################################
#Bloodspill Circle
def writeSection10(Object):
    print("File opened for section 10 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Blood Spill Circle~~~~~")
    f.write("\nCarnage mark found:")
    f.write("\n" + Object.BSCcarnageMark)
    f.write("\nCarnage points rewarded: " + str(Object.BSCcarnage))
    
    f.write("\n\nElixir\\Fox Hunt\\Bloodlust marks found:")
    pos = 0
    while pos < len(Object.BSCcombMarks):
        f.write("\n" + Object.BSCcombMarks[pos])
        pos = pos + 1
    f.write("\nCombined points rewarded: " + str(Object.BSCcomb))

    f.write("\n\nSubpath Victory marks found:")
    pos = 0
    while pos < len(Object.BSCspvicMarks):
        f.write("\n" + Object.BSCspvicMarks[pos])
        pos = pos + 1
    f.write("\nSubpath Victory points rewarded: " + str(Object.BSCspvic))

    f.write("\nVictorious marks found:")
    pos = 0
    while pos < len(Object.BSCvictoryMarks):
        f.write("\n" + Object.BSCvictoryMarks[pos])
        pos = pos + 1
    f.write("\nVictorious points rewarded: " + str(Object.BSCvictory))

    f.write("\nTotal Bloodspill points rewarded: " + str(Object.BSCreward))
    f.close()
    print("File closed for section 10 write.")    
    #################################################################################
#Tender Flesh Circle
def writeSection11(Object):
    print("File opened for section 11 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~Tender Flesh Circle~~~~~ ")
    #+ "\n*Manual check required: Solo Formidable Opponent")
    f.write("\n\nTender Flesh Qualified marks found:")
    pos = 0
    while pos < len(Object.TFCmarks):
        f.write("\n" + Object.TFCmarks[pos])
        pos = pos + 1
    f.write("\nTender Flesh points rewarded: " + str(Object.TFCreward))
    f.close()
    print("File closed for section 11 write.")

######################################################################################
#True Harmony Circle
def writeSection12(Object):
    print("File opened for section 12 write")
    f = open("temp"+ Object.charName + ".txt", "a")
    f.write("\n\n\n~~~~~True Harmony Circle~~~~~")
    f.write("\nTender Flesh Qualified marks found:")
    pos = 0
    while pos < len(Object.Sublime):
        f.write("\n" + Object.Sublime[pos])
        pos = pos + 1
    pos = 0
    while pos < len(Object.Greater):
        f.write("\n" + Object.Greater[pos])
        pos = pos + 1
    pos = 0
    while pos < len(Object.Lesser):
        f.write("\n" + Object.Lesser[pos])
        pos = pos + 1
    f.write("\nAlliance points rewarded: " + str(Object.allianceScore))
    f.write("\n\nHanji(ho) marks found:")
    pos = 0
    while pos < len(Object.hanMark2):
        f.write("\n" + Object.hanMark2[pos])
        pos = pos + 1
    f.write("\nHanji(ho) points rewarded: " + str(Object.hanScore))    
    f.write("\n\nStudied in the way mark found:")
    pos = 0
    while pos < len(Object.THCstudiedMark):
        f.write("\n" + Object.THCstudiedMark[pos])
        pos = pos + 1
    f.write("\nStudied points rewarded: " + str(Object.THCstudied))
    f.write("\nTrue Harmony Points rewarded: " + str(Object.THCreward))
    f.close()
    print("File closed for section 12 write.")