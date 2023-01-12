import MarkFinder

def carnage(test):
    score = 0
    bool, mark = MarkFinder.Mark_Test(test, 'Carnage victories')
    marks = "None"
    if bool == True:
        marks = mark[0]
        count = mark[0].split(' ')
    try:
        if int(count[0]) >= 5:
            score = 1
        if int(count[0]) >= 10:
            score = 2
        if int(count[0]) >= 25:
            score = 3
        if int(count[0]) >=50:
            score = 4
    except:
        score = 0
    return score, marks
#print(type(carnage(test)))

def combined(test):
    score = 0
    marks = []
    bool1, mark1 = MarkFinder.Mark_Test(test, 'Elixir War victories')
    bool2, mark2 = MarkFinder.Mark_Test(test, 'Fox hunt victories')
    bool3, mark3 = MarkFinder.Mark_Test(test, 'Bloodlust victories')
    
    if bool1 == True:
        count1 = mark1[0].split(' ')
        c1 = int(count1[0])
        marks.append(mark1[0])
    else:
        c1 = 0
    if bool2 == True:
        count2 = mark2[0].split(' ')
        c2 = int(count2[0])
        marks.append(mark2[0])
    else:
        c2 = 0
    if bool3 == True:
        count3 = mark3[0].split(' ')
        c3 = int(count3[0])
        marks.append(mark3[0])
    else:
        c3 = 0
    total = c1 + c2 + c3
    
    if total >= 10:
        score = 1
    if total >= 25:
        score = 2
    if total >= 50:
        score = 3
    return score, marks

#print(combined(test))

def SpVics(test):
    score = 0
    ####################
    
    bool1, mark1 = MarkFinder.Mark_Test(test, 'Sonbae Battles, observed by')
    marks = []
    try:
        if bool1 == True:
            split1 = mark1[0].split(" ")
            score = score + int(split1[2]) # # is in index 2
            marks.append(mark1[0])
    except:
        print("Sonbae Battle error")
    #####################
    
    bool2, mark2 = MarkFinder.Mark_Test(test, 'Battle scars, last honored')
    try:
        if bool2 == True:
            split2 = mark2[0].split(" ")
            score = score + int(split2[0]) # # is in index 0
            marks.append(mark2[0])
    except:
        print("Battle scar error")
    #####################
    
    bool3, mark3 = MarkFinder.Mark_Test(test, 'Do Shousha')
    try:
        if bool3 == True:
            split3 = mark3[0].split(" ") 
            score = score + int(split3[2]) # # is in index 2
            marks.append(mark3[0])
    except:
        print("Do Shousha error")
    #####################
    
    bool4, mark4 = MarkFinder.Mark_Test(test, 'Kendo Chidoja')
    try:
        if bool4 == True:
            split4 = mark4[0].split(" ")
            score = score + int(split4[2]) # # is index 2
            marks.append(mark4[0])
    except:
        print("Kendo Chidoja error")
    #####################
    
    bool5, mark5 = MarkFinder.Mark_Test(test, 'Blade Dancer')
    try:
        if bool5 == True:
            split5 = mark5[0].split(" ")
            score = score + int(split5[2]) # # is index 2
            marks.append(mark5[0])
    except:
        print(" blade dancer error")
    ######################
    
    bool6, mark6 = MarkFinder.Mark_Test(test, 'Last Man Alive')
    try:
        if bool6 == True:
            split6 = mark6[0].split(" ")
            score = score + int(split6[3]) # # index 3
            marks.append(mark6[0])
    except:
        print("Last man alive error")
    ######################
    
    bool7, mark7 = MarkFinder.Mark_Test(test, 'Barbarian events')
    try:

        if bool7 == True:
            split7 = mark7[0].split(" ")
            score = score + int(split7[2]) # # index 2
            marks.append(mark7[0])
    except:
        print("winner of barbarian events error")
    ########################
    
    bool8, mark8 = MarkFinder.Mark_Test(test, 'Has Proven Themselves in the Eyes of the Raven,')
    try:
        if bool8 == True:
            split8 = mark8[0].split(" ")
            score = score + int(split8[9]) # # index 9
            marks.append(mark8[0])
    except:
        print(" proven raven error")
    
    ########################
    bool9, mark9 = MarkFinder.Mark_Test(test, 'Archery Tournaments')
    try:
        if bool9 == True:
            split9 = mark9[0].split(" ")
            score = score + int(split9[2]) # # index 2
            marks.append(mark9[0])
    except:
        print("Archery tournament error")
    bool10, mark10 = MarkFinder.Mark_Test(test,'Sah-Ruh Tournament')
    try:
        if bool10 == True:
            split10 = mark10[0].split(" ")
            score = score + int(split10[5])# # index 5
            marks.append(mark10[0])
    except:
        print("Sah-Ruh error")
    
    vscore = 0
    if score >= 1:
        vscore = 1
    if score >= 5:
        vscore = 2

    return vscore, marks


def victory(test):
    bool1, mark1 = MarkFinder.Mark_Test(test,'Do Masai Tournaments')
    bool2, mark2 = MarkFinder.Mark_Test(test,'KSG Tournaments')
    bool3, mark3 = MarkFinder.Mark_Test(test,'Carnage Champion')
    marks = []
    score = 0
    if bool1 == True:
        score = 1
        marks.append(mark1[0])
    if bool2 == True:
        score = 1
        marks.append(mark2[0])
    if bool3 == True:
        score = 1
        marks.append(mark3[0])
    return score, marks
#print(SpVics(test))