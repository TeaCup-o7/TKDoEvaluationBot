import MarkFinder

Diviner = ['I ching readings', 'Studied under the Divine Order', 'Dared to hold an unpopular opinion', 'Understood that which is small']
Geomancer = ['Experienced the Ba Gua', 'Practiced the Elemental arts', 'Balanced the flow of Qi', 'Studied with the Sages']
Shaman = ['Master of the Lore', 'Shaman Ritual(s) by', 'Captured Grave Robber', 'Found Victory before the Mudang', 'Noticed by the Mudang', 'Has survived the Deadliest']
Druid = ['Druid festivals, observed by', 'Tales Around the Fire', 'Favored by Awen', 'Flower readings, last observed by', 'Ogham Rune readings, last observed by']
Monk = ['blessed journeys,']
Muse = ['science courses at Muse College','art courses at Muse College','theatre courses at Muse College by']
Merchant = ['Merchant events, recognized', 'Recovered the Treasure', 'Treasure Hunts, appointed by']
Ranger = ['Scouted with Rangers']
Spy = ['jobs for the Spy Guild', 'bounties for the Spy Guild', 'Impressed the Spy Guild']
Barbarian = []
Chongun = ['Aided the Chongunate in', 'Has dined at the Chongun kitchen', 'services with the Chongunate,','Contemplated Knowledge with the Chongunate','Studied the Principles of Peace']
Kingdoms = ['tutor classes, last witnessed by','Has completed the Illusion trials, instructed by']


def ePWC_Test(test,list):
    print("starting Pure water Engagement test")
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

            if list == Druid:
                 if Spos == 0:
                    Spos = Spos + 1
                    print("testing special: Nature Sage")
                    bool, mark = MarkFinder.Mark_Test(test, 'Nature')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[0] == 'Nature\'s':
                            print("test 1 passed")
                        if tmark[1] == 'sage':
                            print("test 2 passed")
                        if tmark[3] == 'times,':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        print("special failed")
            if list == Barbarian:
                if Spos == 1:
                    Spos = Spos + 1
                    print("testing special: Survived challenges")
                    bool, mark = MarkFinder.Mark_Test(test, 'Survived')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[0] == 'Survived':
                            print("test 1 passed")
                        if tmark[2] == 'Challenges,':
                            print("test 2 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        pass
            if list == Kingdoms:
                 if Spos == 2:
                    Spos = Spos + 1
                    print("testing special: won clan events")
                    bool, mark = MarkFinder.Mark_Test(test, 'clan events')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[0] == 'won':
                            print("test 1 passed")
                        if tmark[2] == 'clan':
                            print("test 2 passed")
                        if tmark[3] == 'events':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        print("special failed")
            if list == Kingdoms:
                 if Spos == 3:
                    Spos = Spos + 1
                    print("testing special: Nature Sage")
                    bool, mark = MarkFinder.Mark_Test(test, 'tutor events')
                    tmark = mark[0].split(" ")
                    try:
                        if tmark[0] == 'Participated':
                            print("test 1 passed")
                        if tmark[1] == 'in  ':
                            print("test 2 passed")
                        if tmark[3] == 'tutor,':
                            print("test 3 passed")
                            marks.append(mark[0])
                            PWC = PWC + 1
                    except:
                        print("special failed")


        except:
            pos = pos + 1
    if PWC > 2:
        PWC = 2
    return(PWC, marks)
#print(ePWC_Test(test,Diviner))

#need PWC_Test for hard marks..

def PWC_Engagement(test):
    list = [Diviner, Geomancer, Shaman, Druid, Monk, Muse, Merchant, Spy, Barbarian, Chongun, Kingdoms]
    pos = 0
    fPWC = 0
    diplo = 0
    marks_found = []
    while pos <= len(list)-1:
        mpos = 0
        PWC, marks = ePWC_Test(test, list[pos])
        while mpos < len(marks):
            marks_found.append(marks[mpos])
            mpos = mpos + 1
        fPWC = fPWC + PWC
        pos = pos + 1
    if fPWC >= 10:
        diplo = diplo + 1
    return diplo, marks_found

#print(ePWC_final(test))


