
import MarkFinder
import DbManager as dbm

list = ['Skilled Apothecary','Mastered the Art of Combat','Trained in the Art of Infiltration','Scholar of the Art of Peace','Scholar of Healing Items','Understands Weapon Mechanics','Acquired their Paragon Form']

def Tender_Flesh_Test(test):
    print("Tender flesh test")
    marks = []
    PWC = 0
    pos = 0
    while pos <= len(list)-1:
        try:
            bool, mark = MarkFinder.Mark_Test(test,list[pos])
            print(bool, mark)
            pos = pos + 1
            if bool == True:
                PWC = PWC + 1
                marks.append(mark[0])
        except:
            pos = pos + 1
    return(PWC,marks)

def Checksolo(person):
    point, message = dbm.getSolo(person)
    return(point, message)
