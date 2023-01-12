import MarkFinder
import Search_Parse
import DbManager as dbm


test = []
list = ['Elected Judge', 'Primogen of', 'Pledged to defend ', 'Sage of Nagnang', 'Imperial Minister of Buya', 'Royal Prime Minister of Koguryo', 'Warrior Tutor',
'Mage Tutor', 'Poet Tutor', 'Rogue Tutor','Carnage Host', 'Bloodlust host', 'Fox Hunt Host']

def Honor_Position_Test(test):
    print("Honorable position test")
    PWC = 0
    pos = 0
    marks = []
    while pos <= len(list)-1:
        try:
            bool, mark = MarkFinder.Mark_Test(test,list[pos])
            pos = pos + 1
            if bool == True:
                marks.append(mark[0])
                PWC = PWC + 1
        except:
            pos = pos + 1
    print(str(PWC) + " marks found")
    if PWC >= 1:
        PWC = 1
    return(PWC, marks)

#Honor_Position_Test(test)

############
#Hanji test#
############
#the diplo hanji test is changing the entire list.. this no longer works because the marks are changed before they're viewed here.
def Hanjiho(test):
    Hanji_list = []
    Hanji_index = 0
    pos = 0
    Score = 0
    Total = 0
    Temp_test = test.copy()
    Hanjmark = "None Found"
    while pos != 2:
        try:
            Hanji_index = Search_Parse.Search(Temp_test, 'Hanji')
            pos = pos + 1
            print("searching for Hanji(ho)")
            try:
                Hanji_list.append(Temp_test[Hanji_index])
                Temp_test.remove(Temp_test[Hanji_index])
                print("Hanji(ho) mark added")
            except:
                print("Something went wrong with Hanji(ho)!")

        except ValueError:
            print("Giving up searching for Hanji(ho) marks")
            pos = pos + 1
    hanjiBackup = Hanji_list.copy()

    try:
        H1 = Hanji_list[0].split(' ')
        H1conv = H1[2].split(',')
        Total = Total + int(H1conv[0])
        if H1[1] == 'Hanjiho':
            H1_count = 0
        else:
            H1_count = H1conv[0]
            Hanjmark = hanjiBackup[0]

    except:
        H1_count = 0

    try:
        H2 = Hanji_list[1].split(' ')
        H2conv = H2[2].split(',')
        Total = Total + int(H2conv[0])
        if H2[1] == 'Hanjiho':
            H2_count = 0
        else:
            H2_count = H2conv[0]
            Hanjmark = hanjiBackup[1]

    except:
        H2_count = 0
    #print(str(H2_count) + ' sss')
    if int(H1_count) != 0:
        if int(H1_count) >= 1:
            Score = 1
        if int(H1_count) >= 10:
            Score = 2

    if int(H2_count) != 0:
        if int(H2_count) >= 1:
            Score = 1
        if int(H2_count) >= 10:
            Score = 2  
    return Total, Score, Hanjmark, Hanji_list
    

#rint(str(Hanjiho(test)))


def Poetry(test):
    Score = 0
    place = MarkFinder.Mark_Test(test, 'in Poetry Revel')
    mark = ["none"]
    if place[0] == True:
        print(place[1][0])
        mark[0] = place[1][0]
        Score = 1
    return Score, mark[0]
#print(Poetry(test))

def Story(test):
    Score = 0
    place = MarkFinder.Mark_Test(test, 'in Story Contest')
    mark = ["none"]
    if place[0] == True:
        Score = 1
        mark[0] = place[1][0]
    return Score, mark[0]
#print(Story(test))

def Wep_lore(test):
    Score = 0
    place = MarkFinder.Mark_Test(test, 'Teller of Weapon Lore,')
    mark = ["none"]
    if place[0] == True:
        Score = 1
        mark[0] = place[1][0]
    return Score, mark[0]
#print(Wep_lore(test))


def CheckHonor(person):
    point, message = dbm.getHonor(person)
    return(point, message)