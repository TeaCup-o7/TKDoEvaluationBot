import MarkFinder
test = []

Diviner = []
Geomancer = ["Keeper of Balance"]
Shaman = ["Favored by the Spirits"]
Druid = ["Protector of Nature"]
Monk = ["Took a step towards inner peace"]
Muse = ["Graced by the Muse"]
Merchant = ["Trustworthy trader"]
Ranger = ["Respects Nature"]
Spy = ["Initiate of the Spy Guild"]
Barbarian = ["Kin to Barbarians"]
Chongun = ["Honorary Chongun"]
Shadow = ["Engulfed by the Shadow"]


def pPWC_Test(test,list):
    print("starting praise test")
    marks = []
    PWC = 0
    pos = 0
    Spos = 0
    while pos <= len(list)-1:
        try:
            bool, mark = MarkFinder.Mark_Test(test,list[pos])
            pos = pos + 1
            if bool == True:
                marks.append(mark[0])
                PWC = PWC + 1
        except:
            pos = pos + 1
    if PWC >= 1:
        PWC = 1
    return(marks,PWC)
#print(ePWC_Test(test,Diviner))

#need PWC_Test for hard marks..

def PWC_Praise(test):
    list = [Diviner, Geomancer, Shaman, Druid, Monk, Muse, Merchant, Spy, Barbarian, Chongun, Shadow]
    pos = 0
    fPWC = 0
    diplo = 0
    marks_found = []
    while pos <= len(list)-1:
        marks, PWC = pPWC_Test(test, list[pos])
        mpos = 0
        while mpos < len(marks):
            marks_found.append(marks[mpos])
            mpos = mpos + 1
        fPWC = fPWC + PWC
        pos = pos + 1
    if fPWC == 1:
        diplo = 1
    
    if fPWC >= 2:
        diplo = 2
    return diplo, marks_found


#print(pPWC_final(test))


