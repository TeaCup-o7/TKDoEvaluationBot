import MarkFinder as mf








#start alliance test
def alliance(test):
    Temp_test = test.copy()

    Sublime = []
    Greaters = []
    Lessers = []
    pos = 0


    try:
        bool, mark = mf.Mark_Test(Temp_test, 'Sublime')
        Sublime.append(mark[0])
        print("Sublime added")
    except:
        print("No sublime found")
    
    while pos <= 2:
        try: 
            bool, mark = mf.Mark_Test(Temp_test, 'Greater alliance')
            Greaters.append(mark[0])
            Temp_test.remove(mark[0])
            print("A greater alliance has been added")
            pos = pos + 1
        except:
            print("Done with greaters or couldn't find")
            pos = pos + 1
    
    pos = 0
    while pos <= 5:
        try:
            bool, mark = mf.Mark_Test(Temp_test, 'Lesser alliance')
            Lessers.append(mark[0])
            Temp_test.remove(mark[0])
            print("A lesser alliance has been added")
            pos = pos + 1
        except:
            print("Done with lessers or couldn't find anymore")
            pos = pos + 1

    return (Sublime, Greaters, Lessers)



#end alliance test
#start test Hanji(ho)

def Hanjiho(test): ##wtf does this even work? lol
    Hanji_list = []
    Hanji_index = 0
    pos = 0

    while pos != 2:
        try:
            Temp_test = test.copy()
            Hanji_index = mf.Mark_Test(Temp_test, 'Hanji')
            pos = pos + 1
            print("searching for Hanji(ho)")
            try:
                print("trying to append " + str(Temp_test[Hanji_index]))
                Hanji_list.append(Temp_test[Hanji_index])
                print("trying to remove " + str(Temp_test[Hanji_index]))
                Temp_test.remove(Temp_test[Hanji_index])
                print("Hanji(ho) mark added")
            except:
                print("Something went wrong with Hanji(ho)!")

        except ValueError:
            print("Giving up searching for Hanji(ho) marks")
            pos = pos + 1

    try:
        H1 = Hanji_list[0].split(' ')
        print(H1)
        H1conv = H1[2].split(',')
        print(str(H1conv) + " H1conv")
        H1_count = H1conv[0]
        print(str(H1_count) + " H1_count")
    except:
        H1_count = 0

    try:
        H2 = Hanji_list[1].split(' ')
        H2conv = H2[2].split(',')
        H2_count = H2conv[0]
    except:
        H2_count = 0
    Hanji_count = int(H1_count) + int(H2_count)
    return(Hanji_count, Hanji_list)



###########################
#end test Hanji(ho)
#start test Studied the way
###########################

def Studiedtest(test):
    try:
        print("starting study the way test")
        credit = 0
        marks = []
        try:
            bool, mark = mf.Mark_Test(test, 'Studied the way of the')
            if bool == True:
                marks.append(mark[0])
                credit = 1
        except:
            print("error in studied test")

        return credit, marks
    except:
        print("something went wrong")