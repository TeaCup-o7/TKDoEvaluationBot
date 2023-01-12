import MarkFinder
import DbManager as dbm
test = ['Talented Food preparer']
#Ranks = ['Novice', 'Apprentice', 'Accomplished', 'Adept', 'Talented','Skilled','Expert','Master','Grand Master','Champion','Legendary']

Gather = ["woodcutter","fisherman", "farmer", "miner"]
Refining = ['smelter', 'gemcutter', 'weaver', 'food preparer']
Manufact = ['smith','carpenter', 'tailor', 'jeweler', 'chef']


def Gather_search(test): #Gathering skill search Adept + max 2
    Gpos = 0 #max 3
    test_copy = test.copy()
    marks = []
    SSC = 0
    while Gpos <=3:
        Bool, mark = MarkFinder.Mark_Test(test_copy, Gather[Gpos])
        if Bool == True:
            cust = mark[0].split(" ")
            if cust[0] == "Adept":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Talented":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Skilled":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Expert":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Master":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Grand":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Champion":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            elif cust[0] == "Legendary":
                SSC = SSC + 1
                marks.append(mark[0])
                Gpos = Gpos + 1
            else:
                test_copy.remove(mark[0])
        else:
            Gpos = Gpos + 1

    print(marks)
    return(SSC, marks)


######################################
def Refine_search(test): #tests refinery skill, skilled = 1, master+ = 2
    Rpos = 0 #max 2
    marks = []
    SSC = 0
    test_copy = test.copy()
    while Rpos <=3:
        Bool, mark = MarkFinder.Mark_Test(test_copy, Refining[Rpos])
        if Bool == True:
            cust = mark[0].split(" ")
            if cust[0] == "Adept":
                SSC = SSC + 1
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Talented":
                SSC = SSC + 1
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Skilled":
                SSC = SSC + 1
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Expert":
                SSC = SSC + 1
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Master":
                SSC = SSC + 2
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Grand":
                SSC = SSC + 2
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Champion":
                SSC = SSC + 2
                marks.append(mark[0])
                Rpos = Rpos + 1
            elif cust[0] == "Legendary":
                SSC = SSC + 2
                marks.append(mark[0])
                Rpos = Rpos + 1
            else:
                test_copy.remove(mark[0])
                Rpos = Rpos + 1
        else:
            Rpos = Rpos + 1
    return(SSC, marks)
######################################

def Manuf_search(test): #tests refinery skill, skilled = 1, master+ = 2
    Mpos = 0 #max 3
    marks = []
    SSC = 0
    test_copy = test.copy()
    while Mpos <=4:
        Bool, mark = MarkFinder.Mark_Test(test_copy, Manufact[Mpos])
        if Bool == True:
            cust = mark[0].split(" ")
            print(cust)
            if cust[0] == "Adept":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Talented":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Skilled":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Expert":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Master":
                SSC = SSC + 2
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Grand":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Champion":
                SSC = SSC + 1
                marks.append(mark[0])
                Mpos = Mpos + 1
            elif cust[0] == "Legendary":
                SSC = SSC + 2
                marks.append(mark[0])
                Mpos = Mpos + 1
            else:
                test_copy.remove(mark[0])
                Mpos = Mpos + 1
        else:
            Mpos = Mpos + 1
            print("Something went wrong")

    return(SSC, marks)
###############################################
def SSCOther(test):
    marks = []
    list = ['Master Bladecrafter', 'Wudang Sword', 'Emei Spear']
    SSC = 0
    pos = 0
    while pos <= 2:
        try:

            bool, mark = MarkFinder.Mark_Test(test,list[pos])
            pos = pos + 1
            if bool == True:
                marks.append(mark[0])
                SSC = SSC + 1
        except:
            pos = pos + 1

    return(SSC,marks)
 ##############################################       
def evalSharp(gather,refine,manufact):
        #SKill matrix
    ##########Adept, Talented, Skilled, Expert, Master, Grand Master, Champion, Legendary
    #Collect   1a,     1b,       1c,     1d,     1e,        1f,         1g,       1h
    #Refine    2a,     2b,       2c,     2d,     2e,        2f,         2g,       2h
    #Manufact  3a,     3b,       3c,     3d,     3e,        3f,         3g,       3h

    gatherMatrix   = [0,0,0,0,0,0,0,0]
    refineMatrix   = [0,0,0,0,0,0,0,0]
    manufactMatrix = [0,0,0,0,0,0,0,0]


    #matrix loader manufact
    pos = 0
    while pos < len(manufact):
        mark = manufact[pos]
        markSplit = mark.split(" ")
        if markSplit[0] == "Adept":
            manufactMatrix[0] = manufactMatrix[0] + 1
        elif markSplit[0] == "Talented":
            manufactMatrix[1] = manufactMatrix[1] + 1
        elif markSplit[0] == "Skilled": 
            manufactMatrix[2] = manufactMatrix[2] + 1
        elif markSplit[0] == "Expert":
            manufactMatrix[3] = manufactMatrix[3] + 1    
        elif markSplit[0] == "Master":
            manufactMatrix[4] = manufactMatrix[4] + 1
        elif markSplit[0] == "Grand":
            manufactMatrix[5] = manufactMatrix[5] + 1
        elif markSplit[0] == "Champion":
            manufactMatrix[6] = manufactMatrix[6] + 1
        elif markSplit[0] == "Legendary":
            manufactMatrix[7] = manufactMatrix[7] + 1
        pos = pos + 1

    #matrix loader refine
    pos = 0
    while pos < len(refine):
        mark = refine[pos]
        markSplit = mark.split(" ")
        if markSplit[0] == "Adept":
            refineMatrix[0] = refineMatrix[0] + 1
        elif markSplit[0] == "Talented":
            refineMatrix[1] = refineMatrix[1] + 1
        elif markSplit[0] == "Skilled": 
            refineMatrix[2] = refineMatrix[2] + 1
        elif markSplit[0] == "Expert":
            refineMatrix[3] = refineMatrix[3] + 1    
        elif markSplit[0] == "Master":
            refineMatrix[4] = refineMatrix[4] + 1
        elif markSplit[0] == "Grand":
            refineMatrix[5] = refineMatrix[5] + 1
        elif markSplit[0] == "Champion":
            refineMatrix[6] = refineMatrix[6] + 1
        elif markSplit[0] == "Legendary":
            refineMatrix[7] = refineMatrix[7] + 1
        pos = pos + 1

    #matrix loader gather
    pos = 0
    while pos < len(gather):
        mark = gather[pos]
        markSplit = mark.split(" ")
        if markSplit[0] == "Adept":
            gatherMatrix[0] = gatherMatrix[0] + 1
        elif markSplit[0] == "Talented":
            gatherMatrix[1] = gatherMatrix[1] + 1
        elif markSplit[0] == "Skilled": 
            gatherMatrix[2] = gatherMatrix[2] + 1
        elif markSplit[0] == "Expert":
            gatherMatrix[3] = gatherMatrix[3] + 1
        elif markSplit[0] == "Master":
            gatherMatrix[4] = gatherMatrix[4] + 1
        elif markSplit[0] == "Grand":
            gatherMatrix[5] = gatherMatrix[5] + 1
        elif markSplit[0] == "Champion":
            gatherMatrix[6] = gatherMatrix[6] + 1
        elif markSplit[0] == "Legendary":
            gatherMatrix[7] = gatherMatrix[7] + 1
        pos = pos + 1

    # adept at a craft gather +
    # adept at 2 craft gather +
    # skilled at a craft refining +
    # master at a craft  refining +
    # grand master at a craft manufacture +
    # legendary at a craft manufacture +

    #full credit scenarios
    # 2 legendary manufact
    # 1 legendary manufact + 1 adept+

    #5 point credit
    #if manufact legendary and no other mark
    #if gmaster manufact + gmaster chef = 5 credit no legendary
    #if gmaster manufact + any other mark = 5

    #SKill matrix
    ##########Adept, Talented, Skilled, Expert, Master, Grand Master, Champion, Legendary
    #Collect   1a,     1b,       1c,     1d,     1e,        1f,         1g,       1h
    #Refine    2a,     2b,       2c,     2d,     2e,        2f,         2g,       2h
    #Manufact  3a,     3b,       3c,     3d,     3e,        3f,         3g,       3h
    
                #index  0,1,2,3,4,5,6,7
    # gatherMatrix   = [0,0,0,0,0,0,0,0]
    # refineMatrix   = [0,0,0,0,0,0,0,0]
    # manufactMatrix = [0,0,0,0,0,0,0,0]
    
    #these are (all "any other")
    #sum of skills above adept in matrix
    sumGMatrix =  sum(gatherMatrix)
    sumRMatrix = sum(refineMatrix)
    sumMMatrix = sum(manufactMatrix)
    #removes legendary manufact from logic if 2 skills exist
    #this will count as "any other" but not twice.

    score = 0
    ####################
    #6 credit situations
    ####################

    #manufacture legendary any + legendary chef = full credit
    if manufactMatrix[7] >= 2:
        score = 6
        return(score)

    #manufact legendary + any other mark
    if manufactMatrix[7] == 1 and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 1):
        score = 6
        return(score)

    ####################
    #5 credit situations
    ####################

    #manufact legendary + no other mark
    if manufactMatrix[7] == 1 and (sumGMatrix == 0 and sumRMatrix == 0 and sumMMatrix == 1):
        score = 5
        return(score)

    #grand master manufact and any other mark
    if manufactMatrix[5] >= 1 or manufactMatrix[6] >= 1 and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 1):
        score = 5
        return(score)

    ####################
    #4 credit situations
    ####################

    #grand master manufact + any and no other mark
    if manufactMatrix[5] == 1 or manufactMatrix[6] == 1 and (sumGMatrix == 0 and sumRMatrix == 0 and sumMMatrix == 1):
        score = 4
        return(score)

    #master in refinery+ plus any other mark
    if manufactMatrix[4] >= 1 and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 1):
        score = 4
        return(score)
    if refineMatrix[4] >= 1 and (sumGMatrix > 0 or sumRMatrix > 1 or sumMMatrix > 0):
        score = 4
        return(score)

    ####################
    #3 credit situations
    ####################

    #only master or champion refiner+ and no other marks
    #manufact consideration
    if (manufactMatrix[4] == 1
    and (sumGMatrix == 0 and sumRMatrix == 0 and sumMMatrix == 1)):
        score = 3
        return(score)
    #refinery consideration
    if (refineMatrix[4] == 1 or refineMatrix[5] == 1 or refineMatrix[6] == 1 or refineMatrix[7] == 1
    and (sumGMatrix == 0 and sumRMatrix == 1 and sumMMatrix == 0)):
        score = 3
        return(score)

    #skilled or expert refiner+ and any other mark
    #account for ranks above skilled and below master
    #manufact consideration
    if (manufactMatrix[2] >= 1 or manufactMatrix[3] >= 1
    and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 1)):
        score = 3
        return(score)
    #refinery consideration
    if (refineMatrix[2] >= 1 or refineMatrix[3] >= 1
    and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 0)):
        score = 3
        return(score)    

    ####################
    #2 credit situations
    ####################

    #if skilled/expert refiner in manufact no other mark
    #manfact consideration
    if (manufactMatrix[2] == 1 or manufactMatrix[3] == 1 
    and (sumGMatrix == 0 and sumRMatrix == 0 and sumMMatrix == 1)):
        score = 2
        return(score)
    #refine consideration
    if (refineMatrix[2] == 1 or refineMatrix[3] == 1 
    and (sumGMatrix == 0 and sumRMatrix == 1 and sumMMatrix == 0)):
        score = 2
        return(score)

    #combo of 2 adept or higher skills
    #manufact consideration
    if (manufactMatrix[0] >= 1 or manufactMatrix[1] >= 1 
    and (sumGMatrix > 0 or sumRMatrix > 0 or sumMMatrix > 1)):
        score = 2
        return(score)
    #refiner consideration
    if (refineMatrix[0] >= 1 or refineMatrix[1] >= 1 
    and (sumGMatrix > 0 or sumRMatrix > 1 or sumMMatrix > 0)):
        score = 2
        return(score)
    #gather consideration
    #if more than one gather skill atleast adept then 2 points
    #or if 1 gather skill and any other atleast adept then 2 points
    if (sumGMatrix > 1 
    or (sumGMatrix == 1 and (sumGMatrix > 1 or sumRMatrix > 0 or sumMMatrix > 0))):
        score = 2
        return(score)
    
    ###################
    #1 credit situation
    ###################
    if (sumGMatrix >= 1 or sumRMatrix >= 1 or sumMMatrix >= 1):
        score = 1
        return(score)

        

    #adept       : gather +
    #adept(at 2) : gather +
    #skilled     : refine +
    #master      : refine +
    #grand master: manufact +
    #legendary   : manufact +


    return(score)
    

def CheckShield(person):
    point, message = dbm.getShield(person)
    return(point, message)